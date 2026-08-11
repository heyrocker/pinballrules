---
title: "Competition Install Master List"
---

# Competition Install Master List {#heading--top}
- [General & Manufacturer Overview](#heading--overview)
- [Stern Pinball Competition Settings](#heading--stern)
- [Bally & Classic Settings](#heading--classics)

This guide provides a quick-reference breakdown for Tournament Directors and competitive players on how **Competition Mode** and **Competition Install** alter game rules, mystery awards, and difficulty settings across various pinball machines.

---

## General & Manufacturer Overview {#heading--overview}

### Stern Pinball Overview
* **Warning:** Changing to tournament mode will affect **COINAGE** and **FREEPLAY** settings on older Stern games (pre-High Roller Casino, High Roller Casino before 3.0 ROM, Data East, and Sega games).
* **Spike 2 Games:** Spike 2 games with the newer service menu will detail the exact changes before performing the install.
* **Spike 3 Games:** Spike 3 games with the newer service menu will detail the exact changes before performing the install.


#### Setup Methods:
1. **Competition Mode (Standard Adjustments) or (quick menu new service menu):**
    * Sets `Competition Mode: YES`
    * Removes randomness from game features; Mystery awards follow a fixed order and reflexive settings lock to fixed values.
2. **Competition Install (Utilities Menu):**
    * Installs **Competition** (enables competition mode and alters adjustments) and **Novelty** (disables extra balls and specials).

### Bally Overview
* Setting Bally SS games to **NOVELTY** converts Extra Balls to **25,000 points** and Specials to **50,000 points**.
* Toggles carry-over settings for Bonus, Bonus X, and other game features depending on the specific title.

---

## Stern Pinball Competition Settings {#heading--stern}

| Game                             | Mode / Install Type | Key System Adjustments                                                                                                                                                                                                     | Fixed Awards & Gameplay Changes                                                                                                                                                                                                                                                                   | Extra Ball Replacement / Limit |
|:---------------------------------| :--- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :--- |
| **Avengers: Infinity Quest**     | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | Bingo awards are fixed (Center column/row are Super Ball Save & Light Portal Lock; all others are super modes). Mystery in fixed order.                                                                                                                                                           | Disabled. |
|                                  | **Competition Install** | Competition Mode: On
Start with lockdown button: Off
Tilt Debounce: 1000ms
Instant Info Auto Scroll: Off                                                                                                          | Insider Connected Computer Gem Mania Award: Off.                                                                                                                                                                                                                                                  | Disabled. |
| **Foo Fighters**                 | **Competition Mode** *(Pre-1.00)* | Standard adjustments applied.                                                                                                                                                                                              | Mystery given in fixed order: 2.5M, Engine van upgrade, Advance spinner, Speakers van upgrade, Max tractor beam, Bomb van upgrade, 5M, +1x Bonus X, Light ball save, Light extra ball.                                                                                                            | Award 10M points. |
|                                  | **Competition Install** *(V1.00+)* | Competition Mode: YES
Tilt Warnings: 2
Action Button Behavior: DISABLED
Timed Plunger / Flipper Launch: OFF                                                                                                       | Overlord difficulty: Medium (no target spotting inside)
Overlord lock: Empties at end of ball (2+ players)
Van mode timer: 40 seconds.                                                                                                                                                      | Extra Ball Limit: NO EXTRA BALLS. |
| **Game of Thrones**              | **Competition Install** | Lannister Buttons: EXTRA HARD (4/game)
Targaryen Freeze Time: HARD (10s)
Dire Wolf Frequency: HARD (2/game)                                                                                                          | Swords Unlock Multipliers: HARD
Ram Hits for Multipliers: HARD
Two Bank Difficulty: EXTRA HARD (always times out)
Ball Save Timers: Blackwater/Wall (6s), Hand (8s), Iron Throne/Winter (10s)
Left Drops Award Lord of Light: OFF.                                                    | Disabled. |
| **Ghostbusters**                 | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | Tobin Spirit Guide & Slot Pops in fixed order
Negative Reinforcement: 1 correct guess per 10 ghosts collected (next guess always incorrect).                                                                                                                                                   | Extra Ball Limit: No Extra Balls (Scoop never lights; no points awarded). |
|                                  | **Competition Install** | Competition Mode: Yes
Player Language Select: No
Game Restart: No
Lost Ball Recovery: No                                                                                                                          | *Recommended manual tweaks:* Set Midnight Madness to NO and Allow Scare Feature to NO.                                                                                                                                                                                                            | Extra Ball Limit: No Extra Balls. |
| **Godzilla (Stern)**             | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | Maser Mystery award in fixed order.                                                                                                                                                                                                                                                               | Award 50M points instead. |
|                                  | **Competition Install** | Competition mode: On
Tilt Debounce: 1000ms
Start with lockdown button: Off
Planet X Unlock Normal                                                                                                                 | Standard competition behavior active.                                                                                                                                                                                                                                                             | Extra Ball Limit: No Extra Balls. |
| **Guardians of the Galaxy**      | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | Removes all randomness.                                                                                                                                                                                                                                                                           | Award 15M points instead. |
|                                  | **Competition Install** | Free Play: Yes
Player Language Select: No
Game Restart: No
Allow Left + Start End: Never
Lost Ball Recovery: No                                                                                                | Groot M.B. Virtual Lock: Yes.                                                                                                                                                                                                                                                                     | Extra Ball Limit: No Extra Balls. |
| **Iron Maiden**                  | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | 1st drop target award: Advance Bonus X (instead of Light Orb)
Initial lit Eddie Battle fixed as Flight of Icarus.                                                                                                                                                                              | Disabled. |
|                                  | **Competition Install** | Competition Mode: On
Secret Skillshots: Off                                                                                                                                                                             | Fear of the Dark is initially lit mode
Madness Mode Enabled: Off (Can I Play With Madness disabled).                                                                                                                                                                                           | Disabled. |
| **JAWS**                         | **Competition Install** | COMPETITION MODE: YES
TILT_WARNINGS: 2
COIN DOOR DISABLE TILT: YES
ACTION BUTTON BEHAVIOR: DISABLED
START BUTTON BEHAVIOR: SINGLE CREDIT                                                                       | Game Restart: NO
Lost Ball Recovery: NO
Timed Plunger / Flipper Launch: OFF
Target Game Time: NO TARGET TIME                                                                                                                                                                             | EXTRA BALL LIMIT: NO EXTRA BALLS. |
| **JAMES BOND**                   | **Competition Install** | COMPETITION MODE: YES
TILT_WARNINGS: 2
COIN DOOR DISABLE TILT: YES
ACTION BUTTON BEHAVIOR: DISABLED
START BUTTON BEHAVIOR: SINGLE CREDIT                                                                       | Game Restart: NO
Lost Ball Recovery: NO
Timed Plunger / Flipper Launch: OFF
Target Game Time: NO TARGET TIME                                                                                                                                                                             | EXTRA BALL LIMIT: NO EXTRA BALLS. |
| **Jurassic Park (Stern)**        | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | Amber Frenzy modes in fixed order (Pops, Targets, Slings, Ramps).                                                                                                                                                                                                                                 | Disabled. |
|                                  | **Competition Install** | Competition Mode: On
Tilt Debounce: 1000ms
Start with lockdown button: Off                                                                                                                                           | Smart Missile can award Invalid Frenzy: Off
Goat Mania: Off.
MAP - ALLOW DINO ESCAPES No
                                                                                                                                                                                                | Disabled. |
| **Led Zeppelin**                 | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | If Extra Ball Records set to Auto, EB lights at 5 records.                                                                                                                                                                                                                                        | Disabled. |
|                                  | **Competition Install** | Competition mode: On
Start with lockdown button: Off                                                                                                                                                                    | Build Icarus During Multiball: No
Zeppelin MB lock difficulty: Medium (spell ROCK)
Lite Start Tour: requires +1 R ramp
Earn Sales from Active PF: No
Electric Magic: 3 completions of LED ZEP
Band Boosts: 0.                                                                      | Disabled. |
| **Rush**                         | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | Mystery awards in fixed order (Activate Instruments, 2.5M, Bonus X...)
Red Barchetta is initial Time Machine MB
Far Cry MB jackpots in fixed order.                                                                                                                                         | Disabled. |
|                                  | **Competition Install** | Standard adjustments applied.                                                                                                                                                                                              | Far Cry MB Difficulty: Medium (standups -> timed R ramp -> Side scoop lock)
Drops Stay Down on Full Set: No
Freewill add-a-ball set to 2 hits.                                                                                                                                              | Disabled. |
| **Star Wars (Stern)**            | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | Mystery awards in fixed order
Shot multiplier maxes at 10x (instead of 20x)
                                                                                                                                                                                                                | Disabled. |
|                                  | **Competition Install** | Competition mode: On                                                                                                                                                                                                       | Allow Missions to Stack: Off.
Tie Fighter Multiball starts at 50 Tie Fighters (instead of 35).
Multpliers Difficulty Hard
Hyperspace Mball Difficulty Hard                                                                                                                                                               | Disabled. |
| **Star Wars Fall Of The Empire** | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | Removes all randomness.                                                                                                                                                                                                                                                                           | Disabled. |
|                                  | **Competition Install** | Competition mode: On                                                                                                                                                                                                       | Show Scores More Frequently On
Jedi Save Diffculty Medium
Battle of Hoth Muitball Difficulty Increase Nedium
                                                                                                                                                                            | Disabled. |
| **The Beatles**                  | **Competition Install** | Player Language Select: No
Game Restart: No
Allow Left + Start End: Never
Default game mode: Competition                                                                                                          | Main/Tax Man/AML MB ball save: 15s
Record magnet: Multiball only
Level to complete song: 3                                                                                                                                                                                                  | Extra Ball Limit: No Extra Balls (200K points awarded).
Special: 400K points awarded if disabled. |
| **The Mandalorian**              | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | Multiball always enabled treated as No (must start/complete Hunter Mission or drain)
First shot starts Ambush
The Foundry excludes Question Mark award.                                                                                                                                     | Disabled. |
|                                  | **Competition Install** | Multiball Always Enabled: No
Start with lockdown button: Off
Default Game Mode: Competition
Player Game Mode: No                                                                                                  | Standard competition features forced.                                                                                                                                                                                                                                                             | Disabled. |
| **The Walking Dead**             | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | If 1st Walker EB set to Auto, lights at fixed kills.                                                                                                                                                                                                                                              | Award 2.5M points instead. |
|                                  | **Competition Install** | Competition Mode: On
Bicycle Girl Lit at Start: No
Shot Modes Light/Start MB: Start
Multi-Kill Sequencing: Left to Right
Multi-Kill Carryover Horde: Yes
Horde Lost Advances Ball: Yes                      | Only 1 drop target bank completion needed to light modes (modes cannot light during MB)
Multi-Kill value does NOT reset after Horde
Supplies/Combos/Cross-Bow/Bicycle Girl for Multi-Kill: Off
Prison/Well MB Super JP with Bomb: No
Draining/getting bit in Horde ends ball-in-play. | Extra Ball Limit: No Extra Balls. |
| **Venom**                        | **Competition Mode** | Standard adjustments applied.                                                                                                                                                                                              | Disables saved progress loading during Competition Mode.                                                                                                                                                                                                                                          | Disabled. |
|                                  | **Competition Install** | COMPETITION MODE: YES
TILT_WARNINGS: 2
ACTION BUTTON BEHAVIOR: DISABLED
START BUTTON BEHAVIOR: SINGLE CREDIT                                                                                                      | Coin Door Ball Saver: YES
Coin Door Disable Tilt: YES
Allow Left + Start End: Never
Timed Plunger / Flipper Launch: OFF                                                                                                                                                                  | EXTRA BALL LIMIT: NO EXTRA BALLS. |

---

## Bally & Classic Settings {#heading--classics}

| Game / Platform | Mode / Setting | Specific Adjustments | Gameplay & Scoring Changes |
| :--- | :--- | :--- | :--- |
| **Bally SS Games** | **Novelty Mode** | System Dipswitches / Menu | Extra Balls score 25,000 points; Specials score 50,000 points. Adjusts carry-over behavior for Bonus and Bonus X. |
| **Viking (Bally)** | **Custom / Switch Settings** | Switch #8 (Inline drops score 5 bonus advances) | Toggles carryover for EB, Special, outlane 25k lights, and drop target point values. Extra Balls score 25,000; Specials score 50,000. |