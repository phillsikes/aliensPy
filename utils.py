"""Small helpers for screen output."""

import os
import time


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
