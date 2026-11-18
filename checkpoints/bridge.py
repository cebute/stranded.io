from ui.bridge_ui import (
    show_bridge_arrival,
    show_bridge_completed,
    show_bridge_death,
    show_bridge_menu,
    show_final_guardian_intro,
    show_final_riddle,
    show_first_guardian_intro,
    show_first_guardian_passed,
    show_first_riddle,
    show_gate_unlocked,
    show_invalid_answer,
    show_invalid_bridge_choice,
    show_jump_fail,
    show_no_key_for_gate,
    show_no_rope,
    show_rope_secure,
    show_second_guardian_intro,
    show_second_guardian_passed,
    show_second_riddle,
    show_wait_storm,
    show_wrong_answer,
)
from ui.theme import ask


def bridge(character_name, hp, inventory):
    show_bridge_arrival(character_name, hp)

    # Check whether the player has the rope
    if "rope" not in inventory:
        show_no_rope()
        return "cave", hp, inventory

    # Bridge decision
    while True:
        show_bridge_menu()
        choice = ask("Enter your choice:")

        if choice == "1":
            show_rope_secure(character_name, hp)
            break

        elif choice == "2":
            hp = max(0, hp - 2)
            show_jump_fail(character_name, hp)

            if hp <= 0:
                show_bridge_death(character_name, hp)
                return "game_over", hp, inventory

        elif choice == "3":
            hp = max(0, hp - 1)
            show_wait_storm(character_name, hp)

            if hp <= 0:
                show_bridge_death(character_name, hp)
                return "game_over", hp, inventory

        elif choice == "4":
            show_inventory(inventory)

        else:
            show_invalid_bridge_choice()

    # FIRST GUARDIAN
    show_first_guardian_intro()
    repeat = False

    while True:
        show_first_riddle(repeat)
        repeat = True
        answer = ask("Your answer:")

        if answer == "2":
            show_first_guardian_passed()
            break

        elif answer in ["1", "3", "4"]:
            hp = max(0, hp - 1)
            show_wrong_answer(character_name, hp, "first", hp > 0)

            if hp <= 0:
                show_bridge_death(character_name, hp)
                return "game_over", hp, inventory

        else:
            show_invalid_answer()

    # SECOND GUARDIAN
    show_second_guardian_intro()
    repeat = False

    while True:
        show_second_riddle(repeat)
        repeat = True
        answer = ask("Your answer:")

        if answer == "2":
            show_second_guardian_passed()
            break

        elif answer in ["1", "3", "4"]:
            hp = max(0, hp - 1)
            show_wrong_answer(character_name, hp, "second", hp > 0)

            if hp <= 0:
                show_bridge_death(character_name, hp)
                return "game_over", hp, inventory

        else:
            show_invalid_answer()

    # FINAL GUARDIAN
    show_final_guardian_intro()
    repeat = False

    while True:
        show_final_riddle(repeat)
        repeat = True
        answer = ask("Your answer:")

        if answer == "1":

            if "key" in inventory:
                show_gate_unlocked()
                break

            else:
                show_no_key_for_gate()
                return "cave", hp, inventory

        elif answer in ["2", "3", "4"]:
            hp = max(0, hp - 1)
            show_wrong_answer(character_name, hp, "final", hp > 0)

            if hp <= 0:
                show_bridge_death(character_name, hp)
                return "game_over", hp, inventory

        else:
            show_invalid_answer()

    # BRIDGE COMPLETED
    show_bridge_completed(character_name, hp)

    return "lighthouse", hp, inventory