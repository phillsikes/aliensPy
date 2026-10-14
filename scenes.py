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
                 "A sealed security door leads deeper into the colony.\n"
                 "In the floor, a maintenance shaft drops into darkness. A foul smell drifts up."),
        "item_text": {
            "tracker": "Your motion tracker flickers with contacts somewhere down the shaft.",
        },
        "choices": {
            "logs": {"next": "colony_logs", "label": "Read the colony logs on the terminals"},
            "office": {"next": "admin_office", "label": "Search the administrator's office",
                       "unless": "keycard"},
            "door": {"next": "medlab", "label": "Open the security door",
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

    # --- Act 3: Medlab ---
    "medlab": {
        "text": ("Beyond the security door is the colony Medlab. Specimen tubes line the walls,\n"
                 "and pale, many-legged things float inside them.\n\n"
                 "A man in a spotless company jacket steps out from behind a lab bench.\n"
                 "\"Dalton Pryce, company liaison. Am I glad to see you.\n"
                 " There's a service lift in the sub-level lab that comes up right inside\n"
                 " the compound. Saves a lot of time. Just escort me on the way.\"\n\n"
                 "The only other way is the long quarantine corridor."),
        "item_text": {
            "tracker": "Your motion tracker twitches. Some of the things in those tubes are alive.",
        },
        "choices": {
            "trust": {"next": "pryce_shortcut", "label": "Take Pryce's shortcut",
                      "text": "\"Smart choice,\" Pryce says, a little too quickly."},
            "refuse": {"next": "quarantine", "label": "Refuse and take the long way",
                       "text": "Pryce shrugs. \"Your call. Your funeral.\""},
            "notes": {"next": "lab_notes", "label": "Read the lab notes"},
            "bench": {"next": "workbench", "label": "Search the workbench",
                      "unless": "welding torch"},
        },
    },
    "lab_notes": {
        "text": ("Notes scrawled on a clipboard:\n\n"
                 "  Specimens 1-4 ALIVE. Do NOT open the tubes.\n"
                 "  Pryce asked for the tube release codes again. Told him no.\n"
                 "  He keeps asking how long the creatures take to hatch inside a host.\n"
                 "  Why does he want to know that?"),
        "choices": {
            "back": {"next": "medlab", "label": "Put the clipboard down"},
        },
    },
    "workbench": {
        "text": ("Under a tarp on the workbench you find a welding torch with a full tank.\n"
                 "It could seal a door shut in a hurry."),
        "choices": {
            "back": {"next": "medlab", "label": "Head back to Pryce"},
        },
        "on_enter": {"time": -1, "item": "welding torch"},
    },
    "quarantine": {
        "text": ("You take the long way through the quarantine corridor.\n"
                 "Sealed doors, flickering lights, and nothing moving. It's slow, but it's quiet.\n"
                 "At the far end, a hatch opens into the terraforming compound."),
        "choices": {
            "hatch": {"next": "crossroads", "label": "Climb through the hatch"},
        },
        "on_enter": {"time": -2},
    },
    "pryce_shortcut": {
        "text": ("Pryce leads you down a stairwell to the sub-level lab.\n"
                 "More specimen tubes glow in the dark.\n"
                 "\"Lift's just through here,\" he says, and steps through a doorway ahead of you."),
        "choices": {
            "follow": {"next": "pryce_betrayal", "label": "Follow him"},
        },
        "on_enter": {"time": 0},
    },
    "pryce_betrayal": {
        "text": ("The door slams shut between you. Through the glass, Pryce taps at a wall panel.\n"
                 "\"Sorry, Marine. The company needs live specimens. Nothing personal.\"\n\n"
                 "With a hiss, the specimen tubes drain and swing open.\n"
                 "Something skitters across the floor toward you."),
        "choices": {
            "fight": {"next": "crossroads", "label": "Open fire with your pulse rifle",
                      "ammo": 20,
                      "text": ("You blast the creatures as they leap, then shoot out the door lock.\n"
                               "You ride the service lift up into the compound. Pryce is gone.")},
            "burn": {"next": "crossroads", "label": "Flood the floor with fire",
                     "requires": "flamethrower",
                     "text": ("The creatures shriek and curl up in the flames.\n"
                              "You kick the door open and ride the service lift up into the compound.")},
            "seal": {"next": "crossroads", "label": "Weld yourself into a supply closet",
                     "requires": "welding torch",
                     "text": ("You dive into a supply closet and weld the door shut behind you.\n"
                              "Claws scrape the metal. You crawl out through a vent into the compound.")},
            "beg": {"next": "death_betrayal", "label": "Pound on the glass and beg Pryce"},
        },
        "on_enter": {"time": 0},
    },

    # --- The compound ---
    "crossroads": {
        "text": ("You step into the terraforming compound, which way do you go?\n"
                 "A supply room door hangs open beside you."),
        "choices": {
            "left": {"next": "egg_room", "label": "Go left",
                     "text": ("Good choice. The lifeform signal is getting stronger.\n"
                              "The reactor alarm rises to a shriek. From here on, "
                              "time runs out twice as fast.")},
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

    # --- Act 4: The Hive (every scene here costs 2 time) ---
    "egg_room": {
        "text": ("The corridor opens into a chamber coated in black resin, ribbed like the\n"
                 "inside of some huge animal. Leathery eggs cover the floor in rows.\n"
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
        "on_enter": {"time": -2},
    },
    "three_doors": {
        "text": ("You stand before 3 colored doors: red, yellow, and blue.\n"
                 "Newt must be behind one of these doors. Which one will you choose?"),
        "choices": {
            "red": {"next": "red_door", "label": "Open the red door"},
            "yellow": {"next": "newt_shelter", "label": "Open the yellow door"},
            "blue": {"next": "death_blue_door", "label": "Open the blue door"},
            "listen": {"next": "listen_at_doors", "label": "Stop and listen at the doors"},
        },
        "on_enter": {"time": -2},
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
        "on_enter": {"time": -2},
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
        "on_enter": {"time": -2},
    },
    "newt_shelter": {
        "text": ("Behind the yellow door is an emergency shelter, torn apart.\n"
                 "Cots are overturned. Small, dusty handprints lead to a loose vent grate,\n"
                 "and from inside the vent comes the sound of someone trying not to breathe."),
        "item_text": {
            "tracker": "Your motion tracker shows one small contact, very still, just inside the vent.",
        },
        "choices": {
            "call": {"next": "newt_found", "label": "Kneel down and call out softly"},
            "grab": {"next": "newt_ducts", "label": "Reach into the vent and grab her",
                     "text": ("A small hand bites down hard on yours, and the figure scrambles\n"
                              "away deeper into the ducts. You crawl in after her.")},
        },
        "on_enter": {"time": -2},
    },
    "newt_ducts": {
        "text": ("You crawl through the cramped, dark ducts, following the sound\n"
                 "of small knees on metal. Precious time slips away.\n"
                 "At last you corner her in a dead-end junction."),
        "choices": {
            "talk": {"next": "newt_found", "label": "Talk to her gently"},
        },
        "on_enter": {"time": -2},
    },
    "newt_found": {
        "text": ("A small, filthy face peers out at you. It's Newt.\n"
                 "She stares at your armor, then at your face, for a long moment.\n"
                 "\"You came,\" she whispers. \"Everyone else is gone.\""),
        "choices": {
            # Acts 5 (The Queen) and 6 (Escape) will go here.
            "go": {"next": "escape_newt", "label": "Take her hand and get out of here",
                   "text": "Newt grips your hand tight. Together you head for the dropship."},
        },
        "on_enter": {"time": -2},
    },

    # --- Endings ---
    "escape_newt": {
        "text": ("You've found Newt!!! Congratulations!!!\n"
                 "You both escape aboard the Marine Dropship and fly safely back to Earth...\n"
                 "or do you."),
        "ending": True,
    },
    "death_betrayal": {
        "text": ("Pryce watches through the glass as the creatures close in.\n"
                 "The company gets its specimen.\n" + GAME_OVER),
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
