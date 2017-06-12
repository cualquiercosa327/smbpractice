# About

Super Mario Bros. practice ROM for advanced players.

## Features
	* Detailed performance metrics; frame rule, frame and frames left on frame-rule.
	* Select what level and frame rule to start on.
	* Predefined "perfect-frame-rule" selection for each level.
	* Infinite lives.

## Controls
### Title screen
	* Use Select to move up and down in the menu.
	* Use Left and Right change world/level.
	* To change what frame rule to start from, use Left and Right to select digit, and Up and Down to change it.
	* Press Start as normal to start the game.
	* Hold B while pressing start to play as Luigi :) Poor fellow never gets to play.
### In-game
	* Press Select to get back to title screen.

## Display
From left to right, the top status bar displays:
	* Current frame-rule.
	* Lowest 2 digits of current frame number.
	* Number of frames left on frame-rule when beating area.
	* Standard game timer.

The values are not updated continuously, as it was pretty hard to make any sense of it. Instead, they are updated at certain checkpoints. All values are updated when you exit an area, by a pipe, a vine or by completing the level.

In addition, the current frame and frame-rule are also updated when you would normally get score.

# Build Instructions

	1. Extract the character ROM from an existing SMB ROM, name it smb.chr
	2. Clone this repo.
	3. Clone pellsson/badassm into the same directory.
	3. Run build.sh
