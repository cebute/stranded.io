from ui.bridge_ui import (
    show_bridge_arrival,
    show_bridge_death,
    show_bridge_menu,
    show_gate_opens,
    show_guardian_correct,
    show_guardian_refuses,
    show_guardian_riddle,
    show_guardian_wrong,
    show_has_rope,
    show_invalid_bridge_choice,
    show_jump_fail,
    show_no_key,
    show_no_rope,
    show_rope_crossing,
    show_wait_storm,
)
# from ui.theme import ask, show_inventory


def bridge(character_name, hp, inventory):
    show_bridge_arrival(character_name, hp)

    # Check whether the player has the rope
    if "rope" not in inventory:
        show_no_rope()
        return "cave", hp, inventory

    show_has_rope()

    while True:

        if hp <= 0:
            show_bridge_death(character_name, hp)
            return "game_over", hp, inventory

        show_bridge_menu()
        choice = ask("Make a choice:").lower()

        # OPTION 1: USE ROPE
        if choice == "1":
            show_rope_crossing(character_name, hp)
            break

        # OPTION 2: JUMP ACROSS
        elif choice == "2":
            hp = max(0, hp - 2)
            show_jump_fail(character_name, hp)

        # OPTION 3: WAIT FOR THE STORM
        elif choice == "3":
            hp = max(0, hp - 1)
            show_wait_storm(character_name, hp)

        # OPTION 4: CHECK INVENTORY
        elif choice == "4":
            print(inventory)

        else:
            show_invalid_bridge_choice()

    # CHECK FOR KEY BEFORE UNLOCKING THE GATE
    if "key" not in inventory:
        show_no_key()
        return "cave", hp, inventory

    show_gate_opens()

    # GUARDIAN'S PUZZLE
    show_guardian_riddle()
    attempts = 2

    while attempts > 0:
        answer = ask("Choose your answer:")

        if answer == "2":
            show_guardian_correct(character_name, hp)
            return "lighthouse", hp, inventory

        else:
            attempts -= 1
            hp = max(0, hp - 1)
            show_guardian_wrong(character_name, hp, attempts > 0 and hp > 0)

            if hp <= 0:
                show_bridge_death(character_name, hp)
                return "game_over", hp, inventory

    show_guardian_refuses()
    return "bridge", hp, inventory