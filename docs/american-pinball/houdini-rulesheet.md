---
title: "Houdini Rulesheet"
manufacturer: "American Pinball"
opdb_id: "GvBQX"
---

# Houdini

**Houdini Rules**
Current Version: 18.12.12

Playfield Design, Mechanics: Joe Balcer
Engineering: Jim Thornton
Rules, Programming, Animation: Josh Kugler
Artwork, Animations: Jeff Busch
Music, Sound: Matt Kern
Sculptures: Matt Riesterer (Back Alley)
Animation: Ish Raneses

Rules edited and compiled from the following sources: American Pinball, This Week in Pinball, Josh Kugler, Straight Down The Middle: a pinball show YouTube channel, konjurer, et al.

Original Wiki Rulesheet hosted on [Tilt Forums](/american-pinball/houdini-rulesheet_GvBQX)

Conventions:
`Monotype` is used for feature adjustment values. Unless specified, these are defaults.

***

**THE GOAL**

The goal of Houdini is to become a Master Magician, which is the final wizard mode. This is done by spelling H-O-U-D-I-N-I; each of the 7 letters correspond to 7 major areas of the game: Stage modes, Movie modes, the Magic Shop, Jail Escape hurry-ups, Secret Mission combos, Trunk Multiball, and Seance Multiball.

Each of these areas is represented by a different color, and progress in each can be seen in the status dashboard by holding both flippers or collecting a Houdini letter. The movies, escapes, and missions are also tracked by the chain link inserts near the flippers.

Getting to the Master Magician Mode can be made less difficult in the settings (see "Suggested Home Settings" for more information).

**OVERVIEW**

_Skill Shot_
3 random rotating awards

_10 Stage Modes_
* Vanishing Elephant
* Chinese Water Torture
* Indian Needle Trick
* Walk through Walls
* Handcuff King
* Milkcan Escape
* Metamorphosis
* Bullet Catch (multiball using the upper catapult)
* Straight Jacket Escape (Multiball with reverse/inverted flippers)
* King of Cards (video mode)

_Mini Wizard Modes_
* Movie Binge - complete all 5 Movie Modes
* Great Jail Escape - complete all 5 Jail Escape Hurry-Up Modes
* Ultimate Secret Mission - complete all Secret Mission Combos

_Master Magician Wizard Mode_
You must collect all the Houdini letters:
* Complete `10` Stage Modes
* Complete `5` Movie Modes
* Collect `8` items from the Magic Shop
* Complete `5` Jail Escape Hurry-Up Modes
* Complete `5` Secret Mission Combos
* Collect `3` jackpots during Trunk Multiball
* Collect `2` jackpots during Seance Multiball

_Outlane Modes_
There are 2 modes that are set up at the outlanes that can revive your ball.
* Return from Beyond
* Escape Death

***

**SKILL SHOT**

**Regular:** Plunge to hit one of three roving ESC targets, each with an award. Possible awards include:
* Points (values increase with each skill shot made)
* Light Outlane Mode (only one is lit; alternates with flippers)
* Escape Letter
* Film Letter
* Seance Letter
* Hold Multiplier
* Magician's Choice
* Milkcan Multiplier (immediately starts 2X Milkcan Multiplier scoring)
* 5X Multiplier
* Open Magic Shop
* Open Movie
* Award Lock

**Super:** Soft plunge to the left Magic target to collect all 3 listed awards.

**STAGE MODES**

Color Code: Red

