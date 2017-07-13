# About

Super Mario Bros. practice ROM for advanced players.

## Features
	* Detailed performance metrics; frame rule, frame and frames left on frame-rule.
	* Select what level and frame rule to start on.
	* Select number of power-ups collected.
	* Predefined frame-rule for each level.
	* Press select to restart level from Frame Rule you entered.
	* Shows relative x-position (for wrong warp practice).
	* Press select while paused to reset.
	* Infinite lives.
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
	* Press Select while NOT paused to restart level at entered Frame Rule.
	* Press Select while paused to return to Title Screen.

## Display
From left to right, the top status bar displays are,

	* Current frame-rule.
	* Current frame number.
	* Number of frames left on frame-rule when beating area.
	* Relative X position.
	* Standard game timer.

The frame values are not updated continuously, as it was pretty hard to make any sense of it. Instead, they are updated at certain checkpoints. All values are updated when you exit an area, by a pipe, a vine or by completing the level.

In addition, the current frame and frame-rule are also updated as you land from a jump and when you would normally get score.

# Get it!

## From the build-server!

Build server allows you to easily create a custom version of the Practice ROM with pre-defined frame-rules for each level. You can either enter them manually or create from a Wsplit file (to convert to Wsplit from other formats, you can use https://splits.io).

Build-server at: http://83.253.236.75:5555

## Using IPS

	1. Download Lunar IPS (http://fusoya.eludevisibility.org/lips/download/lips102.zip).
	2. Get the latest IPS patch from from the ips directory in this repo.
	3. Using Lunar IPS, patch your original SMB (US/JP) ROM with the .ips.


## Building from scratch

	1. Clone this repo.
	2. Clone pellsson/badassm into the smbpractice directory.
	3. Put the original SMB (US/JP) as "smb-org.nes" in the smbpractice directory.
	4. Run build.sh

