from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

if TYPE_CHECKING:
    from randovania.game_description.resources.item_resource_info import ItemResourceInfo


class DamageReduction(NamedTuple):
    inventory_item: ItemResourceInfo | None
    damage_multiplier: float
