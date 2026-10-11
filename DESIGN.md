# aliensPy — Design Document

## Overview
aliensPy is a text-based adventure game inspired by the film ALIENS. It is the successor to
alienPy, a bootcamp exercise (`alien.py`). aliensPy expands the story, adds simple mechanics, and
restructures the code so new content can be added without deep nesting.

**Guiding principle: keep it simple.** This is a hobby project and should stay readable to a
beginner Python developer.

## Constraints
- Python 3.10+, **standard library only** (no pip installs).
- Must run in a normal terminal on Windows, macOS, and Linux.
- Code should be beginner-readable: clear names, short functions, comments where helpful.
  Avoid classes-heavy architecture, metaprogramming, or frameworks.
- The game must be fully playable at the end of every phase.
- Keep `README.md` updated (roadmap checkboxes, run instructions) and rename the project to
  aliensPy throughout it.
- Write original story text. Short nods to the films are fine, but don't reproduce film dialogue at length.

## File Structure
```
aliensPy/
├── game.py        # Entry point: game loop, input handling, mechanics
├── scenes.py      # Story content: a dictionary of scenes
├── art.py         # ASCII art assets as string constants
├── utils.py       # Screen clearing, typewriter text, colors, pauses
├── alien.py       # Original alienPy game, kept for reference (do not delete)
└── README.md
```

## Core Engine: Scene-Based Design
Replace nested `if` statements with a data-driven scene dictionary. Each scene looks roughly like:

```python
"egg_room": {
    "art": "EGG",                      # optional key into art.py
    "text": "A chamber full of leathery eggs...",
    "choices": {
        "walk": {"next": "death_facehugger"},
        "lift": {"next": "three_doors"},
        "burn": {"next": "three_doors", "requires": "flamethrower"},
    },
    "on_enter": {"time": -1},          # optional effects
}
```

The game loop:
1. Clear the screen, show the scene's art and text.
2. Show only the choices the player can currently take (hide or lock ones whose
   `requires` item is missing; optionally show locked ones as "[LOCKED]").
3. Read input, normalize it (`.strip().lower()`), and re-prompt on invalid input.
4. Apply effects (items gained, ammo/time changes), then move to the next scene.
5. Scenes with `"ending": True` end the run and show the matching ending screen.

## Mechanics
| Mechanic | Description |
|---|---|
| Input validation | Invalid input re-prompts instead of killing the player. Occasional flavor text for gibberish. |
| Inventory | Simple list of item names. Items unlock choices. |
| Ammo | Integer counter for the pulse rifle. Fighting costs ammo; at 0, fight choices are unavailable. |
| Reactor countdown | Integer "time remaining." Most scenes cost 1. At 0, the colony detonates (bad ending). Shown in a status bar. |
| Motion tracker | If the player has the tracker, show random proximity pings ("ping... ping-ping") to build tension, using `random`. |
| Play again | After any ending, offer to restart. |

### Items
- **Motion tracker** — enables tracker pings and reveals a hint at the three doors.
- **Flamethrower** — allows burning a path through the egg room.
- **Keycard** — opens locked doors in Operations/Medlab.
- **Welding torch** — seal a door to escape a pursuit.
- **Colony logs** (found, not carried) — give story and hints about Newt's location.

## Story Outline (Acts)
Each act is a few scenes. Build them one at a time.

1. **Landing** — Dropship touches down on LV-426. Choose a loadout (tracker, flamethrower, or
   extra ammo). This choice shapes the run.
2. **Operations Center** — Deserted colony. Terminals with colony logs hint where Newt is.
   Find the keycard.
3. **Medlab** — Specimen tubes. A company representative suggests a risky plan. Choice to trust
   or refuse affects a later betrayal scene.
4. **The Hive** — Expanded version of the existing egg room and three doors. Newt is found
   here. The reactor countdown speeds up.
5. **The Queen** — Final confrontation with 2–3 strategies (fight, sneak, burn the eggs and run).
6. **Escape** — Race to the dropship before detonation.

Optional later: **Prologue chapter** set aboard a commercial towing ship answering a distress
signal, unlocked after finishing the main game.

### Endings
- **Good ending** — Escape with Newt.
- **Solo ending** — Escape without Newt.
- **Bad endings** — Various deaths (each with a short, distinct message; keep "Game over, man!" flavor).
- **Secret ending** — Escape with Newt, but a twist hints something stowed away aboard the dropship
  (payoff for alienPy's "...or do you" line).

## Presentation
- Clear screen between scenes: `os.system('cls' if os.name == 'nt' else 'clear')`.
- Typewriter effect for ship computer and log text (print characters with a short delay).
  Allow skipping or keep the delay small so it doesn't get tedious.
- Short `time.sleep()` pauses at dramatic beats.
- ANSI colors: green for computer/terminal text, red for danger. Include a way to disable colors
  if the terminal doesn't support them.
- A one-line status bar: `TIME: 12 | AMMO: 40 | ITEMS: tracker, keycard`.

### ASCII Art Assets (art.py)
Keep the existing title art. Add small original pieces (5–15 lines each):
- Motion tracker display
- Dropship
- Alien egg
- Facehugger
- Reactor / warning sign
- "GAME OVER" banner
- Victory screen

## Fixes Carried Over from alienPy
- Typos: "Welcome to back to", "terrafroming", "ecape", "Which once will you choose".
- `"you\ve"` is an invalid escape sequence; use `"you've"`.
- Rename the leftover variable `swim`.

## Build Phases
1. **Refactor** — Create the scene engine and port alienPy's existing content into `scenes.py`
   with identical story and outcomes. Move the title art into `art.py`. Apply the alienPy fixes.
2. **Polish** — Input validation, screen clearing, pauses, play-again loop.
3. **Mechanics** — Inventory, ammo, reactor countdown, status bar, tracker pings.
4. **Story** — Add acts one at a time, starting with Landing and Operations Center.
5. **Art & presentation** — New ASCII art, colors, typewriter text, endings screens.

After each phase: run the game end to end, check every ending is reachable, and update the
README roadmap.
