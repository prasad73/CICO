from m5stack import *
from m5stack_ui import *
from uiflow import *

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000000)






try:
  with open('/sd/check.text', 'w') as fs:
    fs.write('OK')
    wait_ms(200)
except:
  while True:
    lcd.clear()
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('INSERT SD CARD & RESTART!!', 10, 100, 0xcc0000)
    wait(3)
   
 
with open('/sd/history.text', 'a') as fs:
  os.remove('/sd/history.text')
with open('/sd/id.text', 'a') as fs:
  os.remove('/sd/id.text')
with open('/sd/date.text', 'a') as fs:
  os.remove('/sd/date.text')
with open('/sd/check.text', 'a') as fs:
  os.remove('/sd/check.text')
lcd.print('CLEAR MODE-5', 10, 10, 0xffffff)
lcd.print('ERASE FINISHED..', 100, 100, 0xffffff)
lcd.print('Ready to Burn', 100, 140, 0xffffff)
nvs.write(str('2'), '0')
wait(1)
