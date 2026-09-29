def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    split_ingredients = str.split(ingredients)
    for item in split_ingredients:
        if str.lower(item) in light_spell_allowed_ingredients():
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
