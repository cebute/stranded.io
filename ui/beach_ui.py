"""Everything the player sees on the beach. No game rules live here."""

from ui.theme import ASH, BONE, RUST, level_header, say, show_status, slow_print

SALVAGE = ["Backpack", "First aid kit", "Empty water bottle", "Wire string", "Lighter"]


def show_beach_arrival(name, hp):
    """Header, salvaged items, status and the first choice."""
    level_header("THE BEACH", "where the sea left you")
    say("You pick through the wreckage and take what you can carry:", ASH)
    for number, item in enumerate(SALVAGE, 1):
        say(f"  {number}. {item}")
    say("You pack it all away.", ASH)
    print()
    show_status(name, hp)
    print()
    slow_print("I'm thirsty. I'm hungry. These wounds are getting worse.", ASH)
    slow_print("I can feel myself getting weaker.", BONE)
    print()
    say("What do I do now?")
    say("  1. Get some sea water to drink. Should quench your thirst, right?")
    say("  2. Head towards the jungle. Find food, find shade.")
    print()


def show_saltwater_death(name, hp):
    """The player drank sea water."""
    print()
    slow_print("Salt burns down your throat. For a moment, it almost helps.", ASH)
    slow_print("Then your organs begin to shut down.", RUST)
    print()
    show_status(name, hp)


def show_beach_exit(name, hp):
    """The player leaves for the jungle."""
    print()
    slow_print("You turn your back on the water and head for the treeline.", ASH)
    slow_print("The sun beats down. Every step through the sand costs you.", BONE)
    print()
    show_status(name, hp)


def show_beach_indecision(name, hp):
    """The player hesitated and was punished."""
    print()
    slow_print("Indecision costs you time.", RUST)
    slow_print("Out of sheer exhaustion, you stumble into the jungle with no plan.", ASH)
    print()
    show_status(name, hp)