from ui.cave_ui import (
    show_already_collected,
    show_cave_arrival,
    show_cave_complete,
    show_cave_death,
    show_cave_menu,
    show_correct_key,
    show_correct_rope,
    show_invalid_cave_choice,
    show_key_riddle,
    show_riddle_failed,
    show_rope_riddle,
    show_wrong_answer,
)
from ui.theme import ask


def cave(character_name, hp, inventory):
    show_cave_arrival(character_name, hp)

    while True:

        if hp <= 0:
            show_cave_death(character_name, hp)
            return "game_over", hp, inventory

        if "rope" in inventory and "key" in inventory:
            show_cave_complete(character_name, hp)
            return "bridge", hp, inventory

        show_cave_menu(character_name, hp)
        choice = ask("Make a choice:").lower()

        # LEFT PATH - KEY PUZZLE
        if choice == "1":

            if "key" in inventory:
                show_already_collected("key")
                continue

            show_key_riddle()
            attempts = 2

            while attempts > 0:
                answer = ask("Choose your answer:")

                if answer == "1":
                    show_correct_key()
                    inventory.append("key")
                    break

                else:
                    attempts -= 1
                    hp -= 1
                    show_wrong_answer(character_name, hp, attempts > 0 and hp > 0)

            if "key" not in inventory:
                show_riddle_failed()

        # RIGHT PATH - ROPE PUZZLE
        elif choice == "2":

            if "rope" in inventory:
                show_already_collected("rope")
                continue

            show_rope_riddle()
            attempts = 2

            while attempts > 0:
                answer = ask("Choose your answer:")

                if answer == "2":
                    show_correct_rope()
                    inventory.append("rope")
                    break

                else:
                    attempts -= 1
                    hp -= 1
                    show_wrong_answer(character_name, hp, attempts > 0 and hp > 0)

            if "rope" not in inventory:
                show_riddle_failed()

        # CHECK INVENTORY
        elif choice == "3":
            # show_inventory(inventory)
            print(inventory)

        else:
            show_invalid_cave_choice()