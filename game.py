"""aliensPy - a text based adventure game inspired by the film ALIENS.

Run with:  python3 game.py
"""

import random

import art
from scenes import SCENES
from utils import clear_screen, dramatic_dots, pause

# Said now and then when the player types something that isn't a choice.
CONFUSED_LINES = [
    "Static crackles over your headset. Say again?",
    "Stay frosty, Marine. That's not one of your options.",
    "Your squad stares at you. Nobody knows what that means.",
    "That's not a plan, that's a panic attack.",
]


def show_scene(scene):
    """Clear the screen, then print the scene's art (if any) and its text."""
    clear_screen()
    if "art" in scene:
        print(getattr(art, scene["art"]))
    if scene.get("ending"):
        pause(1.0)
    print(scene["text"])


def ask(choice_names):
    """Keep asking until the player types one of choice_names, then return it."""
    while True:
        answer = input("> ").strip().lower()
        if answer in choice_names:
            return answer
        if random.random() < 0.5:
            print(random.choice(CONFUSED_LINES))
        print("Please type one of: " + ", ".join(choice_names))


def play():
    """Run one game from the start scene. Return the name of the ending reached."""
    scene_name = "start"
    while True:
        scene = SCENES[scene_name]
        show_scene(scene)
        if scene.get("ending"):
            return scene_name
        choices = scene["choices"]
        answer = ask(list(choices))
        dramatic_dots()
        scene_name = choices[answer]["next"]


def main():
    """Play games until the player decides to stop."""
    try:
        while True:
            ending = play()
            if ending == "quit":
                break
            print()
            print('Play again? Type "Y" for yes or "N" for no:')
            if ask(["y", "n"]) == "n":
                print("Thanks for playing aliensPy. Stay frosty.")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nComms lost. Thanks for playing aliensPy.")


if __name__ == "__main__":
    main()
