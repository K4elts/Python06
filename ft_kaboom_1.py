import alchemy.grimoire as grimoire

if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    print("Testing record light spell: "
          f"{grimoire.dark_spell_record("Fantasy", "Earth, wind and fire")}")
