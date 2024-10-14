#!/bin/bash

# Directory containing wallpapers
WALLPAPER_DIR="$HOME/Pictures/wallpapers"

# Select a random wallpaper and set it
DISPLAY=:0 feh --randomize --bg-fill "$WALLPAPER_DIR/"
