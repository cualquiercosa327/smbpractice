# About

Super Mario Bros. practice ROM for advanced players.

## Features
	* Detailed performance metrics; frame rule, frame and frames left on frame-rule.
	* Shows relative x-position (for wrong warp practice).
	* Select what level and frame rule to start on.
	* Select number of power-ups collected.
	* Predefined "perfect-frame-rule" for each level.
	* Infinite lives.
	* Instant reset button.
	* Play as Luigi :) Poor guy never gets to play.

## Controls
### Title screen
	* Use Select to move up and down in the menu.
	* Use Left and Right change world/level/p-ups.
	* To change what frame rule to start from, use Left and Right to select digit, and Up and Down to change it.
	* Press B to set starting Rule to 0 (Will use current game rule if 0).
	* Press Start as normal to start the game.
	* Press Up when Rule is not selected to change to Luigi.
### In-game
	* Press Select to get back to title screen.
	* Press Start to pause and see current frame-metrics.

## Display
From left to right, the top status bar displays are,

	* Current frame-rule.
	* Current frame number.
	* Number of frames left on frame-rule when beating area.
	* Relative X position.
	* Standard game timer.

The frame values are not updated continuously, as it was pretty hard to make any sense of it. Instead, they are updated at certain checkpoints. All values are updated when you exit an area, by a pipe, a vine or by completing the level.

In addition, the current frame and frame-rule are also updated when you would normally get score.

# Build Instructions

	1. Clone this repo.
	2. Clone pellsson/badassm into the same directory.
	3. Put the original SMB (US/JP) as "smb-org.nes" in the smbpractice directory.
	4. Run build.sh

