"""Everything the player sees in the cave. No game rules live here."""

from ui.theme import (
    ASH, BONE, RUST,
    ground_line, level_header, say, show_status, slow_print,
)


def show_cave_arrival(name, hp):
    """Header, entrance scene and the two paths."""
    level_header("THE CAVE", "where the dark begins")
    show_status(name, hp)
    print()
    slow_print("You arrive at the entrance of a dark cave.", ASH)
    slow_print("After filling yourself up, you light a torch with your lighter and step inside.", BONE)
    slow_print("Suddenly, bats burst past you. You disturbed them.", ASH)
    slow_print("You steady your breath and keep walking until you reach a junction.", ASH)
    print()
    slow_print("Two paths lie ahead. Which will you explore?", BONE)


def show_cave_menu(name, hp):
    """The junction menu, shown every time the player returns to it."""
    print()
    show_status(name, hp)
    print()
    say("Available paths:", ASH)
    say("  1. The path to the left")
    say("  2. The path to the right")
    say("  3. Check inventory")
    print()


def show_invalid_cave_choice():
    """Bad input at the junction."""
    print()
    say("That is not an option. Choose 1, 2 or 3.", RUST)


def show_already_collected(item):
    """The player went back to a path they already cleared."""
    print()
    say(f"You have already collected the {item}.", ASH)


def show_key_riddle():
    """The statue on the left path."""
    print()
    print(ground_line())
    print()
    slow_print("You enter the left path and find an ancient statue.", ASH)
    slow_print("The statue speaks:", ASH)
    print()
    slow_print("  'I have keys but open no locks.", BONE)
    slow_print("   I have space but no room.", BONE)
    slow_print("   What am I?'", BONE)
    print()
    say("  1. A keyboard")
    say("  2. A treasure chest")
    say("  3. A door")
    say("  4. A map")
    print()


def show_rope_riddle():
    """The inscription on the right path."""
    print()
    print(ground_line())
    print()
    slow_print("You enter the right path and find a mysterious inscription.", ASH)
    slow_print("It reads:", ASH)
    print()
    slow_print("  'I am long and strong.", BONE)
    slow_print("   I help people climb, pull and cross.", BONE)
    slow_print("   What am I?'", BONE)
    print()
    say("  1. A lantern")
    say("  2. A rope")
    say("  3. A stone")
    say("  4. A wooden box")
    print()


def show_correct_key():
    """The player solved the statue's riddle."""
    print()
    slow_print("Correct. The statue reveals a hidden key.", BONE)


def show_correct_rope():
    """The player solved the inscription's riddle."""
    print()
    slow_print("Correct. You find a rope behind a loose rock.", BONE)


def show_wrong_answer(name, hp, can_retry):
    """A wrong riddle answer, with or without another attempt left."""
    print()
    say("Wrong answer. You lose 1 HP.", RUST)
    show_status(name, hp)
    if can_retry:
        say("You have one more attempt.", ASH)


def show_riddle_failed():
    """The player ran out of attempts."""
    print()
    say("You failed to solve the riddle.", ASH)


def show_cave_complete(name, hp):
    """The player holds both the rope and the key."""
    print()
    print(ground_line())
    print()
    slow_print("You hold the rope and the key.", BONE)
    slow_print("You can now proceed towards the Old Bridge.", ASH)
    print()
    show_status(name, hp)


def show_cave_death(name, hp):
    """The player's HP ran out in the cave."""
    print()
    slow_print("Your strength gives out. The dark closes in.", RUST)
    slow_print("You have run out of energy. Your adventure ends here.", ASH)
    print()
    show_status(name, hp)