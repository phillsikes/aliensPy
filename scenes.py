"""Story content for aliensPy.

Each scene is a dictionary entry with:
    "art"     - optional name of an ASCII art constant in art.py
    "text"    - what the player reads
    "choices" - maps what the player types to the next scene
    "ending"  - True if this scene ends the game
"""

GAME_OVER = "Game Over Man, GAME OVER!"

SCENES = {
    "start": {
        "art": "TITLE",
        "text": ("Welcome back to LV-426.\n"
                 "Your mission is to find Newt\n"
                 "and make it off the planet alive.\n"
                 'Would you like to play?\n     Type "Y" for yes or "N" for no:'),
        "choices": {
            "y": {"next": "crossroads"},
            "n": {"next": "quit"},
        },
    },
    "crossroads": {
        "text": ("Let's begin!\n"
                 "You enter the terraforming compound, which way do you go?\n"
                 '     Type "Left" or "Right"'),
        "choices": {
            "left": {"next": "egg_room"},
            "right": {"next": "death_xenomorphs"},
        },
    },
    "egg_room": {
        "text": ("Good choice. The lifeform signal is getting stronger.\n"
                 "You've come to a room full of alien eggs. "
                 "The signal is coming from the other side.\n"
                 '     Type "Walk" to walk through the room quietly. '
                 'Or type "Lift" to ride the lift across.'),
        "choices": {
            "walk": {"next": "death_facehugger_eggs"},
            "lift": {"next": "three_doors"},
        },
    },
    "three_doors": {
        "text": ("Good idea, the eggs stir, but nothing emerges as you ride the lift.\n"
                 "You've reached the other side safely and come to 3 colored doors.\n"
                 "Newt must be behind one of these doors. Which one will you choose?\n"
                 '     Type "Red" "Yellow" or "Blue"'),
        "choices": {
            "red": {"next": "death_red_door"},
            "yellow": {"next": "escape_newt"},
            "blue": {"next": "death_blue_door"},
        },
    },

    # --- Endings ---
    "escape_newt": {
        "text": ("You've found Newt!!! Congratulations!!!\n"
                 "You both escape aboard the Marine Dropship and fly safely back to Earth...\n"
                 "or do you."),
        "ending": True,
    },
    "death_xenomorphs": {
        "text": ("Oh No!! You walked right into a group of hungry Xenomorphs!!!\n     "
                 + GAME_OVER),
        "ending": True,
    },
    "death_facehugger_eggs": {
        "text": "Ouch!! You've been attacked by a facehugger!!!\n     " + GAME_OVER,
        "ending": True,
    },
    "death_red_door": {
        "text": "Sorry, you've been attacked by a massive Xenomorph!\n" + GAME_OVER,
        "ending": True,
    },
    "death_blue_door": {
        "text": ("Sorry, you've been attacked by a facehugger and die as an Alien Queen is born\n"
                 + GAME_OVER),
        "ending": True,
    },
    # Not reachable right now. The reactor countdown (Phase 3) will lead here.
    "death_reactor": {
        "text": "Sorry, you've run out of time and the colony self destructs\n" + GAME_OVER,
        "ending": True,
    },
    "quit": {
        "text": ("Well that's great, that's just great, man. "
                 "Now what are we supposed to do?"),
        "ending": True,
    },
}
