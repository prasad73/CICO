from m5stack import *
from m5stack_ui import *
from uiflow import *

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)





switch0 = M5Switch(x=111, y=185, w=70, h=30, bg_c=0xdf0404, color=0xa21414, parent=None)
label0 = M5Label('HELLO M5 STACK', x=18, y=104, color=0x000, font=FONT_MONT_32, parent=None)
