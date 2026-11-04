"""Title screen and opening story for Stranded IO."""

from ui.theme import (
    ASH, BONE, RESET, RUST, WIDTH,
    grey, ground_line, pause, say, slow_print, tide_line,
)

# Each banner row is a little darker and more eroded than the one above it,
# so the title looks like it is sinking into fog.
FADE = [grey(255), grey(251), grey(247), grey(244), grey(241)]
ERODE = ["█", "█", "█", "▓", "▒"]

# Each glyph is 5 rows tall. Add more letters here if you change the title.
FONT = {
    "S": ["█████", "█    ", "█████", "    █", "█████"],
    "T": ["█████", "  █  ", "  █  ", "  █  ", "  █  "],
    "R": ["████ ", "█   █", "████ ", "█  █ ", "█   █"],
    "A": [" ███ ", "█   █", "█████", "█   █", "█   █"],
    "N": ["█   █", "██  █", "█ █ █", "█  ██", "█   █"],
    "D": ["████ ", "█   █", "█   █", "█   █", "████ "],
    "E": ["█████", "█    ", "████ ", "█    ", "█████"],
    "I": ["█████", "  █  ", "  █  ", "  █  ", "█████"],
    "O": [" ███ ", "█   █", "█   █", "█   █", " ███ "],
    " ": ["   ", "   ", "   ", "   ", "   "],
}


def render_banner(text):
    """Return the text as 5 rows of block letters that fade from top to bottom."""
    rows = ["", "", "", "", ""]
    for letter in text.upper():
        glyph = FONT.get(letter, FONT[" "])
        for row in range(5):
            shaded = glyph[row].replace("█", ERODE[row])
            rows[row] += FADE[row] + shaded + RESET + " "
    return "\n".join(rows)


def show_intro():
    """Show the title screen, story intro and basic instructions."""
    print()
    print(tide_line())
    print()
    print(render_banner("STRANDED IO"))
    print()
    print(tide_line())
    subtitle = "S U R V I V E   T H E   I S L A N D"
    print(f"{ASH}{subtitle:^{WIDTH}}{RESET}\n")

    story = [
        (ASH, "Salt. Smoke. The slow hiss of the tide."),
        (BONE, "You wake face-down in the sand."),
        (ASH, "Splintered hull. Torn canvas. Nobody else moving."),
        (BONE, "Your throat is cracked and dry. Your side is bleeding."),
        (ASH, "Far up the cliffs, something tall stands against the grey sky."),
        (BONE, "A lighthouse. Dark."),
        (RUST, "Nobody is coming for you. Not unless you reach it."),
    ]
    for color, line in story:
        slow_print(line, color)
        pause()

    print()
    slow_print("May God be with you.", ASH)
    print()
    say("Type the number of your choice and press Enter.", ASH)
    say("Every choice has a price. Watch your HP.", ASH)
    print()
    print(ground_line())
    print()
    say("You try to recall your name...")
    print()


if __name__ == "__main__":
    show_intro()