from ui.jungle_ui import (
    show_bear_death,
    show_climb_trees,
    show_fishing_repeat,
    show_fishing_success,
    show_herb_death,
    show_invalid_survival_choice,
    show_invalid_wound_choice,
    show_jungle_arrival,
    show_stream_scene,
    show_treat_wounds,
)
from ui.theme import ask


def jungle(character_name, hp, inventory):
    show_jungle_arrival(character_name, hp)

    # First decision loop: Health status
    choice = "0"
    while choice not in ["1", "2"]:
        choice = ask("What are you going to do?")

        if choice == "1":
            hp += 20
            used_kit = "first_aid_kit" in inventory
            if used_kit:
                inventory.remove("first_aid_kit")
            show_treat_wounds(character_name, hp, used_kit)

        elif choice == "2":
            hp = 0
            show_herb_death(character_name, hp)
            return "game_over", hp, inventory

        else:
            show_invalid_wound_choice()

    # Second decision loop: Survival and Destination
    show_stream_scene()

    has_fished = False

    while True:
        choice = ask("What's your decision?")

        if choice == "1":
            hp = 0
            show_bear_death(character_name, hp)
            return "game_over", hp, inventory

        elif choice == "2":
            if not has_fished:
                hp += 15
                has_fished = True
                show_fishing_success(character_name, hp)
            else:
                show_fishing_repeat()

        elif choice == "3":
            show_climb_trees(character_name, hp)
            # Instantly transitions to the cave level smoothly
            return "cave", hp, inventory

        else:
            show_invalid_survival_choice()