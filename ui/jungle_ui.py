"""Everything the player sees in the jungle. No game rules live here."""

from ui.theme import (
    ASH, BONE, RUST,
    ground_line, level_header, say, show_status, slow_print,
)


def show_jungle_arrival(name, hp):
    """Header, status and the first choice."""
    level_header("THE JUNGLE", "where the light turns green")
    show_status(name, hp)
    print()
    slow_print("The trees close in behind you. The air is thick and wet.", ASH)
    slow_print(f"You have {hp} HP left. You have to do something, or you won't make it.", BONE)
    print()
    say("  1. Treat your wounds")
    say("  2. Try some herbs you see. Perhaps they could help")
    print()


def show_treat_wounds(name, hp, used_kit):
    """The player treated their wounds, with or without the first aid kit."""
    print()
    if used_kit:
        slow_print("You tear open the first aid kit and bandage your bleeding wounds.", ASH)
    else:
        slow_print("You don't have a first aid kit.", RUST)
        slow_print("You do your best, binding the wounds with large leaves.", ASH)
    slow_print("After a few minutes, the bleeding slows. You feel a lot better.", BONE)
    slow_print("But you still need food and clean water.", ASH)
    print()
    show_status(name, hp)


def show_herb_death(name, hp):
    """The player ate the poisonous herbs."""
    print()
    slow_print("You chew the leaves. Bitter at first. Then your mouth goes numb.", ASH)
    slow_print("You should have taken those herb classes seriously.", BONE)
    slow_print("It was highly poisonous.", RUST)
    print()
    show_status(name, hp)


def show_invalid_wound_choice():
    """Bad input on the first menu."""
    print()
    say("God abeg... That's not an option. Try again!", RUST)
    print()


def show_stream_scene():
    """The stream, the deer, the fruit trees and the second choice."""
    print()
    print(ground_line())
    print()
    slow_print("While you rest, you hear the distant sound of rushing water.", ASH)
    slow_print("You follow it and find a clear stream.", BONE)
    slow_print("Fruit trees line the bank. A deer grazes a few yards away.", ASH)
    slow_print("Are you feeling lucky?", BONE)
    print()
    say("  1. Try hunting the deer")
    say("  2. Try your luck at fishing in the stream")
    say("  3. Climb the trees to gather fruit and get a better view")
    print()


def show_bear_death(name, hp):
    """The player tried to hunt the deer."""
    print()
    slow_print("You creep after the deer, eyes on nothing else.", ASH)
    slow_print("A massive, territorial bear ambushes you.", RUST)
    slow_print("Weak and weaponless, you stand no chance.", BONE)
    print()
    show_status(name, hp)


def show_fishing_success(name, hp):
    """The player caught fish."""
    print()
    slow_print("You twist your wire string into a makeshift fishing tool, and get lucky.", ASH)
    slow_print("Three fish before the line snaps. You cook and eat them over a small fire.", BONE)
    slow_print("Your hunger is satisfied. +15 HP.", BONE)
    print()
    show_status(name, hp)
    print()
    slow_print("You are fed, but you still need to find a way out of here. What next?", ASH)
    print()


def show_fishing_repeat():
    """The player tried to fish a second time."""
    print()
    say("Your fishing line is already broken. Choose another option.", ASH)
    print()


def show_climb_trees(name, hp):
    """The player climbed the trees and spotted the lighthouse."""
    print()
    slow_print("You climb a tall tree and gather wild fruit.", ASH)
    slow_print("From the high canopy, you see it: a lighthouse, far in the distance.", BONE)
    slow_print("To reach it, you must descend into a dark, rocky chasm", ASH)
    slow_print("that leads into a cave system...", ASH)
    print()
    show_status(name, hp)


def show_invalid_survival_choice():
    """Bad input on the second menu."""
    print()
    say("God abeg... That's not a valid survival choice. Choose 1, 2, or 3.", RUST)
    print()