# About

Super Mario Bros. practice ROM for advanced players.

# Update v1.7 - 2017-01-07

- **Fix bug** causing **state to become arbitrary** after entering a pipe (the Hammer Bro bug).

- Changed **restart level** to **Select + Up**

- Changed **restart game** to **Select + Down**

- Visually restore rule-counter @ restart level (Judge & Timer control are restored too, but not visually).

# Update v1.6 - 2017-12-30

## Judge-Radar

Upon beating a level, the rightmost column in the statusbar, "J", will show you what judge-frame you are on (for good/bad judges on 8-1). Only essential if you go to 8-1 from pipe.

## Sockfolder FPG compatible timer

Shows the timer control value in the same manner as Sockfolder FPG ROM under "x" in the statusbar. This is the value 0-K shown as level in Sockfolder FPG.

## Update frame & rule nr on jump

Previously frame and rule values were only updated when you land, now updated on jump too.

## Align statusbar with original SMB

Aligned "RM" and "TIME" to match "WORLD" and "TIME" in original SMB, so that visual queues are not destroyed.

# Update v1.5 - 2017-12-29

I hope you people had a jolly Christmas; also happy new year! <3

* No bugs! Resuming on a frame-rule in any mode should work, regardless of level! Please let me know if you find any resume-issues.
* Save-state re-enabled (completely untested). Select+B to re-load level @ entered frame-rule.
* Select+A to return to title-screen.
* Buildserver running on _ATROCIOUSLY slow_ rPI. Takes like 15 sec to build (and thus download) a tailored ROMs.

# Features
* **Detailed performance metrics**; frame rule, timer value, frame and frames left on frame-rule.
* Choose what **level and frame rule** to **start on**.
* **Predefined frame-rule** for each level.
* **Judge-radar** which shows what "Judge-frame" you entered the level at (for 8-1).
* **Quick return** to main-level for **level select**, no need to get up and reset console.
* Shows relative **x-position** (for wrong warp practice).
* Choose **nr of power-ups** collected.
* **Restart level** from Frame Rule you entered.
* Infinite lives.
* Play as **Luigi** :) Poor guy never gets to play.

# Controls
## Title screen
* Use **Select** to move up and down in the menu.
* Use **Left** and **Right** change world/level/p-ups.
* To change what frame rule to start from, use **Left** and **Right** to select position, and **Up** and **Down** to change it.
* Press **B** to set starting Rule to 0 (Will use current game rule if 0).
* Press **Start** as normal to start the game.
* Press **Up** when Rule is not selected to change to Luigi.

## In-game
* Press **Select + Up** to restart level at entered Frame Rule.
* Press **Select + Down** to return to Title Screen.

# Display
From left to right, the top status bar displays are,

* Current frame-rule.
* Rule-timer at level entry (same as world letter in Sockfolder FPG).
* Current frame nr.
* Number of frames left on frame-rule when beating area.
* Relative X position.
* Standard game timer.
* Judge-radar. Shows you the current "Judge-frame" (for 8-1).

The frame values are not updated continuously, as it was pretty hard to make any sense of it. Instead, they are updated at certain checkpoints. All values are updated when you exit an area, by a pipe, a vine or by completing the level.

In addition, the current frame and frame-rule are also updated as you land from a jump and when you would normally get score.

# Get it!

## From the build-server!

Build server allows you to easily create a custom version of the Practice ROM with pre-defined frame-rules for each level. Just paste your WSplit file and download your custom-built ROM image.

Build-server at: http://83.253.236.75:5555

*To convert to Wsplit from other formats, you can use https://splits.io*

## Using IPS

1. Download Lunar IPS (http://fusoya.eludevisibility.org/lips/download/lips102.zip).
2. Get the latest IPS patch from from the ips directory in this repo.
3. Using Lunar IPS, patch your original SMB (US/JP) ROM with the .ips.


## Building from scratch

1. Clone pellsson/smbpractice (github)
2. Clone pellsson/badassm into the smbpractice directory (githib)
3. Put the original SMB (US/JP) as "smb-org.nes" in the smbpractice directory.
4. Run build.sh


**TY WOP0 WOP0** <3