#! /usr/bin/env python3
import subprocess

screen_size = ("1440", "900") # ширина, высота
screen_name = "DVI-1" # смотри xrandr
frequency = "60" # частота

cvt_output = subprocess.check_output(["cvt", screen_size[0], screen_size[1], frequency]).decode()
newmode = cvt_output.split("Modeline ")[1][:-1]
newmode_name = newmode.split("\"")[1].split("\"")[0]
subprocess.call(f"xrandr --newmode {newmode}", shell=True)
subprocess.call(f"xrandr --addmode {screen_name} {newmode_name}", shell=True)
subprocess.call(f"xrandr --output {screen_name} --mode {newmode_name}", shell=True)
print("ok")
