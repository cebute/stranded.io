"""Game over and victory screens."""

from ui.theme import ASH, BONE, RUST, WIDTH, RESET, ground_line, pause, say, slow_print, spaced, tide_line


def show_game_over(name):
    """Shown whenever the player dies."""
    print()
    print(tide_line())
    print(f"\n{RUST}{spaced('GAME OVER'):^{WIDTH}}{RESET}\n")
    print(tide_line())
    print()
    slow_print(f"{name} did not make it.", BONE)
    pause()
    slow_print("Your journey ends here.", ASH)
    slow_print("The island claims another soul.", ASH)
    print()
    print(ground_line())


def show_victory(name):
    """Shown when the beacon is lit."""
    print()
    print(tide_line())
    print(f"\n{BONE}{spaced('THE BEACON BURNS'):^{WIDTH}}{RESET}\n")
    print(tide_line())
    print()
    slow_print("The lamp catches. A pale beam sweeps across the water.", ASH)
    pause()
    slow_print("Far out, a boat turns toward the light.", BONE)
    pause()
    slow_print(f"{name} survived.", BONE)
    print()
    print(ground_line())