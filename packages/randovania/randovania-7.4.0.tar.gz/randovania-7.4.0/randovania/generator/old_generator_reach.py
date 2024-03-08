from __future__ import annotations

import copy
import functools
import typing
from typing import TYPE_CHECKING, NamedTuple

from randovania.game_description.db.node import Node, NodeContext
from randovania.game_description.db.resource_node import ResourceNode
from randovania.game_description.requirements.base import Requirement
from randovania.game_description.requirements.requirement_and import RequirementAnd
from randovania.game_description.requirements.requirement_set import RequirementSet
from randovania.game_description.requirements.resource_requirement import ResourceRequirement
from randovania.generator import graph as graph_module
from randovania.generator.generator_reach import GeneratorReach

if TYPE_CHECKING:
    from collections.abc import Iterator

    from randovania.game_description.game_description import GameDescription
    from randovania.resolver.state import State


def _extra_requirement_for_node(game: GameDescription, context: NodeContext, node: Node) -> Requirement | None:
    extra_requirement = None

    if node.is_resource_node:
        assert isinstance(node, ResourceNode)
        dangerous_extra = [
            ResourceRequirement.simple(resource)
            for resource, quantity in node.resource_gain_on_collect(context)
            if resource in game.dangerous_resources
        ]
        if dangerous_extra:
            extra_requirement = RequirementAnd(dangerous_extra)

    return extra_requirement


class GraphPath(NamedTuple):
    previous_node: Node | None
    node: Node
    requirement: RequirementSet

    def is_in_graph(self, digraph: graph_module.BaseGraph) -> bool:
        if self.previous_node is None:
            return False
        else:
            return digraph.has_edge(self.previous_node.node_index, self.node.node_index)

    def add_to_graph(self, digraph: graph_module.BaseGraph) -> None:
        digraph.add_node(self.node.node_index)
        if self.previous_node is not None:
            digraph.add_edge(self.previous_node.node_index, self.node.node_index, requirement=self.requirement)


class _SafeNodes(typing.NamedTuple):
    as_list: list[int]
    as_set: set[int]


