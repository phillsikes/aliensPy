"""aliensPy - a text based adventure game inspired by the film ALIENS.

Run with:  python3 game.py
Add --no-color if your terminal shows odd symbols instead of colors.
"""

import os
import random

import art
from scenes import SCENES
from utils import clear_screen, color, dramatic_dots, pause, typewriter, wait_for_enter

STARTING_TIME = 34
STARTING_AMMO = 30
LOW_TIME = 5  # The TIME in the status bar turns red at or below this.

# Escaping LV-426 creates this file, which unlocks the prologue for good.
SAVE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aliensPy_save.txt")

# Said now and then when the player types something that isn't a choice.
CONFUSED_LINES = [
    "Static crackles over your headset. Say again?",
    "Stay frosty, Marine. That's not one of your options.",
    "Your squad stares at you. Nobody knows what that means.",
    "That's not a plan, that's a panic attack.",
]

# Random sounds from the motion tracker, if the player has one.
TRACKER_PINGS = [
    "ping...",
    "ping... ping-ping...",
    "ping-ping-ping-ping",
]


def is_prologue_unlocked():
    """Return True if the player has escaped LV-426 before."""
    return os.path.exists(SAVE_FILE)


def unlock_prologue():
    """Create the save file that unlocks the prologue."""
    try:
        with open(SAVE_FILE, "w") as save:
            save.write("prologue_unlocked\n")
    except OSError:
        pass  # Can't save here (e.g. a read-only folder). The game still works.


def new_state():
    """Return the player's state at the start of a game."""
    # "flags" remember story events (like "queen_hunting"). Unlike items,
    # they aren't shown in the status bar.
    flags = []
    if is_prologue_unlocked():
        flags.append("prologue_unlocked")
    return {"time": STARTING_TIME, "ammo": STARTING_AMMO, "items": [], "flags": flags}


def show_status(state):
    """Print a one-line status bar, e.g. TIME: 9 | AMMO: 30 | ITEMS: tracker"""
    items = ", ".join(state["items"]) or "none"
    time_text = f"TIME: {state['time']}"
    if state["time"] <= LOW_TIME:
        time_text = color(time_text, "red")
    print(f"{time_text} | AMMO: {state['ammo']} | ITEMS: {items}")
    print("-" * 60)


def tracker_ping(state):
    """Sometimes print a motion tracker ping to build tension."""
    if "tracker" in state["items"] and random.random() < 0.5:
        print(color("[tracker] " + random.choice(TRACKER_PINGS), "green"))
        print()


def apply_effects(effects, state, default_time=0):
    """Apply effects like {"time": -1, "ammo": 30, "item": "keycard"} to the state."""
    state["time"] += effects.get("time", default_time)
    state["ammo"] += effects.get("ammo", 0)
    item = effects.get("item")
    if item and item not in state["items"]:
        state["items"].append(item)
    flag = effects.get("flag")
    if flag and flag not in state["flags"]:
        state["flags"].append(flag)


def lock_reason(choice, state):
    """Return why a choice is locked (e.g. "needs 20 ammo"), or None if it's open."""
    if "requires" in choice and choice["requires"] not in state["items"]:
        return "needs " + choice["requires"]
    if state["ammo"] < choice.get("ammo", 0):
        return f"needs {choice['ammo']} ammo"
    return None


def show_choices(choices, state):
    """Print the choices the player can see. Return the names they can pick."""
    open_choices = []
    print()
    for name, choice in choices.items():
        if choice.get("unless") in state["items"]:
            continue  # Hidden: the player already has this item.
        if "only_if" in choice and choice["only_if"] not in state["flags"]:
            continue  # Hidden: the flag it needs isn't set (e.g. prologue not unlocked).
        line = f"  {name:<8} - {choice['label']}"
        reason = lock_reason(choice, state)
        if reason:
            line += f"  [LOCKED: {reason}]"
        else:
            open_choices.append(name)
        print(line)
    return open_choices


def show_scene(scene, state):
    """Clear the screen, then print the status bar, art, scene text, and any banner."""
    clear_screen()
    if not scene.get("hide_status"):
        show_status(state)
        tracker_ping(state)
    ending = scene.get("ending")
    if "art" in scene:
        art_text = getattr(art, scene["art"])
        if ending == "death":
            art_text = color(art_text, "red")
        print(art_text)
    if ending:
        pause(1.0)

    if scene.get("style") == "computer":
        typewriter(scene["text"], "green")
    elif ending == "death":
        print(color(scene["text"], "red"))
    else:
        print(scene["text"])
    for item, text in scene.get("item_text", {}).items():
        if item in state["items"]:
            print(text)

    # Ending screens finish with a big banner.
    if ending == "death":
        pause(0.5)
        print(color(art.GAME_OVER, "red"))
    elif ending == "win":
        pause(0.5)
        print(color(art.VICTORY, "green"))


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
    state = new_state()
    scene_name = "start"
    while True:
        scene = SCENES[scene_name]
        if not scene.get("ending"):
            # Most scenes cost 1 unit of time.
            apply_effects(scene.get("on_enter", {}), state, default_time=-1)
            if state["time"] <= 0:
                state["time"] = 0
                scene_name = "death_reactor"
                continue
        show_scene(scene, state)
        if scene.get("ending"):
            if scene.get("unlocks_prologue") and not is_prologue_unlocked():
                unlock_prologue()
                print(color('*** PROLOGUE UNLOCKED! Type "prologue" on the title screen '
                            'to play it. ***', "green"))
            return scene_name
        open_choices = show_choices(scene["choices"], state)
        answer = ask(open_choices)
        choice = scene["choices"][answer]
        state["ammo"] -= choice.get("ammo", 0)
        apply_effects(choice.get("on_choose", {}), state)
        dramatic_dots()
        if "text" in choice:
            # Keep the result on screen until the player has read it.
            print(choice["text"])
            wait_for_enter()
        scene_name = choice["next"]
        # A choice can lead somewhere else if a flag is set.
        for flag, other_scene in choice.get("next_if", {}).items():
            if flag in state["flags"]:
                scene_name = other_scene


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
