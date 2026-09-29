from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    split_ingredients = str.split(ingredients)
    for item in split_ingredients:
        if str.lower(item) in dark_spell_allowed_ingredients():
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
