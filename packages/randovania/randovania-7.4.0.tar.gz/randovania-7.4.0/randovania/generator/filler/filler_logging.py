from __future__ import annotations

from typing import TYPE_CHECKING

from randovania.generator.filler.filler_library import UncollectedState, find_node_with_resource
from randovania.resolver import debug

if TYPE_CHECKING:
    from collections.abc import Iterable

    from randovania.game_description.db.node_identifier import NodeIdentifier
    from randovania.game_description.db.resource_node import ResourceNode
    from randovania.game_description.game_description import GameDescription
    from randovania.game_description.pickup.pickup_entry import PickupEntry
    from randovania.game_description.resources.pickup_index import PickupIndex
    from randovania.game_description.resources.resource_info import ResourceInfo
    from randovania.generator.generator_reach import GeneratorReach


def debug_print_collect_event(event: ResourceNode, game: GameDescription) -> None:
    if debug.debug_level() > 0:
        print(f"\n--> Collecting {game.region_list.node_name(event, with_region=True)}")


def print_retcon_loop_start(
    game: GameDescription,
    pickups_left: Iterable[PickupEntry],
    reach: GeneratorReach,
    player_index: int,
) -> None:
    if debug.debug_level() > 0:
        current_uncollected = UncollectedState.from_reach(reach)
        if debug.debug_level() > 1:
            extra = f", pickups_left:\n{sorted({pickup.name for pickup in pickups_left})}"
        else:
            extra = ""

        print("\n===============================")
        print(
            (
                "\n>>> Player {}: From {}, {} reachable nodes, {} safe nodes, "
                "{} open pickup indices, {} open events{}"
            ).format(
                player_index,
                game.region_list.node_name(reach.state.node, with_region=True),
                sum(1 for n in reach.nodes if reach.is_reachable_node(n)),
                sum(1 for n in reach.nodes if reach.is_safe_node(n)),
                len(current_uncollected.indices),
                len(current_uncollected.events),
                extra,
            )
        )

        if debug.debug_level() > 2:
            print("\nCurrent reach:")
            for node in reach.nodes:
                print(
                    "[{!s:>5}, {!s:>5}] {}".format(
                        reach.is_reachable_node(node), reach.is_safe_node(node), game.region_list.node_name(node)
                    )
                )


def print_new_resources(
    game: GameDescription,
    reach: GeneratorReach,
    seen_count: dict[ResourceInfo, int],
    label: str,
) -> None:
    if debug.debug_level() > 1:
        region_list = game.region_list
        for index, count in seen_count.items():
            if count == 1:
                node = find_node_with_resource(index, reach.node_context(), region_list.iterate_nodes())
                print(f"-> New {label}: {region_list.node_name(node, with_region=True)}")


def print_new_node_identifiers(
    game: GameDescription,
    seen_count: dict[NodeIdentifier, int],
    label: str,
) -> None:
    if debug.debug_level() > 1:
        region_list = game.region_list
        for identifier, count in seen_count.items():
            if count == 1:
                node = region_list.node_by_identifier(identifier)
                print(f"-> New {label}: {region_list.node_name(node, with_region=True)}")


def print_new_pickup_index(player: int, game: GameDescription, location: PickupIndex) -> None:
    if debug.debug_level() > 1:
        region_list = game.region_list
        node = region_list.node_from_pickup_index(location)
        print(f"-> New Pickup Index: Player {player}'s {region_list.node_name(node, with_region=True)}")
