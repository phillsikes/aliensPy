"""Story content for aliensPy.

Each scene is a dictionary entry with:
    "art"         - optional name of an ASCII art constant in art.py
    "text"        - what the player reads
    "item_text"   - optional extra text shown only if the player has an item,
                    e.g. {"tracker": "The tracker pings..."}
    "choices"     - maps what the player types to a choice (see below)
    "on_enter"    - optional effects when the scene starts:
                    "time" (default -1), "ammo", "item" (an item to pick up)
    "hide_status" - True to hide the status bar (title screen, quitting)
    "ending"      - True if this scene ends the game

Each choice has:
    "next"      - the scene to go to
    "label"     - a short description shown in the list of choices
    "text"      - optional text shown right after the player picks it
    "requires"  - optional item needed; without it the choice is [LOCKED]
    "ammo"      - optional ammo cost; without enough ammo the choice is [LOCKED]
    "unless"    - optional item that hides this choice once the player has it
    "on_choose" - optional effects when picked, same as "on_enter"
                  (but time defaults to 0)
"""

GAME_OVER = "Game Over Man, GAME OVER!"

SCENES = {
    "start": {
        "art": "TITLE",
        "text": ("Welcome back to LV-426.\n"
                 "Your mission is to find Newt\n"
                 "and make it off the planet alive.\n"
                 "Would you like to play?"),
        "choices": {
            "y": {"next": "landing", "label": "Yes", "text": "Let's begin!"},
            "n": {"next": "quit", "label": "No"},
        },
        "on_enter": {"time": 0},
        "hide_status": True,
    },

    # --- Act 1: Landing ---
    "landing": {
        "text": ("The dropship punches through the storm and slams down on LV-426.\n"
                 "Rain hammers the hull. Through the viewport the colony is dark.\n"
                 "No lights. No answer on any channel.\n\n"
                 "The sergeant kicks open the weapons locker.\n"
                 "\"One extra piece of gear each, Marine. Make it count.\""),
        "choices": {
            "tracker": {"next": "colony_gate", "label": "Motion tracker",
                        "on_choose": {"item": "tracker"},
                        "text": "You clip the motion tracker to your belt and head down the ramp."},
            "flamer": {"next": "colony_gate", "label": "Flamethrower",
                       "on_choose": {"item": "flamethrower"},
                       "text": ("You heft the flamethrower. Its pilot light hisses blue "
                                "as you head down the ramp.")},
            "ammo": {"next": "colony_gate", "label": "Extra pulse rifle ammo (+30)",
                     "on_choose": {"ammo": 30},
                     "text": "You stuff your pockets with magazines and head down the ramp."},
        },
        "on_enter": {"time": 0},
    },
    "colony_gate": {
        "text": ("You cross the rain-lashed landing pad to the colony's main entrance.\n"
                 "Inside, a recorded voice echoes through the empty halls:\n\n"
                 "    \"Warning. Reactor cooling failure. Evacuate the colony.\"\n\n"
                 "The countdown has started. Watch your TIME."),
        "choices": {
            "enter": {"next": "ops_center", "label": "Go inside"},
        },
        "on_enter": {"time": 0},
    },

    # --- Act 2: Operations Center ---
    "ops_center": {
        "text": ("The Operations Center is deserted. Emergency lights flicker over\n"
                 "overturned chairs and cold coffee cups. Terminals glow along one wall.\n"
                 "A sealed security door leads into the terraforming compound.\n"
                 "In the floor, a maintenance shaft drops into darkness. A foul smell drifts up."),
        "item_text": {
            "tracker": "Your motion tracker flickers with contacts somewhere down the shaft.",
        },
        "choices": {
            "logs": {"next": "colony_logs", "label": "Read the colony logs on the terminals"},
            "office": {"next": "admin_office", "label": "Search the administrator's office",
                       "unless": "keycard"},
            "door": {"next": "crossroads", "label": "Open the security door",
                     "requires": "keycard",
                     "text": "You swipe the keycard. The security door grinds open."},
            "shaft": {"next": "death_shaft", "label": "Climb down the maintenance shaft"},
        },
    },
    "colony_logs": {
        "text": ("You wipe the dust off a terminal and scroll through the last entries:\n\n"
                 "  SECURITY 04/12: Lost contact with the survey team. Medical has one survivor.\n"
                 "  SECURITY 04/19: Creatures in the lower levels. Moved the kids to the\n"
                 "                  shelter behind the YELLOW door.\n"
                 "  ADMIN NOTE:     Security door only opens with my keycard. It's in my office.\n"
                 "  LAST ENTRY:     Something is moving in the ceiling. We can hear it above us"),
        "choices": {
            "back": {"next": "ops_center", "label": "Step away from the terminal"},
        },
    },
    "admin_office": {
        "text": ("The administrator's office is wrecked. Under the desk lamp you spot the keycard,\n"
                 "and crouched on the desk above it, a Xenomorph turns its eyeless head toward you."),
        "choices": {
            "fight": {"next": "ops_center", "label": "Open fire with your pulse rifle",
                      "ammo": 20, "on_choose": {"item": "keycard"},
                      "text": ("You open fire. The creature screeches and crashes out through the window.\n"
                               "You grab the keycard and hurry back to Operations.")},
            "burn": {"next": "ops_center", "label": "Torch it with the flamethrower",
                     "requires": "flamethrower", "on_choose": {"item": "keycard"},
                     "text": ("A roar of flame fills the office and the creature flees, shrieking.\n"
                              "You snatch the keycard, still warm, and head back to Operations.")},
            "back": {"next": "ops_center", "label": "Back away slowly",
                     "text": "You ease out of the office. It doesn't follow... yet."},
        },
    },

    # --- The compound (from alienPy) ---
    "crossroads": {
        "text": ("You step into the terraforming compound, which way do you go?\n"
                 "A supply room door hangs open beside you."),
        "choices": {
            "left": {"next": "egg_room", "label": "Go left",
                     "text": "Good choice. The lifeform signal is getting stronger."},
            "right": {"next": "death_xenomorphs", "label": "Go right"},
            "search": {"next": "supply_room", "label": "Search the supply room",
                       "unless": "tracker"},
        },
    },
    "supply_room": {
        "text": ("You pry open a dented supply locker.\n"
                 "Inside is a working motion tracker. It hums to life in your hands."),
        "choices": {
            "back": {"next": "crossroads", "label": "Head back to the corridor"},
        },
        "on_enter": {"time": -1, "item": "tracker"},
    },
    "egg_room": {
        "text": ("You've come to a room full of alien eggs. "
                 "The signal is coming from the other side."),
        "choices": {
            "walk": {"next": "death_facehugger_eggs",
                     "label": "Walk through the room quietly"},
            "lift": {"next": "three_doors", "label": "Ride the lift across",
                     "text": ("Good idea, the eggs stir, but nothing emerges as you ride the lift.\n"
                              "You reach the other side safely.")},
            "burn": {"next": "three_doors", "label": "Burn a path with the flamethrower",
                     "requires": "flamethrower",
                     "text": ("You sweep the flamethrower across the eggs. They pop and hiss\n"
                              "as you cross the room. You reach the other side safely.")},
        },
    },
    "three_doors": {
        "text": ("You stand before 3 colored doors: red, yellow, and blue.\n"
                 "Newt must be behind one of these doors. Which one will you choose?"),
        "choices": {
            "red": {"next": "red_door", "label": "Open the red door"},
            "yellow": {"next": "escape_newt", "label": "Open the yellow door"},
            "blue": {"next": "death_blue_door", "label": "Open the blue door"},
            "listen": {"next": "listen_at_doors", "label": "Stop and listen at the doors"},
        },
    },
    "listen_at_doors": {
        "text": ("You hold your breath and listen.\n"
                 "Steam hisses from broken pipes. Somewhere far below, the reactor groans."),
        "item_text": {
            "tracker": "Your motion tracker picks up a small, still signal behind the yellow door.",
        },
        "choices": {
            "back": {"next": "three_doors", "label": "Step back from the doors"},
        },
    },
    "red_door": {
        "text": "You open the red door. A massive Xenomorph uncoils from the shadows!",
        "choices": {
            "fight": {"next": "three_doors", "label": "Open fire with your pulse rifle",
                      "ammo": 20,
                      "text": ("Your pulse rifle roars. The creature shrieks and flees into the vents.\n"
                               "The room beyond is a dead end. You back out to the doors.")},
            "run": {"next": "death_red_door", "label": "Run for it"},
        },
    },

    # --- Endings ---
    "escape_newt": {
        "text": ("You've found Newt!!! Congratulations!!!\n"
                 "You both escape aboard the Marine Dropship and fly safely back to Earth...\n"
                 "or do you."),
        "ending": True,
    },
    "death_shaft": {
        "text": ("You drop into the maintenance shaft. In the dark, the walls begin to move.\n"
                 "They were waiting for you.\n" + GAME_OVER),
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
    # The game sends the player here when the reactor countdown reaches 0.
    "death_reactor": {
        "text": "Sorry, you've run out of time and the colony self destructs\n" + GAME_OVER,
        "ending": True,
    },
    "quit": {
        "text": ("Well that's great, that's just great, man. "
                 "Now what are we supposed to do?"),
        "ending": True,
        "hide_status": True,
    },
}
