from ui.beach_ui import (
    show_beach_arrival,
    show_beach_exit,
    show_beach_indecision,
    show_saltwater_death,
)
from ui.theme import ask


def beach(character_name, hp):
    # Creating a list of items for the player's inventory
    inventory = ["first_aid_kit", "empty_water_bottle", "wire_string", "lighter"]

    show_beach_arrival(character_name, hp)
    choice = ask("Make a choice (1 or 2):")

    if choice == "1":
        hp = 0
        show_saltwater_death(character_name, hp)
        return "game_over", hp, inventory

    elif choice == "2":
        hp -= 20
        show_beach_exit(character_name, hp)
        return "jungle", hp, inventory

    else:
        hp -= 25
        show_beach_indecision(character_name, hp)
        return "jungle", hp, inventory