Flipping the respective flippers scrolls left and right through the 10 Stage illusions, and a progress map, shown on the API Theater marquee. They are _not_ awarded randomly. The currently displayed illusion (the progress map represents magician's choice) is locked-in upon opening the stage curtain in one of three ways:

* Bash the stage curtain `4` times.
* Bash the stage curtain through a clean Stage Alley shot, not hitting a single bumper.
* Shoot the Key Lane and hit the back red Key Target without hitting a single bumper.

When the curtain is open, shooting the Stage starts the mode. Shooting the Stage Alley through to the Stage without hitting a bumper begins the stage mode at 2X value; the top-right corner of the display will read "2X Stage Scoring" in red.

If the stage is locked-in to magician's choice, you get to select which illusion to start from those not yet played. In addition to opening the stage curtain on the progress map, magician's choice is available as an award from the skill shot and magic shop. These awards will override the selected illusion when the stage curtain is already open. Magician's choice is an important tactical advantage, as availability of multiball, active playfield or mode scoring multipliers, and other conditions can be considered.

Basic stage modes run on a `45` second timer. At 10 seconds, the orbits will light to "add time".

Once per Stage mode (with the exception of _King of Cards_, _Bullet Catch_, and _Indian Needle Trick_), the Magic standup targets turn red. Hitting one of them awards a free mode shot. See "Magic Targets" for more information.

Film modes cannot be started during Stage modes.

_Vanishing Elephant_ — 3 ramp shots move elephant into the crate, then stage to show crate empty.
* Ramp 3 times
* Stage

_Chinese Water Torture_ — Key Lane to lower into tank, either orbit to close curtain, stage to open curtain and set Houdini free. There is now recognition for the fastest escape from the tank!
* Key Lane
* Either Orbit
* Stage

_Indian Needle Trick_ — All switches score X, Magic and Key standup targets increase switch value. Houdini pulls needles out of his mouth as shots are made.
* All switches
* Magic/Key targets to increase switch value

_Walk through Walls_ — To move Houdini through the wall, shoot one of the right shots, then one of the center shots, then one of the left shots.
* Right Shot (Inner Loop, Right Orbit, or Scoop)
* Middle Shot (Stage, or Ramp)
* Left Shot (Left Orbit, Stage Alley, or Key Lane)

_Handcuff King_ — Shoot the pops and every `3` hits results in a handcuff or chain being thrown out. Shed all `6` handcuffs to free Houdini. There is now recognition for the fastest escape from the cuffs!
* Hit `3` pops to shed a handcuff
* Shed `6` handcuffs

_Milkcan Escape_ — Shoot the lower left loop 3 times to lower him into the milkcan, roll out the screen, and then show him free. This can be the most lucrative of the stage modes.
* Milkcan Loop 3 times

_Metamorphosis_ — Shoot trunk to lower Houdini into the trunk, then orbit to close curtain, then stage or trunk to open curtain to reveal Houdini free, and Bess then in the trunk.
* Trunk
* Orbit
* Stage or Trunk

_King of Cards_ — A video mode where you are throwing cards (known as scaling) through moving hoops. The longer you hold the flipper in before throwing, the higher it will go, so you need to time it both for when you start and release your press. As you make shots, the hoops move faster. Making 3 of the smaller hoop will then light the smaller hoop for extra ball. It is possible to make both hoops with a single throw, which will double their value.

The mode starts with `5` cards to throw from each hand and will time out after `45` seconds.

_Straight Jacket Multiball_ — An instant 3 ball multiball, with jackpots at the Orbits, Stage Alley, Key Lane, and Ramp. The last shot made is worth a super jackpot, after which all jackpots are relit.

At the start, you get to choose how the mode plays with your flippers (holding the left or right).

"Reversed Flippers": The left flipper button controls the right flipper, and vice versa. It's Springfield Mystery Spot (_The Simpsons Pinball Party_) all over again. Jackpots are at normal value.

Hint: Cross your arms while flipping. Your brain will work as intended and you should be fine.

"Reversed and Inverted Flippers": Same as above, except that the flippers stay in the "up" position until you press a flipper button, at which point they drop. Jackpots are 3X.

Hint: Good to practice. This can be very valuable.

Beware: the game will _penalize_ you for hitting both flippers at the same time. You get warned for "chimping";
 and a cymbal-clashing monkey appears on the display. Keep double flipping and the jackpot value decreases.

_Bullet Catch_ — A 2 ball multiball, in three phases.
* Shoot the Inner Loop to load the gun (ball lock). This is on the basic stage mode timer.
* Shoot the roving hurry-up shot to fire, locking in the location and value. It starts at the Milkcan Loop and rotates right. A drain here ends the mode, but play continues with the release of the locked ball.
* The locked ball is released for a 2 ball multiball. Shoot extra jackpots at the stopped rover and Inner Loop.

Note the rover is a one-switch shot. Importantly, this means "Orbits" count from either direction.

Play all 10 Stage modes, and you'll get:

_Encore Bonus_

The crowd chants Houdini's name, and the Stage opens if it was not already. Shoot the Stage to earn a bonus consisting of:

* The total points earned from all Stage modes.
* An extra 10% bonus for each mode completed.

Encore Bonus can only be doubled by the 2X Stage Alley shot; Milkcan Multipliers won't count. At any rate, when collected the Stage Modes reset, and you can play them all again.


**MAGIC TARGETS**

The Magic Standup Targets help you in different ways depending on the current state of the game.  Hitting a magic target can add escape letters, séance letters, or film letters.  Hitting a target can also advance you a step during a Stage Mode or Movie Mode.  The magic targets also engage the magnets.

**MOVIE MODES**

Color Code: Blue

There are 5 modes based on Houdini’s movies. These modes are presented in black and white with an old film look and have a piano accompaniment. Failing to complete results in the film "burning". One is a type of add-a-ball multiball. Complete all 5 for a Houdini letter. Completing all 5 will also start the Mini-Magician Mode called Movie Binge.  You don’t have to complete each movie mode, but how well you did at each mode will impact your scoring potential in Movie Binge. By default the order is `random`, but the listed order is used when set to `fixed`.

Basic movie modes run on a `45` second timer. At 10 seconds, the orbits will light to "add time".

_Haldane of the Secret Service_ (`60` spins on the spinner) — Escape the waterwheel. Each shot makes it spin faster until it breaks free.

_Grim Game_ (Orbit, ramp, orbit) — Move Houdini from plane to plane to rescue the woman.

_Man From Beyond_ — This is an add-a-ball kind of mode. First bash the stage to free Houdini from the Ice (where he was frozen for 100 years), which will then put a second ball in play. Next, shoot orbits X times to free him from his restraints in the insane asylum, where another ball is put into play and the lights turn off except for three shots and a moving ‘spotlight’ running through inserts. Only one of the three lit shots will pay off. You can figure out which by sneaking a peek at the display and spotting Houdini when the spotlight is on him. Shooting the correct shot scores a jackpot, and then Houdini will randomly move between the three shots.

_Terror Island_ (Scoop, ramp, scoop, ramp) — Free the woman from the safe that was thrown in the ocean, then go back for the treasure.

_Master of Mystery_ (Left orbit, right orbit, left orbit, right orbit) — Featuring Q The Automaton, the first ever movie robot. Stop him from getting the woman or getting to the weapon. You only have X seconds to complete the next shot in the sequence, and making it resets the clock (but less time that previous shot).

Note: For most of the stage and movie modes, you can also hit one of the two Magic Standup Targets, which are located on either side of the lower playfield to advance a step through the mode. When not in a mode, these targets will assist you in other ways, based on current state, typically adding ESCAPE, SEANCE or FILM letters. They will also trigger the magnets under the hands which will then twirl and throw the ball. There is an optional ball saver (controlled via settings), when the magnets are triggered via the targets (and when not in seance mulitball).

**JAIL ESCAPE HURRY-UPS**

Color Code: Green

Spell E-S-C-A-P-E via stand-up targets and shoot the Jail hole to begin a Jail Escape Hurry Up. Complete `5` escapes to earn a Houdini letter, and cue the Great Jail Escape mini-wizard mode.

E-S-C stand-up targets are shootable but the A-P-E letters are not.  Use the pop bumpers and indirect shots to hit the A-P-E stand-ups. Light the Escape Death outlane mode by completing '2' escapes, and light extra ball by completing `3`.  By default, jails are selected in a `random` order. The listed order is used when order is set to `easiest to hardest`.

The 5 jails are:
* Paris - Trunk for 50,000
* London - Key Lane for 40,000
* New York - Ramp for 40,000
* Sydney - Spinner for 50,000
* Chicago - Milkcan Loop for 75,000

Rule designer Josh Kugler stated that "random is default since always seeing same one first would annoy most owners. However, random just means how it is set at the beginning, so if you get New York first and don't make it, you will see the other four before it gives you NY again."

Kugler went on to say that "the **_easy_** difficulty setting, means you only need the 'first part' of a shot versus the complete shot (normal/hard)."

A beginner set the Escape modes to easy to be a little more forgiving.  "The Milkcan shot, you only need to hit the magic target or near it - you don't have to make the loop."  On easy mode you can just sneak it up the ramp and it doesn't have to make it all the way around.  With the Key Target - you just need to hit key lane.  Inner loop?  Just first switch and you don't have to make it around the bend.  On easy you can hit the spinner from either direction and not just the right orbit.

Complete all hurry-ups, then complete ESCAPE again and land a ball in the Jail hole to start...

_The Great Jail Escape_

All 5 hurry-ups restart. The hurry-up value is the total points earned in all previous hurry-ups; each scores the hurry-up value. Complete all 5 shots to end the mode successfully. If the hurry-up value runs out, the mode ends.

[more information needed]

**SECRET MISSION COMBOS**

Color Code: Pink

Houdini was rumored to be a spy for the US government - hence the secret missions! Each secret mission is a combo. There are 5 different missions, and each combo gets progressively harder to complete. The secret missions are considered to be the hardest objective in the game to complete.

Secret Missions start at the scoop. Only one secret mission is active at a time. Complete it and you can then start the next. The next shot in the sequence is identified with a flashing purple arrow. If the sequence is broken, it will go back to the first shot of the sequence. Complete `3` missions to light extra ball and `5` missions for a Houdini letter. Completing all the missions lights the scoop for a mini-wizard mode.

* Combo Mission 1:  Ramp, then Scoop for 50,000
* Combo Mission 2:  Right Orbit, then Scoop for 75,000
* Combo Mission 3:  Ramp, Right Orbit, then Scoop for 125,000
* Combo Mission 4:  Ramp, Right Orbit, then Inner Loop for 175,000
* Combo Mission 5:  Milkcan Loop, Ramp, Right Orbit, then Scoop for 250,000

**OUTLANE MODES**

Complete the task to continue your ball; fail and the ball ends.

_Return From Beyond_
You get 30 flips to spell SEANCE (via mini stand-up targets). Earned by scoring `2` jackpots during Seance Multiball.

_Escape Death_
You get 30 seconds to spell ESCAPE (via stand-up targets). Escape Death is the harder of the two. Earned by completing `2` Jail Escape hurry-ups.

You can also light the outlane drain modes at the Magic Shop. If earned there it will bounce from side to side with each flip. If earned via Seance or Escapes, it will not move. If you have earned one plus magic shop version, then both outlines are lit. You can only earn each once per game.

**MAGIC SHOP “MYSTERY AWARD”**

Color Code: Yellow

Spinning the spinner enough times lights the Magic Shop at the Jail hole for a mystery award. By default the order is `random`, but the listed order is used when set to `fixed`.

_Magic Shop Awards:_
* Increase Bonus Multiplier
* Advance Milkcan Multiplier
* 20 Seconds of Ball Save
* Magical Points (varies from 5,000 to 10,000)
* Hold Bonus Multiplier
* Award Trunk Lock
* Light Extra Ball
* Light Return from Beyond or Escape Death (only one is lit; alternates with flippers)

Collecting `8` items from the Magic Shop yields a HOUDINI letter toward the Master Magician Mode.

Keep an eye out for the Easter Egg hat pulls, which poke fun at some of American Pinball's friends and competitors.

**STACKING**

Stage and Film modes can run during multiballs, but only one can be started and neither Stage nor Film modes can be stacked with each other. A mode must be started _before_ multiball to stack it. In single ball play, Jail Escape hurry-ups, Secret Missions, and the Magic Shop can be qualified and played, but not during multiball.

The best stack is Trunk and Seance Multiball and a third multiball--either _Straight Jacket Escape_ or _Bullet Catch_ Stage modes, or _The Man From Beyond_ Film mode. Milkcan Multipliers can be started at any time.

**MULTIBALLS**

_Trunk Multiball_

Color Code: Turquoise

By default the lock is lit at the start of the game. Stage Alley shot will light the lock on subsequent locks. Shoot the right inner loop to catapult a ball into the trunk for each locked ball. Lock 3 balls in the trunk to start the Trunk Multiball. 3 shots are lit for jackpots; complete those then shoot trunk (via inner loop) to score super jackpot and re-light jackpots. Collect `3` jackpots to earn a Houdini letter.

_Seance Multiball_ - 3 ball

Color Code: Teal

Spell S-E-A-N-C-E to light at the scoop. The magnets will engage in this multiball.  Spell seance to score jackpots, and spell in order for super jackpot (very hard). Gets harder to light each time. Collect `2` jackpots to earn a Houdini letter.


**MILKCAN PLAYFIELD MULTIPLIERS**

Color: Orange

The Milkcan loop (lower left loop) is a difficult shot that feeds the left inlane. Shooting the milkman loop immediately followed by the ramp will increase the playfield multiplier for X seconds. Each time this 2 shot combo is hit advances the multiple from 2X to 3X to 4X. Starting a mode via Stage Alley with a max milkcan multiplier gives 8X scoring.

**SUGGESTED HOME SETTINGS**
If you would like a more approachable game for the family and for new to intermediate players try these settings. This configuration allows the player to open the stage by bashing the stage curtain just one time. You also get more time to complete a mode before the mode times out and the crowd "boos" at you. When the jail escape order is from "easy to hard", it forces you to complete the cities in order.

* Stage Difficulty: Easy
* Stage Mode Timer: 45 to 60 seconds
* King of Cards: 40 to 60 seconds
* Jail Escapes Order: Easy to Hard
* Jail Escapes Difficulty: Easy

**TIPS**
You may elect to start each stage mode by shooting through the Stage Alley lane. A well-placed shot will start the stage mode at 2X.

***

**VERSION RELEASE NOTES**

Bug fixes and updates not listed - _only new features._ Check out https://www.american-pinball.com/support/updates/ for release notes and download links.

_18.12.12_
New — adjustment for right lock if it is having trouble releasing the ball to the scoop or if two balls
are being released. The double release can occur if the machine is set very steep. This adjustment
can also be used if you find that sometimes the ball does not feed to the scoop from the subway
every time. If you need guidance on adjusting this, contact support.
New — high score will automatically exit after 30 seconds of no activity

_18.8.1_
New — added an additional main audio track (now 4 different tracks), existing tracks have been improved
New — sound effect on increase jackpot
New — sound effect at start of game
New — sound effect on shooter lane
New — Flipper escape on Magic Shop, currently only available on visits 1,2,5,8
New — voice calls for NY cop for Great Escape opening
New — “progress ribbon” on ‘last scores screen’ that shows what you did on each of the major objective areas.
New — points per second — shown on the last scores screen, shows who is the most strategic/efficient.
New — Most Efficient Player Recognition — requires a game of at least 2 minutes to qualify
New — Support for Custom Message — to use, put a png formatted file, named custom_message.png with width of
1360 and height of 768 on a USB key and insert into the USB extension cable as if were doing a log dump or code
update. Following directions on screen, after reboot, go to settings -> Standard to enable it.
New — Mini-Magician mode for Secret Missions
New — Master Magician Mode — a little rough still, will get cleaned up in next release
New — Reset High Scores — Go to Settings -> Utilities -> Reset Scores
New — adjust ball save time on Trunk Multiball
New — adjustment for ball save time on Seance
New — 10 second ball save on Return from Beyond
New — 10 second ball save on Escape Death
New — consecutive ramp and loop scoring now have a 1 time 500K payout on the 7 consecutive shot, normally the
7th shot will go back to the start of the ladder.
New — Added support for mechanical knocker — kit availability soon
New — support for Euros on the pricing/credits display

New — support for Pounds on the pricing/credits display
New — support for Kroner on the pricing/credits display
New — setting to control how much the shaker is used. Setting it to ‘Low’ will remove shaker in the pops, setting it
to ‘Heavy’ will enable it for catapult build up.
New — Ball save in Man from Beyond when balls 2 and 3 are put into play
New — Voice calls for magicians choice
New — Voice calls for Movies — new voice is a more of a movie preview voice, and is the default, you can switch
back to the female voice in settings or choose random, which will use both, but each ball will be just one voice.
New — Voice calls for some of the newer joke hat pulls
New — Voice calls for straitjacket
New — Voice calls for Bullet Catch
New — Insert coin animation in attract mode (show if no credits)
New — Press start animation in attract mode (show if credits or in free play)
New — ball save at start of Movie Binge
New — Stage Mode Status screen now shows Green for a mode completed and red for a mode started by failed
New — Bonus for completing all stage modes, total points earned on the modes, plus the average score multiplied
by the number of modes completed. (Straitjacket: three jackpots to “complete”, Needles: 75 needles, Bullet: 1
jackpot, cardking: 4 hoops).
New — cop Easter egg
New — Presets — under service -> Settings -> Presets,
* You can now load a set of settings change to make the game extra easy, extra hard, etc
* Can also save your current settings and then re-load them later (e.g. hosting an event, need to change
some things, easy to now go back to what you had)
* Can also restore factory settings from preset menu
* As a reminder factory restores, presets and code updates do not impact pricing setup, stage calibration
or coil strength.

_18.5.4_
New — pops will now pause timers, except the milkcan multiplier. It will also not pause if the
current stage mode is handcuff escape or needle trick or if a multiball is active

_18.4.27_
New — Fastest Escapes recognition (inspired by TNA/Scott Danesi)
• Handcuff Escape
• Water Torture Escape


_18.4.11_
New — skill shot — each target has an an award, so hitting the flashing shot when on that target gives that award. Shooting super skill awards all three items.
New — Players Choice — allows the player to choose which stage act to perform. Available when the ‘status’ screen is on the marquee. That screen can be locked in via skill shot award or magic shop award.
New — match sequence. **Temp music
New — added a display counter for spins needed during Haldane movie mode
New — 4 additional ‘bad' hat pull items
New — animations for increasing of trunk multiball jackpot
New — Setting to adjust timer for Movie modes from 30 to 60 seconds (45 second is default)
New — Setting to adjust timer for Stage modes that use a timer, except king of cards which has its
own setting. Adjustable from 30 to 60 seconds, 45 is default
New — Settings for match sequence (credit or off) — Off will not show sequence
New — Settings for match sequence (percentage) — percentage of 0 will show match sequence but never award a credit
New — settings for Knocker (‘Audio High Volume’, ‘Audio Low Volume’ or ‘Off’)
New — lightshow for super skill shot
New — lightshow for magic targets
New — Score banner animated when going from shown to hidden and vice versa
New — coil adjustments for left ball lock to shorten or lengthen the time the plunger is held down. If two balls are being released reduce the time if the ball is getting hit and bouncing up when releasing increase the time. If you find you are needing to increase the time more than a small amount it is possible its s mechanical issues that needs to be addressed.
New — Setting to enable an autofire of the shooter lane if the ball has been sitting idle for 60
seconds. Defaults to Off
New — sound effect when ball traveling the wire form return from upper catapult
New — Extra ball when reaching a certain level of bonus multiplier. Controllable via settings
between 5 and 9 or Off, defaults to 7