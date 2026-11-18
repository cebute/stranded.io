"""Everything the player sees at the Old Bridge. No game rules live here."""

from ui.theme import (
    ASH, BONE, RUST, WIDTH,
    ground_line, level_header, say, show_status, slow_print, spaced,
)

# What each guardian says after a wrong answer.
RETRY_LINES = {
    "first": "The guardian demands another attempt.",
    "second": "The guardian asks you to try again.",
    "final": "The guardian demands another attempt.",
}


def _scene_title(title):
    """A smaller heading inside the level, for each guardian."""
    print()
    print(ground_line())
    say(f"{spaced(title):^{WIDTH}}", BONE)
    print(ground_line())
    print()


def _speak(lines, color, repeat):
    """Type the lines out the first time, print them instantly when repeated."""
    show = say if repeat else slow_print
    for line in lines:
        show(line, color)


def _show_options(options):
    """Print numbered answer options."""
    print()
    for number, option in enumerate(options, 1):
        say(f"  {number}. {option}")
    print()


# ---------- The bridge itself ----------

def show_bridge_arrival(name, hp):
    """Header and the broken bridge."""
    level_header("THE OLD BRIDGE", "where the wind tests every plank")
    show_status(name, hp)
    print()
    slow_print("You arrive at an old wooden bridge.", ASH)
    slow_print("Part of the bridge has collapsed.", BONE)
    slow_print("Strong winds shake the remaining wooden planks.", ASH)


def show_no_rope():
    """The player arrived without a rope."""
    print()
    slow_print("You do not have a rope.", RUST)
    slow_print("You cannot safely secure the bridge.", ASH)
    slow_print("You must return to the cave and find one.", ASH)


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


def show_rope_secure(name, hp):
    """The player secured the bridge with the rope."""
    print()
    slow_print("You use your rope to secure the damaged bridge.", ASH)
    slow_print("The bridge is now stable enough to cross.", BONE)
    print()
    show_status(name, hp)


def show_jump_fail(name, hp):
    """The player tried to jump the gap."""
    print()
    slow_print("You attempt to jump across, but lose your balance.", ASH)
    slow_print("You lose 2 HP.", RUST)
    print()
    show_status(name, hp)


def show_wait_storm(name, hp):
    """The player waited out the storm."""
    print()
    slow_print("You wait for the storm to calm down.", ASH)
    slow_print("You lose 1 HP.", RUST)
    print()
    show_status(name, hp)


# ---------- The three guardians ----------

def show_first_guardian_intro():
    """The statues come alive."""
    _scene_title("THE FIRST GUARDIAN")
    slow_print("Three stone statues suddenly come alive.", ASH)
    slow_print("The first statue blocks the entrance to the bridge.", BONE)


def show_first_riddle(repeat=False):
    """The echo riddle."""
    print()
    _speak(["The guardian speaks:"], ASH, repeat)
    print()
    _speak(["  'I speak without a mouth and hear without ears.",
            "   I have no body, but I come alive with the wind.",
            "   What am I?'"], BONE, repeat)
    _show_options(["A shadow", "An echo", "A bird", "A ghost"])


def show_first_guardian_passed():
    """The player answered the first riddle."""
    print()
    slow_print("Correct. The guardian moves aside.", BONE)


def show_second_guardian_intro():
    """The second guardian blocks the middle of the bridge."""
    _scene_title("THE SECOND GUARDIAN")
    slow_print("You walk towards the middle of the bridge.", ASH)
    slow_print("Suddenly, the second stone guardian blocks your path.", BONE)


def show_second_riddle(repeat=False):
    """The water bottles riddle."""
    print()
    _speak(["The guardian says:"], ASH, repeat)
    print()
    _speak(["  'To cross this bridge, you must understand",
            "   what you carry.'"], BONE, repeat)
    print()
    _speak(["A traveller enters the island carrying five water bottles.",
            "He gives two away and finds three more.",
            "How many bottles does he now have?"], ASH, repeat)
    _show_options(["5", "6", "7", "8"])


def show_second_guardian_passed():
    """The player answered the second riddle."""
    print()
    slow_print("Correct. The guardian grants you permission to continue.", BONE)


def show_final_guardian_intro():
    """The iron gate at the end of the bridge."""
    _scene_title("THE FINAL GUARDIAN")
    slow_print("After passing the second guardian, you reach the exit of the bridge.", ASH)
    slow_print("An iron gate blocks your way.", BONE)
    slow_print("There is a keyhole in the middle, but no handle.", ASH)


def show_final_riddle(repeat=False):
    """The key riddle."""
    print()
    _speak(["An inscription reads:"], ASH, repeat)
    print()
    _speak(["  'I have teeth but cannot eat.",
            "   I have a head but cannot think.",
            "   I can open what others cannot.",
            "   What am I?'"], BONE, repeat)
    _show_options(["A key", "A sword", "A comb", "A hammer"])


def show_gate_unlocked():
    """The player answered correctly and has the key."""
    print()
    slow_print("Correct. You take out your key and unlock the gate.", BONE)
    slow_print("The final guardian steps aside.", ASH)


def show_no_key_for_gate():
    """The player solved the riddle but has no key."""
    print()
    slow_print("You have solved the riddle, but you do not have a key.", RUST)
    slow_print("You must return to the cave to find one.", ASH)


def show_wrong_answer(name, hp, guardian, can_retry):
    """A wrong answer to any guardian's riddle."""
    print()
    say("Wrong answer. You lose 1 HP.", RUST)
    show_status(name, hp)
    if can_retry:
        say(RETRY_LINES[guardian], ASH)


def show_invalid_answer():
    """Bad input on a riddle."""
    print()
    say("That is not an option. Choose a number from 1 to 4.", RUST)


# ---------- Ending the level ----------

def show_bridge_death(name, hp):
    """The player's HP ran out at the bridge."""
    print()
    slow_print("The wind and the cold take the last of your strength.", RUST)
    slow_print("You have run out of HP.", ASH)
    print()
    show_status(name, hp)


def show_bridge_completed(name, hp):
    """The player is across."""
    _scene_title("BRIDGE COMPLETED")
    slow_print("You have crossed the old bridge.", BONE)
    slow_print("In the distance, you can finally see the lighthouse.", ASH)
    print()
    show_status(name, hp)