"""Small helpers for screen output."""

import os


def clear_screen():
    """Clear the terminal on Windows, macOS, and Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')
