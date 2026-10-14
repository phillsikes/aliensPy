"""Small helpers for screen output."""

import os
import sys
import time

# Colors are turned off if the player runs `python3 game.py --no-color`,
# sets the NO_COLOR environment variable, or the output isn't a terminal.
COLORS_ON = (sys.stdout.isatty()
             and "NO_COLOR" not in os.environ
             and "--no-color" not in sys.argv)

if COLORS_ON and os.name == 'nt':
    os.system('')  # Turns on color support in Windows terminals.

COLOR_CODES = {
    "green": "\033[32m",  # computer and terminal text
    "red": "\033[31m",    # danger
}
RESET = "\033[0m"


def color(text, name):
    """Return text wrapped in a color, or unchanged if colors are off."""
    if not COLORS_ON:
        return text
    return COLOR_CODES[name] + text + RESET


def typewriter(text, color_name=None, delay=0.01):
    """Print text one character at a time, like a computer terminal."""
    if COLORS_ON and color_name:
        print(COLOR_CODES[color_name], end="")
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    if COLORS_ON and color_name:
        print(RESET, end="")
    print()


def clear_screen():
    """Clear the terminal on Windows, macOS, and Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(seconds=1.0):
    """Wait a moment for dramatic effect."""
    time.sleep(seconds)


def dramatic_dots(count=3, delay=0.4):
    """Print dots one at a time, like something is about to happen."""
    for _ in range(count):
        print(".", end="", flush=True)
        time.sleep(delay)
    print()