class OldGeneratorReach(GeneratorReach):
    _digraph: graph_module.BaseGraph
    _state: State
    _game: GameDescription
    _reachable_paths: dict[int, list[int]] | None
    _reachable_costs: dict[int, int] | None
    _node_reachable_cache: dict[int, bool]
    _unreachable_paths: dict[tuple[int, int], RequirementSet]
    _safe_nodes: _SafeNodes | None
    _is_node_safe_cache: dict[int, bool]

    def __deepcopy__(self, memodict: dict) -> OldGeneratorReach:
        reach = OldGeneratorReach(self._game, self._state, self._digraph.copy())
        reach._unreachable_paths = copy.copy(self._unreachable_paths)
        reach._reachable_paths = self._reachable_paths
        reach._reachable_costs = self._reachable_costs
        reach._safe_nodes = self._safe_nodes

        reach._node_reachable_cache = copy.copy(self._node_reachable_cache)
        reach._is_node_safe_cache = copy.copy(self._is_node_safe_cache)
        return reach

    def __init__(self, game: GameDescription, state: State, graph: graph_module.BaseGraph):
        self._game = game
        self.all_nodes = game.region_list.all_nodes
        self._state = state
        self._digraph = graph
        self._unreachable_paths = {}
        self._reachable_paths = None
        self._node_reachable_cache = {}
        self._is_node_safe_cache = {}

    @classmethod
    def reach_from_state(
        cls,
        game: GameDescription,
        initial_state: State,
    ) -> GeneratorReach:
        reach = cls(game, initial_state, graph_module.RandovaniaGraph.new())
        game.region_list.ensure_has_node_cache()
        reach._expand_graph([GraphPath(None, initial_state.node, RequirementSet.trivial())])
        return reach

    def _potential_nodes_from(self, node: Node) -> Iterator[tuple[Node, RequirementSet]]:
        extra_requirement = _extra_requirement_for_node(self._game, self.node_context(), node)
        requirement_to_leave = node.requirement_to_leave(self._state.node_context())

        for target_node, requirement in self._game.region_list.potential_nodes_from(node, self.node_context()):
            if target_node is None:
                continue

            if requirement_to_leave != Requirement.trivial():
                requirement = RequirementAnd([requirement, requirement_to_leave])

            if extra_requirement is not None:
                requirement = RequirementAnd([requirement, extra_requirement])

            yield (
                target_node,
                requirement.patch_requirements(
                    self._state.resources,
                    1.0,
                    self._state.resource_database,
                ).as_set(self._state.resource_database),
            )

    def _expand_graph(self, paths_to_check: list[GraphPath]) -> None:
        # print("!! _expand_graph", len(paths_to_check))
        self._reachable_paths = None
        while paths_to_check:
            path = paths_to_check.pop(0)

            if path.is_in_graph(self._digraph):
                # print(">>> already in graph", self.game.region_list.node_name(path.node))
                continue

            # print(">>> will check starting at", self.game.region_list.node_name(path.node))
            path.add_to_graph(self._digraph)

            for target_node, requirement in self._potential_nodes_from(path.node):
                if requirement.satisfied(self._state.resources, self._state.energy, self._state.resource_database):
                    # print("* Queue path to", self.game.region_list.node_name(target_node))
                    paths_to_check.append(GraphPath(path.node, target_node, requirement))
                else:
                    # print("* Unreachable", self.game.region_list.node_name(target_node), ", missing:",
                    #       requirement.as_str)
                    self._unreachable_paths[path.node.node_index, target_node.node_index] = requirement
            # print("> done")

        # print("!! _expand_graph finished. Has {} edges".format(sum(1 for _ in self._digraph.edges_data())))
        self._safe_nodes = None

    def _can_advance(
        self,
        node: Node,
    ) -> bool:
        """
        Calculates if we can advance past a given node
        :param node:
        :return:
        """
        # We can't advance past a resource node if we haven't collected it
        if node.is_resource_node:
            assert isinstance(node, ResourceNode)
            return node.is_collected(self.node_context())
        else:
            return True

    def _calculate_safe_nodes(self) -> None:
        if self._safe_nodes is not None:
            return

        for component in self._digraph.strongly_connected_components():
            if self._state.node.node_index in component:
                assert self._safe_nodes is None
                self._safe_nodes = _SafeNodes(sorted(component), component)

        assert self._safe_nodes is not None

    def _calculate_reachable_paths(self) -> None:
        if self._reachable_paths is not None:
            return

        all_nodes = typing.cast(tuple[Node, ...], self.all_nodes)
        context = self.node_context()

        @functools.cache
        def _is_collected(target: int) -> int:
            node: Node = all_nodes[target]
            if node.is_resource_node:
                assert isinstance(node, ResourceNode)
                if node.is_collected(context):
                    return 0
                else:
                    return 1
            else:
                return 0

        def weight(source: int, target: int, attributes: RequirementSet) -> int:
            return _is_collected(target)

        self._reachable_costs, self._reachable_paths = self._digraph.multi_source_dijkstra(
            {self.state.node.node_index},
            weight=weight,
        )

    def is_reachable_node(self, node: Node) -> bool:
        index = node.node_index

        cached_value = self._node_reachable_cache.get(index)
        if cached_value is not None:
            return cached_value

        self._calculate_reachable_paths()
        assert self._reachable_costs is not None
        cost = self._reachable_costs.get(index)
        if cost is not None:
            if cost == 0:
                self._node_reachable_cache[index] = True
            elif cost == 1:
                self._node_reachable_cache[index] = not self._can_advance(node)
            else:
                self._node_reachable_cache[index] = False

            return self._node_reachable_cache[index]
        else:
            return False

    @property
    def connected_nodes(self) -> Iterator[Node]:
        """
        An iterator of all nodes there's an path from the reach's starting point. Similar to is_reachable_node
        :return:
        """
        self._calculate_reachable_paths()
        assert self._reachable_paths is not None
        all_nodes = typing.cast(tuple[Node, ...], self.all_nodes)
        for index in self._reachable_paths.keys():
            yield all_nodes[index]

    @property
    def state(self) -> State:
        return self._state

    @property
    def game(self) -> GameDescription:
        return self._game

    @property
    def nodes(self) -> Iterator[Node]:
        for i, node in enumerate(typing.cast(tuple[Node, ...], self.all_nodes)):
            if i in self._digraph:
                # entries in all_nodes can be None, but never for an index that's in _digraph
                # We'd do `assert node is not None`, but we're skipping that here for speed
                yield node  # type: ignore

    @property
    def safe_nodes(self) -> Iterator[Node]:
        self._calculate_safe_nodes()
        assert self._safe_nodes is not None

        all_nodes = typing.cast(tuple[Node, ...], self.all_nodes)
        for i in self._safe_nodes.as_list:
            # safe disclaimer as `nodes`
            yield all_nodes[i]  # type: ignore

    def is_safe_node(self, node: Node) -> bool:
        node_index = node.node_index
        is_safe = self._is_node_safe_cache.get(node_index)
        if is_safe is not None:
            return is_safe

        self._calculate_safe_nodes()
        assert self._safe_nodes is not None
        self._is_node_safe_cache[node_index] = node_index in self._safe_nodes.as_set
        return self._is_node_safe_cache[node_index]

    def advance_to(
        self,
        new_state: State,
        is_safe: bool = False,
    ) -> None:
        assert new_state.previous_state == self.state
        # assert self.is_reachable_node(new_state.node)

        if is_safe or self.is_safe_node(new_state.node):
            for index in [index for index, flag in self._node_reachable_cache.items() if not flag]:
                del self._node_reachable_cache[index]

            for node_index in [node_index for node_index, flag in self._is_node_safe_cache.items() if not flag]:
                del self._is_node_safe_cache[node_index]
        else:
            self._node_reachable_cache = {}
            self._is_node_safe_cache = {}

        self._state = new_state

        all_nodes = typing.cast(tuple[Node, ...], self.all_nodes)
        paths_to_check: list[GraphPath] = []

        edges_to_remove = []
        # Check if we can expand the corners of our graph
        # TODO: check if expensive. We filter by only nodes that depends on a new resource
        for edge, requirement in self._unreachable_paths.items():
            if requirement.satisfied(self._state.resources, self._state.energy, self._state.resource_database):
                from_index, to_index = edge
                paths_to_check.append(GraphPath(all_nodes[from_index], all_nodes[to_index], requirement))
                edges_to_remove.append(edge)

        for edge in edges_to_remove:
            del self._unreachable_paths[edge]

        self._expand_graph(paths_to_check)

    def act_on(self, node: ResourceNode) -> None:
        new_dangerous_resources = {
            resource
            for resource, quantity in node.resource_gain_on_collect(self.state.node_context())
            if resource in self.game.dangerous_resources
        }
        new_state = self.state.act_on_node(node)

        if new_dangerous_resources:
            edges_to_remove = []
            for source, target, requirement in self._digraph.edges_data():
                if not new_dangerous_resources.isdisjoint(requirement.dangerous_resources):
                    if not requirement.satisfied(new_state.resources, new_state.energy, new_state.resource_database):
                        edges_to_remove.append((source, target))

            for edge in edges_to_remove:
                self._digraph.remove_edge(*edge)

        self.advance_to(new_state)

    def unreachable_nodes_with_requirements(self) -> dict[Node, RequirementSet]:
        results: dict[Node, RequirementSet] = {}
        all_nodes = typing.cast(tuple[Node, ...], self.all_nodes)

        for (_, node_index), requirement in self._unreachable_paths.items():
            node = all_nodes[node_index]
            if self.is_reachable_node(node):
                continue

            requirements = requirement.patch_requirements(self.state.resources, self.state.resource_database)
            if node in results:
                results[node] = results[node].expand_alternatives(requirements)
            else:
                results[node] = requirement
        return results

    def victory_condition_satisfied(self) -> bool:
        return self.game.victory_condition.satisfied(
            self.state.resources, self.state.energy, self.state.resource_database
        )
