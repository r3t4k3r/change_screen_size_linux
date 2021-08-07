#! /usr/bin/env python3
import subprocess

SCREEN_SIZE = ("1440", "900") # ширина, высота // width, height
SCREEN_NAME = "DVI-1" # смотри xrandr // look xrandr
FREQUENCY = "60" # частота // frequency

cvt_output = subprocess.check_output(["cvt", SCREEN_SIZE[0], SCREEN_SIZE[1], FREQUENCY]).decode()
newmode = cvt_output.split("Modeline ")[1][:-1]
newmode_name = newmode.split("\"")[1].split("\"")[0]
subprocess.call(f"xrandr --newmode {newmode}", shell=True)
subprocess.call(f"xrandr --addmode {SCREEN_NAME} {newmode_name}", shell=True)
# comment under line if u want only add screen size without change.
subprocess.call(f"xrandr --output {SCREEN_NAME} --mode {newmode_name}", shell=True)
