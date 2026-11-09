"""Everything the player sees at the Old Bridge. No game rules live here."""

from ui.theme import (
    ASH, BONE, RUST,
    ground_line, level_header, say, show_status, slow_print,
)


def show_bridge_arrival(name, hp):
    """Header and the broken bridge."""
    level_header("THE OLD BRIDGE", "where the wind tests every plank")
    show_status(name, hp)
    print()
    slow_print("After leaving the cave, you arrive at an old wooden bridge.", ASH)
    slow_print("Part of it has collapsed.", BONE)
    slow_print("Strong winds shake the remaining planks.", ASH)
    print()


def show_no_rope():
    """The player arrived without a rope."""
    slow_print("You need a rope to secure the broken bridge.", ASH)
    slow_print("You don't have one.", RUST)
    slow_print("You must return to the cave.", ASH)


def show_has_rope():
    """The player has the rope."""
    slow_print("You have the rope you took from the cave.", BONE)
    slow_print("You can use it to secure your crossing.", ASH)


def show_bridge_menu():
    """The bridge menu, shown every time the player returns to it."""
    print()
    say("What would you like to do?", ASH)
    say("  1. Use the rope to secure the bridge")
    say("  2. Attempt to jump across")
    say("  3. Wait for the storm to pass")
    say("  4. Check inventory")
    print()


def show_invalid_bridge_choice():
    """Bad input on the bridge menu."""
    print()
    say("That is not an option. Choose 1, 2, 3 or 4.", RUST)


def show_rope_crossing(name, hp):
    """The player secured the rope and crossed."""
    print()
    slow_print("You tie the rope around a strong wooden post.", ASH)
    slow_print("You use it to steady yourself as you cross.", ASH)
    slow_print("After a difficult journey, you reach the other side.", BONE)
    print()
    show_status(name, hp)


def show_jump_fail(name, hp):
    """The player tried to jump the gap."""
    print()
    slow_print("You try to jump across the broken section.", ASH)
    slow_print("You lose your balance and fall back onto the bridge.", BONE)
    slow_print("You lose 2 HP.", RUST)
    print()
    show_status(name, hp)


def show_wait_storm(name, hp):
    """The player waited out the storm."""
    print()
    slow_print("You wait for the storm to calm.", ASH)
    slow_print("The cold drains what little energy you have left.", BONE)
    slow_print("You lose 1 HP.", RUST)
    print()
    show_status(name, hp)


def show_no_key():
    """The player crossed but has no key for the gate."""
    print()
    print(ground_line())
    print()
    slow_print("You cross the bridge and find an ancient gate.", ASH)
    slow_print("It is locked. You need a key.", RUST)
    slow_print("Return to the cave and search for the key.", ASH)


def show_gate_opens():
    """The key fits the gate."""
    print()
    print(ground_line())
    print()
    slow_print("An ancient gate stands on the other side of the bridge.", ASH)
    slow_print("You insert your key into the lock, and the gate opens.", BONE)


def show_guardian_riddle():
    """The guardian and his riddle."""
    print()
    slow_print("Suddenly, an old guardian appears.", ASH)
    slow_print("'Before you proceed, answer my riddle.'", BONE)
    print()
    slow_print("  What has cities but no houses,", BONE)
    slow_print("  forests but no trees,", BONE)
    slow_print("  and rivers but no water?", BONE)
    print()
    say("  1. A painting")
    say("  2. A map")
    say("  3. A book")
    say("  4. A mirror")
    print()


def show_guardian_correct(name, hp):
    """The player answered correctly."""
    print()
    slow_print("Correct. The guardian is impressed.", BONE)
    slow_print("He steps aside and allows you to proceed.", ASH)
    slow_print("Far off, you can see the lighthouse.", BONE)
    print()
    show_status(name, hp)


def show_guardian_wrong(name, hp, can_retry):
    """A wrong answer, with or without another attempt left."""
    print()
    say("Incorrect answer. You lose 1 HP.", RUST)
    show_status(name, hp)
    if can_retry:
        say("You have one final attempt.", ASH)


def show_guardian_refuses():
    """The player ran out of attempts."""
    print()
    slow_print("The guardian refuses to let you proceed.", RUST)
    slow_print("You must return and try again.", ASH)


def show_bridge_death(name, hp):
    """The player's HP ran out at the bridge."""
    print()
    slow_print("The wind and the cold take the last of your strength.", RUST)
    slow_print("You have run out of energy.", ASH)
    print()
    show_status(name, hp)