"""Shared look for Stranded IO: colours, lines, typing effect and helpers.

Every other file in ui/ imports from here, so changing a colour or a line
style in this one file changes the whole game.
"""

import os
import time

if os.name == "nt":
    os.system("")  # switches on ANSI colors in the Windows terminal

# Skip the typing effect and pauses while testing:
#   Linux/macOS:  STRANDED_FAST=1 python main.py
#   Windows (PowerShell):  $env:STRANDED_FAST=1; python main.py
FAST = os.environ.get("STRANDED_FAST") == "1"

RESET = "\033[0m"
WIDTH = 63


def grey(level):
    """Return a grey text color. 232 is nearly black, 255 is nearly white."""
    return f"\033[38;5;{level}m"


BONE = grey(252)   # main text
ASH = grey(245)    # quieter text
SOOT = grey(238)   # scenery lines
RUST = "\033[38;5;124m"  # dried blood: the only real color in the game


def tide_line(width=WIDTH):
    """Return a faint line of waves."""
    return SOOT + ("~ " * width)[:width] + RESET


def ground_line(width=WIDTH):
    """Return a faint straight line."""
    return SOOT + "─" * width + RESET


def pause(seconds=0.7):
    """Wait a moment, unless FAST is on."""
    if not FAST:
        time.sleep(seconds)


def say(text="", color=BONE):
    """Print a line instantly in the given color."""
    print(f"{color}{text}{RESET}")


def slow_print(text, color=BONE, delay=0.03):
    """Print one character at a time for a typewriter feel."""
    if FAST:
        delay = 0
    print(color, end="")
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print(RESET)


def spaced(text):
    """Turn 'THE BEACH' into 'T H E   B E A C H'."""
    return " ".join(text.upper())


def level_header(title, subtitle=""):
    """Standard opening for every level, so the player always knows where they are."""
    print()
    print(tide_line())
    print(f"{BONE}{spaced(title):^{WIDTH}}{RESET}")
    if subtitle:
        print(f"{ASH}{subtitle:^{WIDTH}}{RESET}")
    print(ground_line())
    print()


def hp_line(hp, max_hp=40):
    """Return an HP bar. Grey normally, rust when HP is low."""
    filled = max(0, min(10, round(hp / max_hp * 10)))
    bar = "█" * filled + "░" * (10 - filled)
    color = RUST if hp <= 15 else ASH
    return f"{color}HP {bar} {max(hp, 0)}{RESET}"


def show_status(name, hp):
    """Print the player's name and HP on one line."""
    print(f"{ASH}{name}{RESET}   {hp_line(hp)}")


def ask(prompt):
    """Ask for input with a styled prompt and return the stripped answer."""
    return input(f"{BONE}{prompt}{RESET} ").strip()


def ask_choice(prompt, valid):
    """Keep asking until the answer is one of the valid choices."""
    options = [str(choice) for choice in valid]
    while True:
        answer = ask(prompt)
        if answer in options:
            return answer
        say(f"That is not an option. Choose {', '.join(options)}.", RUST)