from ..elements import create_air
import alchemy.potions
from elements import create_fire


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
            f" and '{alchemy.potions.strength_potion()}' mixed with"
            f" '{create_fire()}'")
