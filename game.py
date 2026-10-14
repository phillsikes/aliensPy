"""aliensPy - a text based adventure game inspired by the film ALIENS.

Run with:  python3 game.py
"""

import art
from scenes import SCENES


def show_scene(scene):
    """Print the scene's art (if any) and its text."""
    if "art" in scene:
        print(getattr(art, scene["art"]))
    print(scene["text"])


def get_next_scene(scene):
    """Ask the player for a choice and return the name of the next scene."""
    answer = input("> ").lower()
    choices = scene.get("choices", {})
    if answer in choices:
        return choices[answer]["next"]
    return scene["default"]


def play():
    """Run the game from the start scene until an ending is reached."""
    scene_name = "start"
    while True:
        scene = SCENES[scene_name]
        show_scene(scene)
        if scene.get("ending"):
            break
        scene_name = get_next_scene(scene)


if __name__ == "__main__":
    play()
