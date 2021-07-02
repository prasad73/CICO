from m5stack import *
from m5stack_ui import *
from uiflow import *
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xffffff)


bright = None







screen.set_screen_brightness(0)
wait(2)
for bright in range(0, 100, 1):
  screen.set_screen_brightness(bright)
  wait_ms(20)
label0 = M5Label('HELLO SAJIN', x=70, y=80, color=0x000, font=FONT_MONT_40, parent=None)
