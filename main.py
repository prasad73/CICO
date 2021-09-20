from m5stack import *
from m5stack_ui import *
from uiflow import *
import gc
from m5stack import *
from m5stack_ui import *
from uiflow import *
import espnow
import wifiCfg
import nvs
from machine import WDT
import gc
gc.enable()



screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000000)
wifiCfg.wlan_ap.active(True)
wifiCfg.wlan_sta.active(True)
espnow.init()

global DEVICE_CHECK



EMPLOYEE_ID=None
CURRENT_MINUTE=None
CURRENT_HOUR=None
CURRENT_YEAR=None
CURRENT_MONTH=None
CURRENT_DAY=None
CLOCK=None
MAC_ID=None
TASK_NUMBERS=None

QR_EMPLOYEE_ID=None
QR_CURRENT_MINUTE=None
QR_CURRENT_HOUR=None
QR_CURRENT_YEAR=None
QR_CURRENT_MONTH=None
QR_CURRENT_DAY=None
QR_CLOCK=None
PASSWORD="01"




def PATTERN_CIN_SAVE():
  global EMPLOYEE_ID
  global CURRENT_MINUTE
  global CURRENT_HOUR
  global CURRENT_YEAR
  global CURRENT_MONTH
  global CURRENT_DAY
  global REFRESH_SCREEN
  global CLOCK
  global MAC_ID
  global TASK_NUMBERS
  
  global QR_EMPLOYEE_ID
  global QR_CURRENT_MINUTE
  global QR_CURRENT_HOUR
  global QR_CURRENT_YEAR
  global QR_CURRENT_MONTH
  global QR_CURRENT_DAY
  global QR_CLOCK
 
  
  QR_CODE=None
  MAC_ID=espnow.get_mac_addr() ## maci id of m5
  MAC_ID=MAC_ID[12]+MAC_ID[13]+MAC_ID[15]+MAC_ID[16] ## we need only last 4 digits
  FINAL_PATTERN=None
  FINAL_PATTERN = str(EMPLOYEE_ID)+str(CURRENT_DAY)+str(CURRENT_MONTH)+str(CURRENT_YEAR)+str(CURRENT_HOUR)+str(CURRENT_MINUTE)+str(CLOCK)+str(MAC_ID)+str(TASK_NUMBERS)
  lcd.font(lcd.FONT_DejaVu18)
  lcd.print("Please write down or scan QR ", 0, 20,0x00cccc)
  lcd.font(lcd.FONT_DejaVu24)
  lcd.print("OK", 140, 170,0xFFFFFF)
  
  
  
  


  #CURRENT_DAY=int(str(CURRENT_DAY),16)
  #CURRENT_MONTH=int(str(CURRENT_MONTH),16)
  #CURRENT_YEAR=int(str(CURRENT_YEAR),16)
  
 
  QR_CODE= str(QR_EMPLOYEE_ID)+"."+str(QR_CURRENT_DAY)+"."+str(QR_CURRENT_MONTH)+"."+str(QR_CURRENT_YEAR)+"."+str(QR_CURRENT_HOUR)+"."+str(QR_CURRENT_MINUTE)+"."+str(QR_CLOCK)+"."+str(MAC_ID)
  lcd.font(lcd.FONT_Default)
  lcd.print(str(QR_CODE), 0, 60,0xffffff)
  lcd.print(str(TASK_NUMBERS), 0, 80,0xffffff)
  lcd.qrcode(QR_CODE, 0, 110, 130)
 
                                                                                                                                                                                                                         
  
  while True:
    if (touch.status())==1 and (touch.read()[0]) >120 and (touch.read()[0]) <200  and (touch.read()[1]) >150 and  (touch.read()[1]) <230:
      speaker.playWAV('/sd/button.wav')
      
      try:
        with open('/sd/history.text', 'a') as fs:
          fs.write(FINAL_PATTERN+"\n")
      except:
        del FINAL_PATTERN
        del QR_CODE
        gc.collect()
        return -1
      else:
        del FINAL_PATTERN
        del QR_CODE
        gc.collect()
        return 1
        
          

def CLOCK_IN_WRITE():  # ID WRITING 
  global EMPLOYEE_ID
  with open('/sd/id.text', 'a') as fs:
    fs.write(EMPLOYEE_ID+"\n")
  return 1
  


def CLOCK_IN_CHECK():  # CHECKING CLOCKINS
  lcd.font(lcd.FONT_DejaVu18)
  lcd.print(str("Plz wait.."), 100, 100, 0xffffff)
  wait(1)
  SD_DATA=None
  LIST_LENGTH=None
  LIST=None
  x=0
  with open('/sd/id.text', 'r') as fs:
    SD_DATA=fs.read()
  LIST=SD_DATA.split()
  LIST_LENGTH=len(LIST)
  
  if LIST_LENGTH==0:
    return 1
  
  
  
  if LIST_LENGTH==1:
    if str(EMPLOYEE_ID)==str(LIST[0]):
      LIST.clear()
      del LIST_LENGTH
      del x
      del SD_DATA
      del LIST
      gc.collect()
      return 0
    else:
      del LIST_LENGTH
      del x
      del SD_DATA
      del LIST
      gc.collect()
      return 1
      
  
   
   
  if LIST_LENGTH>1:
    for x in range(LIST_LENGTH):
      if str(EMPLOYEE_ID)==str(LIST[x]):
         LIST.clear()
         del LIST_LENGTH
         del SD_DATA
         del LIST
         del x
         gc.collect()
         return 0
     
    del LIST_LENGTH
    del SD_DATA
    del LIST
    del x
    gc.collect()     
    return 1
    
    
    
def UPDATE_ID():
  global EMPLOYEE_ID
  SD_DATA=None
  LIST_LENGTH=None
  LIST=None
  x=0
  with open('/sd/id.text', 'r+') as fs:
    SD_DATA=fs.read()
  LIST=SD_DATA.split()
  LIST_LENGTH=len(LIST)
  LIST.remove(str(EMPLOYEE_ID))
  LIST_LENGTH=len(LIST)
  os.remove('/sd/id.text')
  with open('/sd/id.text', 'a') as fs:
    for x in range(0, LIST_LENGTH, 1):
      fs.write(str(LIST[(x)])+"\n")
  del LIST_LENGTH
  del SD_DATA
  del LIST
  del x
  gc.collect()    
  return 1
      
  
  
def TASK_WINDOW():
  lcd.clear()
  global TASK_NUMBERS
  num1="-"
  num2="-"
  num3="-"
  num4="-"
  num5="-"
  num6="-"
  num7="-"
  num8="-"
  num9="-"
  num10="-"
  num11="-"
  num12="-"
  num13="-"
  num14="-"
  num15="-"
  num16="-"
  num17="-"
  num18="-"
  num19="-"
  num20="-"
  num21="-"
  num22="-"
  num23="-"
  num24="-"
  num25="-"
  num26="-"
  num27="-"
  num28="-"
  num29="-"
  num30="-"
  i=0
  var=None
  length=0
  
  while True:
    lcd.font(lcd.FONT_DejaVu18)
    lcd.circle(30, 60, 20, color=0xffffff)
    lcd.circle(110, 60, 20, color=0xffffff)
    lcd.circle(190, 60, 20, color=0xffffff)
    lcd.circle(270, 60, 20, color=0xffffff)
    lcd.circle(30, 120, 20, color=0xffffff)
    lcd.circle(110, 120, 20, color=0xffffff)
    lcd.circle(190, 120, 20, color=0xffffff)
    lcd.circle(270, 120, 20, color=0xffffff)
    lcd.circle(30, 180, 20, color=0xffffff)
    lcd.circle(110, 180, 20, color=0xffffff)
    lcd.circle(190, 180, 20, color=0xffffff)
    lcd.circle(270, 180, 20, color=0xffffff)
    lcd.print('0', 25, 55, 0xffffff)
    lcd.print('1', 105, 55, 0xffffff)
    lcd.print('2', 185, 55, 0xffffff)
    lcd.print('3', 265, 55, 0xffffff)
    lcd.print('4', 25, 115, 0xffffff)
    lcd.print('5', 105, 115, 0xffffff)
    lcd.print('6', 185, 115, 0xffffff)
    lcd.print('7', 265, 115, 0xffffff)
    lcd.print('8', 25, 175, 0xffffff)
    lcd.print('9', 105, 175, 0xffffff)
    lcd.print(',', 185, 175, 0xffffff)
    lcd.print('E', 265, 175, 0xffffff)
    lcd.print('BACK', 0, 220, 0xffffff)
    lcd.print('CLEAR', 120, 220, 0xffffff)
    if (touch.status())==1 and (touch.read()[0]) >0 and (touch.read()[0]) <80  and (touch.read()[1]) >75 and  (touch.read()[1]) <90:
      speaker.playWAV('/sd/button.wav')
      i=i+1#
      var='0'
    if (touch.status())==1 and (touch.read()[0]) >100 and (touch.read()[0]) <130  and (touch.read()[1]) >75 and  (touch.read()[1]) <90:
      speaker.playWAV('/sd/button.wav')
      i=i+1#
      var='1'
    if (touch.status())==1 and (touch.read()[0]) >170 and (touch.read()[0]) <200  and (touch.read()[1]) >75 and  (touch.read()[1]) <100:
      speaker.playWAV('/sd/button.wav')
      i=i+1#
      var='2'
    if (touch.status())==1 and (touch.read()[0]) >250 and (touch.read()[0]) <280  and (touch.read()[1]) >75 and  (touch.read()[1]) <100:
      speaker.playWAV('/sd/button.wav')
      i=i+1#
      var='3'
    if (touch.status())==1 and (touch.read()[0]) >0 and (touch.read()[0]) <80  and (touch.read()[1]) >120 and  (touch.read()[1]) <140:
      speaker.playWAV('/sd/button.wav')
      i=i+1#
      var='4'
    if (touch.status())==1 and (touch.read()[0]) >90 and (touch.read()[0]) <130  and (touch.read()[1]) >120 and  (touch.read()[1]) <140:
      speaker.playWAV('/sd/button.wav')
      i=i+1#
      var='5'
    if (touch.status())==1 and (touch.read()[0]) >165 and (touch.read()[0]) <195  and (touch.read()[1]) >120 and  (touch.read()[1]) <140:
      speaker.playWAV('/sd/button.wav')
      i=i+1#
      var='6'
    if (touch.status())==1 and (touch.read()[0]) >220 and (touch.read()[0]) <300  and (touch.read()[1]) >120 and  (touch.read()[1]) <140:
      speaker.playWAV('/sd/button.wav')
      i=i+1#
      var='7'
    if (touch.status())==1 and (touch.read()[0]) >0 and (touch.read()[0]) <80  and (touch.read()[1]) >170 and  (touch.read()[1]) <200:
      speaker.playWAV('/sd/button.wav')
      i=i+1#
      var='8'
    if (touch.status())==1 and (touch.read()[0]) >100 and (touch.read()[0]) <130  and (touch.read()[1]) >170 and  (touch.read()[1]) <200:
      speaker.playWAV('/sd/button.wav')
      i=i+1#
      var='9'
    if (touch.status())==1 and (touch.read()[0]) >155 and (touch.read()[0]) <200  and (touch.read()[1]) >170 and  (touch.read()[1]) <200:
      speaker.playWAV('/sd/button.wav')
      i=i+1#
      var=','
    if (touch.status())==1 and (touch.read()[0]) >130 and (touch.read()[0]) <200  and (touch.read()[1]) >200 and  (touch.read()[1]) <260:  # clear
      
      lcd.clear()
      num1="-"
      num2="-"
      num3="-"
      num4="-"
      num5="-"
      num6="-"
      num7="-"
      num8="-"
      num9="-"
      num10="-"
      num11="-"
      num12="-"
      num13="-"
      num14="-"
      num15="-"
      num16="-"
      num17="-"
      num18="-"
      num19="-"
      num20="-"
      num21="-"
      num22="-"
      num23="-"
      num24="-"
      num25="-"
      num26="-"
      num27="-"
      num28="-"
      num29="-"
      num30="-"
      i=0
      var=None
      
      
      
    if (touch.status())==1 and (touch.read()[0]) >50 and (touch.read()[0]) <70  and (touch.read()[1]) >200 and  (touch.read()[1]) <250: # back
       speaker.playWAV('/sd/button.wav')
       del i
       del var
       del length
       del num1
       del num2
       del num3
       del num4
       del num5
       del num6
       del num7
       del num8
       del num9
       del num10
       del num11
       del num12
       del num13
       del num14
       del num15
       del num16
       del num17
       del num18
       del num19
       del num20
       del num21
       del num22
       del num23
       del num24
       del num25
       del num26
       del num27
       del num28
       del num29
       del num30
       gc.collect()
       lcd.clear()
       return 0
    if (touch.status())==1 and (touch.read()[0]) >235 and (touch.read()[0]) <290  and (touch.read()[1]) >170 and  (touch.read()[1]) <200:
      speaker.playWAV('/sd/button.wav')
      if num1==None and num2==None and num3==None and num4==None and num5==None and num6==None and num7==None and num8==None and num9==None and num10==None and num11==None and num12==None and num13==None and num14==None and num15==None  and num16==None and num17==None and num18==None and  num19==None and num20==None and num21==None and  num22==None and num23==None and num24==None and num25==None and num26==None and num27==None and num28==None and num29==None:                                                                            
        lcd.clear()
        lcd.print(str("NO TASk CODE FOUND.!"), 40, 100, 0xffffff)
        speaker.playWAV('/sd/warning.wav')
        wait(1)
        lcd.clear()
      else:
        TASK_NUMBERS=str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)+str(num7)+str(num8)+str(num9)+str(num10)+str(num11)+str(num12)+str(num13)+str(num14)+str(num15)+str(num16)+str(num17)+str(num18)+str(num19)+str(num20)+str(num21)+str(num22)+str(num23)+str(num24)+str(num25)+str(num26)+str(num27)+str(num28)+str(num29)        
        del i
        del var
        del length
        del num1
        del num2
        del num3
        del num4
        del num5
        del num6
        del num7
        del num8
        del num9
        del num10
        del num11
        del num12
        del num13
        del num14
        del num15
        del num16
        del num17
        del num18
        del num19
        del num20
        del num21
        del num22
        del num23
        del num24
        del num25
        del num26
        del num27
        del num28
        del num29
        del num30
        gc.collect()
        return -1
        
        
     
      
        
    if i==1:
      num1=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num1, 0, 10,  0x66ff99)
    if i==2:
      num2=var
      lcd.print(num2, 10, 10,  0x66ff99)
     
    if i==3:
      num3=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num3, 20, 10,  0x66ff99)
      
    if i==4:
      num4=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num4, 30, 10,  0x66ff99)
    if i==5:
      num5=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num5, 40, 10,  0x66ff99)
      
    if i==6:
      num6=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num6, 50, 10,  0x66ff99)
    if i==7:
      num7=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num7, 60, 10,  0x66ff99)
      
    if i==8:
      num8=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num8, 70, 10,  0x66ff99)
     
    if i==9:
      num9=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num9, 80, 10,  0x66ff99)
    if i==10:
      num10=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num10, 90, 10,  0x66ff99)
    if i==11:
      num11=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num11, 100, 10,  0x66ff99)
      
    if i==12:
      num12=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num12, 110, 10,  0x66ff99)
    if i==13:
      num13=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num13, 120, 10,  0x66ff99)
    if i==14:
      num14=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num14, 130, 10,  0x66ff99)
      
    if i==15:
       num15=var
       lcd.font(lcd.FONT_DejaVu18)
       lcd.print(num15, 140, 10,  0x66ff99)
    if i==16:
       num16=var
       lcd.font(lcd.FONT_DejaVu18)
       lcd.print(num16, 150, 10,  0x66ff99)
    if i==17:
      num17=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num17, 160, 10,  0x66ff99)
     
    if i==18:
      num18=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num18, 170, 10,  0x66ff99)
    if i==19:
      num19=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num19, 180, 10,  0x66ff99)
    if i==20:
      num20=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num20, 190, 10,  0x66ff99)
     
    if i==21:
      num21=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num21, 200, 10,  0x66ff99)
    if i==22:
      num22=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num22, 210, 10,  0x66ff99)
    if i==23:
      num23=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num23, 220, 10,  0x66ff99)
      
    if i==24:
      num24=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num24, 230, 10,  0x66ff99)
    if i==25:
      num25=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num25, 240, 10,  0x66ff99)
    if i==26:
      num26=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num26, 250, 10,  0x66ff99)
      
    if i==27:
      num27=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num27, 260, 10,  0x66ff99)
    if i==28:
      num28=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num28, 270, 10,  0x66ff99)
    if i==29:
      num29=var
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(num29, 280, 10,  0x66ff99)
    if i==30:
      lcd.print(" ", 290, 10,  0x66ff99)
  
     
    
  
 

    
  
   

  




def  GET_TIME_DATE():
  global CURRENT_HOUR
  global CURRENT_MINUTE
  global CURRENT_DAY
  global CURRENT_MONTH
  global CURRENT_YEAR
  
  global QR_CURRENT_MINUTE
  global QR_CURRENT_HOUR
  global QR_CURRENT_YEAR
  global QR_CURRENT_MONTH
  global QR_CURRENT_DAY
 
  length_hour=0
  length_minute=0
  length_day=0
  length_month=0
  length_year=0
  
  
 
  
  
  CURRENT_HOUR=hex(CURRENT_HOUR)[2:]    ## CONVERTING INT HOUR TO HEX HEX HOUR
  CURRENT_MINUTE=hex(CURRENT_MINUTE)[2:]  ## CONVERTING INT MINUTE TO HEX HEX MINUTE
  CURRENT_DAY=hex(CURRENT_DAY)[2:]      ## CONVERTING INT DAY TO HEX HEX DAY  
  CURRENT_MONTH=hex(CURRENT_MONTH)[2:]   ## CONVERTING INT MONTH TO HEX HEX MONTH
  CURRENT_YEAR=hex(CURRENT_YEAR)[2:]      ## CONVERTING INT YEAR TO HEX HEX YEAR
  
  QR_CURRENT_MINUTE=CURRENT_MINUTE
  QR_CURRENT_HOUR=CURRENT_HOUR
  QR_CURRENT_YEAR=CURRENT_YEAR
  QR_CURRENT_MONTH=CURRENT_MONTH
  QR_CURRENT_DAY=CURRENT_DAY
   
   
   
   

  
  length_hour=len(CURRENT_HOUR)   ## FIND LENGTH OF HOUR
  length_minute=len(CURRENT_MINUTE) ## FIND LENGTH OF MINUTE
  length_day=len(CURRENT_DAY) ## FIND LENGTH OF DAY
  length_month=len(CURRENT_MONTH) ## FIND LENGTH OF MONTH
  length_year=len(CURRENT_YEAR) ## FIND LENGTH OF YEAR
  
  
  
  if length_hour==1:
    
    CURRENT_HOUR="0"+"0"+"0"+"0"+"0"+"0"+"0"+CURRENT_HOUR   ## HOUR FORMATTING
  
  if length_hour==2:
    CURRENT_HOUR="0"+"0"+"0"+"0"+"0"+"0"+ CURRENT_HOUR    
    
  if length_minute==1:
    CURRENT_MINUTE="0"+"0"+"0"+"0"+"0"+"0"+"0"+ CURRENT_MINUTE##MINUTE FORMATTING
  
  if length_minute==2:
    CURRENT_MINUTE="0"+"0"+"0"+"0"+"0"+"0"+CURRENT_MINUTE
    
  if length_day==1:
    CURRENT_DAY="0"+"0"+"0"+"0"+"0"+"0"+"0"+CURRENT_DAY   ## DAY FORMATTING
  
  if length_day==2:
    CURRENT_DAY="0"+"0"+"0"+"0"+"0"+"0"+ CURRENT_DAY
    
  if length_month==1:
    CURRENT_MONTH="0"+"0"+"0"+"0"+"0"+"0"+"0"+ CURRENT_MONTH  ##MONTH FORMATTING
  
  if length_month==2:
    CURRENT_MONTH="0"+"0"+"0"+"0"+"0"+"0"+ CURRENT_MONTH
     
  if length_year==3:
    CURRENT_YEAR="0"+"0"+"0"+"0"+"0"+CURRENT_YEAR   ## year formating
    
  del length_hour
  del length_minute
  del length_day
  del length_month
  del length_year
  gc.collect()
  
  
  
  return 1
  

def EMP_KEYPAD():  ## EMPLOYEE ID KEYPAD FUNCTION
  num1=None
  num2=None
  num3=None
  num4=None
  num5=None
  num6=None
  num7=None
  num8=None
  length=0
  global EMPLOYEE_ID
  global QR_EMPLOYEE_ID
  i=0
  var=None
  gc.collect()
  while True:
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('ID :', 5, 20, 0xffffff)
    lcd.print('Back', 250, 10, 0xffffff)
    lcd.circle(40, 75, 20, color=0xff0000)
    lcd.print('0', 35, 70, 0xffffff)
    lcd.circle(120, 75, 20, color=0xff0000)
    lcd.print('1', 115, 70, 0xffffff)
    lcd.circle(200, 75, 20, color=0xff0000)
    lcd.print('2', 195, 70, 0xffffff)
    lcd.circle(280, 75, 20, color=0xff0000)
    lcd.print('3', 275, 70, 0xffffff)
    lcd.circle(40, 140, 20, color=0xff0000)
    lcd.print('4', 35, 135, 0xffffff)
    lcd.circle(120, 140, 20, color=0xff0000)
    lcd.print('5', 115, 135, 0xffffff)
    lcd.circle(200, 140, 20, color=0xff0000)
    lcd.print('6', 195, 135, 0xffffff)
    lcd.circle(280, 140, 20, color=0xff0000)
    lcd.print('7', 275, 135, 0xffffff)
    lcd.circle(40, 210, 20, color=0xff0000)
    lcd.print('8', 35, 205, 0xffffff)
    lcd.circle(120, 210, 20, color=0xff0000)
    lcd.print('9', 115, 205, 0xffffff)
    lcd.circle(200, 210, 20, color=0xff0000)
    lcd.print('C', 195, 203, 0xffffff)
    lcd.circle(280, 210, 20, color=0xff0000)
    lcd.print('E', 275, 203, 0xffffff)
    
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <70  and (touch.read()[1]) >80 and  (touch.read()[1]) <110: # 0
      speaker.playWAV('/sd/button.wav')
      var='0'
      i=i+1
      
    if (touch.status())==1 and (touch.read()[0]) >120 and (touch.read()[0]) <140  and (touch.read()[1]) >80 and  (touch.read()[1]) <110: # 1
      speaker.playWAV('/sd/button.wav')
      var='1'
      i=i+1
      
    if (touch.status())==1 and (touch.read()[0]) >185 and (touch.read()[0]) <220  and (touch.read()[1]) >80 and  (touch.read()[1]) <110: # 2
      speaker.playWAV('/sd/button.wav')
      var='2'
      i=i+1
      
    if (touch.status())==1 and (touch.read()[0]) >265 and (touch.read()[0]) <300  and (touch.read()[1]) >80 and  (touch.read()[1]) <110: # 3
      speaker.playWAV('/sd/button.wav')
      var='3'
      i=i+1
    
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <70  and (touch.read()[1]) >140 and  (touch.read()[1]) <170: # 4
      speaker.playWAV('/sd/button.wav')
      var='4'
      i=i+1
      
    if (touch.status())==1 and (touch.read()[0]) >110 and (touch.read()[0]) <155  and (touch.read()[1]) >140 and  (touch.read()[1]) <170: # 5
      speaker.playWAV('/sd/button.wav')
      var='5'
      i=i+1
      
    if (touch.status())==1 and (touch.read()[0]) >170 and (touch.read()[0]) <210  and (touch.read()[1]) >140 and  (touch.read()[1]) <175: #6
      speaker.playWAV('/sd/button.wav')
      var='6'
      i=i+1
      
    if (touch.status())==1 and (touch.read()[0]) >255 and (touch.read()[0]) <280  and (touch.read()[1]) >140 and  (touch.read()[1]) <170: #7
      speaker.playWAV('/sd/button.wav')
      var='7'
      i=i+1
      
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <90  and (touch.read()[1]) >200 and  (touch.read()[1]) <210: #8
      speaker.playWAV('/sd/button.wav')
      var='8'
      i=i+1
      
    if (touch.status())==1 and (touch.read()[0]) >110 and (touch.read()[0]) <150  and (touch.read()[1]) >200 and  (touch.read()[1]) <230: #9
      speaker.playWAV('/sd/button.wav')
      var='9'
      i=i+1
      
    if (touch.status())==1 and (touch.read()[0]) >195 and (touch.read()[0]) <230  and (touch.read()[1]) >200 and  (touch.read()[1]) <230: # CLEAR
      speaker.playWAV('/sd/button.wav')
      var='C'
      i=0
      lcd.clear()
      num1=None
      num2=None
      num3=None
      num4=None
      num5=None
      num6=None
      num7=None
      num8=None
      
    if (touch.status())==1 and (touch.read()[0]) >230 and (touch.read()[0]) <280  and (touch.read()[1]) >40 and  (touch.read()[1]) <70: # back
      speaker.playWAV('/sd/button.wav')

      del num1
      del num2
      del num3
      del num4    # deleting local variables
      del num5
      del num6
      del num7
      del num8
      del var
      del i
      return 0
      gc.collect()  # garbage collect
      
      
    #### NUMBER PLACEMENT IN EACH DISPLAY  POSITION
    if i==1:
      num1=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print(num1, 60, 20,  0x66ff99)
    if i==2:
      num2=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print(num2, 80, 20, 0x66ff99)
    if i==3:
      num3=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print(num3, 100, 20, 0x66ff99)
    if i==4:
      num4=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print(num4, 120, 20, 0x66ff99)
    if i==5:
      num5=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print(num5, 140, 20, 0x66ff99)
    if i==6:
      num6=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print(num6, 160, 20, 0x66ff99)
    if i==7:
      num7=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print(num7, 180, 20, 0x66ff99)
    if i==8:
      num8=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print(num8, 200, 20, 0x66ff99)
    if i==9:
      num9=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print(" ", 220, 20, 0x66ff99)
      
    if (touch.status())==1 and (touch.read()[0]) >255 and (touch.read()[0]) <290  and (touch.read()[1]) >200 and  (touch.read()[1]) <230:
      speaker.playWAV('/sd/button.wav')
      if str(num1)==str(None) or str(num2)==str(None) or str(num3)==str(None) or str(num4)==str(None): # checking employee is vallid , {minimum integers need}
       
        num1=None
        num2=None
        num3=None
        num4=None
        num5=None
        num6=None   # NOT VALID ID
        num7=None
        num8=None
        i=0
        var=0
        return 2
      if str(num1)!=str(None) and str(num2)!=str(None) and str(num3)!=str(None) and str(num4)!=str(None) and  str(num5)!=str(None) and str(num6)!=str(None) and str(num7)!=str(None) and str(num8)!=str(None):
        EMPLOYEE_ID=str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)+str(num7)+str(num8)
        EMPLOYEE_ID=int(EMPLOYEE_ID,10)
        EMPLOYEE_ID=hex(EMPLOYEE_ID)[2:]
        QR_EMPLOYEE_ID=EMPLOYEE_ID
        length=len(EMPLOYEE_ID)
        if length==4:
          EMPLOYEE_ID="0"+"0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1

        if length==5:
          EMPLOYEE_ID="0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==6:
          EMPLOYEE_ID="0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==7:
          EMPLOYEE_ID="0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
      
      if str(num1)!=str(None) and str(num2)!=str(None) and str(num3)!=str(None) and str(num4)!=str(None) and  str(num5)!=str(None) and str(num6)!=str(None) and str(num7)!=str(None) and str(num8)==str(None):
        EMPLOYEE_ID=str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)+str(num7)
        EMPLOYEE_ID=int(EMPLOYEE_ID,10)
        EMPLOYEE_ID=hex(EMPLOYEE_ID)[2:]
        QR_EMPLOYEE_ID=EMPLOYEE_ID
        length=len(EMPLOYEE_ID)
        if length==4:
          EMPLOYEE_ID="0"+"0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==5:
          EMPLOYEE_ID="0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==6:
          EMPLOYEE_ID="0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==7:
          EMPLOYEE_ID="0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
      if str(num1)!=str(None) and str(num2)!=str(None) and str(num3)!=str(None) and str(num4)!=str(None) and  str(num5)!=str(None) and str(num6)!=str(None) and str(num7)==str(None) and str(num8)==str(None):
        EMPLOYEE_ID=str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)
        EMPLOYEE_ID=int(EMPLOYEE_ID,10)
        EMPLOYEE_ID=hex(EMPLOYEE_ID)[2:]
        QR_EMPLOYEE_ID=EMPLOYEE_ID
        length=len(EMPLOYEE_ID)
        if length==4:
          EMPLOYEE_ID="0"+"0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==5:
          EMPLOYEE_ID="0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==6:
          EMPLOYEE_ID="0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==7:
          EMPLOYEE_ID="0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
      if str(num1)!=str(None) and str(num2)!=str(None) and str(num3)!=str(None) and str(num4)!=str(None) and  str(num5)!=str(None) and str(num6)==str(None) and str(num7)==str(None) and str(num8)==str(None):
        EMPLOYEE_ID=str(num1)+str(num2)+str(num3)+str(num4)+str(num5)
        EMPLOYEE_ID=int(EMPLOYEE_ID,10)
        EMPLOYEE_ID=hex(EMPLOYEE_ID)[2:]
        QR_EMPLOYEE_ID=EMPLOYEE_ID
        length=len(EMPLOYEE_ID)
        if length==4:
          EMPLOYEE_ID="0"+"0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==5:
          EMPLOYEE_ID="0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==6:
          EMPLOYEE_ID="0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==7:
          EMPLOYEE_ID="0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
      if str(num1)!=str(None) and str(num2)!=str(None) and str(num3)!=str(None) and str(num4)!=str(None) and  str(num5)!=str(None) and str(num6)==str(None) and str(num7)==str(None) and str(num8)==str(None):
        EMPLOYEE_ID=str(num1)+str(num2)+str(num3)+str(num4)+str(num5)
        EMPLOYEE_ID=int(EMPLOYEE_ID,10)
        EMPLOYEE_ID=hex(EMPLOYEE_ID)[2:]
        QR_EMPLOYEE_ID=EMPLOYEE_ID
        length=len(EMPLOYEE_ID)
        if length==4:
          EMPLOYEE_ID="0"+"0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==5:
          EMPLOYEE_ID="0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==6:
          EMPLOYEE_ID="0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==7:
          EMPLOYEE_ID="0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
      if str(num1)!=str(None) and str(num2)!=str(None) and str(num3)!=str(None) and str(num4)!=str(None) and  str(num5)==str(None) and str(num6)==str(None) and str(num7)==str(None) and str(num8)==str(None):
        EMPLOYEE_ID=str(num1)+str(num2)+str(num3)+str(num4)
        EMPLOYEE_ID=int(EMPLOYEE_ID,10)
        EMPLOYEE_ID=hex(EMPLOYEE_ID)[2:]
        QR_EMPLOYEE_ID=EMPLOYEE_ID
        length=len(EMPLOYEE_ID)
        if length==3:
          EMPLOYEE_ID="0"+"0"+"0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
          
        if length==4:
          EMPLOYEE_ID="0"+"0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==5:
          EMPLOYEE_ID="0"+"0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==6:
          EMPLOYEE_ID="0"+"0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        if length==7:
          EMPLOYEE_ID="0"+EMPLOYEE_ID
          del num1
          del num2
          del num3
          del num4    # deleting local variables
          del num5
          del num6
          del num7
          del num8
          del var
          del i
          del length
          gc.collect()
          return 1
        
        
def SD():
  check=None
  try:
    with open('/sd/check.text', 'r') as fs:
      check=fs.read()
  except:
    del check
    gc.collect()
    return -1
  else:
    del check
    gc.collect()
    return 1
    
    
  
def TASK_QN():
  lcd.clear()
  lcd.font(lcd.FONT_DejaVu18)
  lcd.print('DID YOU COMPLETE ALL TASKS', 0, 100, 0xffffff)
  lcd.print('DID YOU COMPLETE ALL TASKS', 0, 100, 0xffffff)
  lcd.print('NO', 30, 160, 0xff0808)
  lcd.print('YES TO ALL', 150, 160, 0x08ff62)
  while True:
     if (touch.status())==1 and (touch.read()[0]) >150 and (touch.read()[0]) <220  and (touch.read()[1]) >170 and  (touch.read()[1]) <200:
       speaker.playWAV('/sd/button.wav')
       return 1
     if (touch.status())==1 and (touch.read()[0]) >0 and (touch.read()[0]) <60  and (touch.read()[1]) >170 and  (touch.read()[1]) <200:
       speaker.playWAV('/sd/button.wav')
       return 2
       


def HISTORY():

  SD_DATA=None
  LIST_LENGTH=None
  LIST=None
  x=0
  with open('/sd/history.text', 'r') as fs:
    SD_DATA=fs.read()
  LIST=SD_DATA.split()
  LIST_LENGTH=len(LIST)
  LIST_LENGTH=LIST_LENGTH-1
  if LIST_LENGTH>=0:
    SHOW(x,LIST_LENGTH,LIST)
  else:
    return 0
    
   

  while True:
    
    lcd.print('HISTORY', 0, 0, 0xffff33)
    lcd.print('PREV', 10, 197, 0x208e8a)
    lcd.print('NEXT', 230, 197, 0x208e8a)
    lcd.print('BACK', 130, 197, 0x208e8a)
    if (touch.status())==1 and (touch.read()[0]) >150 and (touch.read()[0]) <170  and (touch.read()[1]) >200 and  (touch.read()[1]) <280:
      speaker.playWAV('/sd/button.wav')
      del SD_DATA
      del LIST_LENGTH
      del LIST
      del x
      return -1
    if (touch.status())==1 and (touch.read()[0]) >220 and (touch.read()[0]) <280  and (touch.read()[1]) >200 and  (touch.read()[1]) <250:
      if x<LIST_LENGTH:
        x=x+1
        lcd.clear()
        SHOW(x,LIST_LENGTH,LIST)
      else:
        x=LIST_LENGTH
  
    if (touch.status())==1 and (touch.read()[0]) >60 and (touch.read()[0]) <80  and (touch.read()[1]) >200 and  (touch.read()[1]) <250:
      if x>0:
        x=x-1
        lcd.clear()
        SHOW(x,LIST_LENGTH,LIST)
      else:
        x=0
        
        
       
def SHOW(x,LIST_LENGTH,LIST):
  FILE_DATA=LIST[x]
  employee_id= FILE_DATA[0]+ FILE_DATA[1]+FILE_DATA[2]+FILE_DATA[3]+ FILE_DATA[4]+FILE_DATA[5]+FILE_DATA[6]+FILE_DATA[7]
  employee_id=int(employee_id,16)
  day= FILE_DATA[8]+ FILE_DATA[9]+FILE_DATA[10]+FILE_DATA[11]+ FILE_DATA[12]+FILE_DATA[13]+FILE_DATA[14]+FILE_DATA[15]
  day=int(day,16)
  month=FILE_DATA[16]+FILE_DATA[17]+FILE_DATA[18]+FILE_DATA[19]+ FILE_DATA[20]+FILE_DATA[21]+FILE_DATA[22]+FILE_DATA[23]
  month=int(month,16)
  year=FILE_DATA[24]+FILE_DATA[25]+FILE_DATA[26]+FILE_DATA[27]+ FILE_DATA[28]+FILE_DATA[29]+FILE_DATA[30]+FILE_DATA[31]
  year=int(year,16)
  hour=FILE_DATA[32]+FILE_DATA[33]+FILE_DATA[34]+FILE_DATA[35]+ FILE_DATA[36]+FILE_DATA[37]+FILE_DATA[38]+FILE_DATA[39]
  hour=int(hour,16)
  minute=FILE_DATA[40]+FILE_DATA[41]+FILE_DATA[42]+FILE_DATA[43]+ FILE_DATA[44]+FILE_DATA[45]+FILE_DATA[46]+FILE_DATA[47]
  minute=int(minute,16)
  clock= FILE_DATA[48]+FILE_DATA[49]+FILE_DATA[50]+FILE_DATA[51]+ FILE_DATA[52]+FILE_DATA[53]+FILE_DATA[54]+FILE_DATA[55]
  clock=int(clock,16)
  device_id=FILE_DATA[56]+FILE_DATA[57]+FILE_DATA[58]+FILE_DATA[59]
  task=FILE_DATA[60]+ FILE_DATA[61]+FILE_DATA[62]+FILE_DATA[63]+ FILE_DATA[64]+FILE_DATA[65]+FILE_DATA[66]+FILE_DATA[67]+ FILE_DATA[68]+ FILE_DATA[69]+FILE_DATA[70]+FILE_DATA[71]+ FILE_DATA[72]+FILE_DATA[73]+FILE_DATA[74]+FILE_DATA[75]+ FILE_DATA[76]+ FILE_DATA[77]+FILE_DATA[78]+FILE_DATA[79]+ FILE_DATA[80]+FILE_DATA[81]+FILE_DATA[82]+FILE_DATA[83]+FILE_DATA[84]+FILE_DATA[85]+FILE_DATA[86]+FILE_DATA[87]+FILE_DATA[88]
  lcd.font(lcd.FONT_DejaVu18)
  lcd.print(str(x), 200, 0, 0xffff33)
  lcd.print(str("/"), 230, 0, 0xffff33)
  lcd.print(str(LIST_LENGTH), 250, 0, 0xffff33)
  lcd.print(str(employee_id), 0, 30, 0xffffff)
  lcd.print(str(day), 0, 50, 0xffffff)
  lcd.print(str(month), 30, 50, 0xffffff)
  lcd.print(str(year), 50, 50, 0xffffff)
  lcd.print(str(hour), 0, 70, 0xffffff)
  lcd.print(str(minute), 30, 70, 0xffffff)
  if clock==1:
    lcd.print(str("CIN"), 0, 90, 0xffffff)
  else:
    lcd.print(str("COUT"), 0, 90, 0xffffff)
  lcd.print(str(device_id), 0, 110, 0xffffff)
  employee_id=hex(employee_id)[2:]
  day=hex(day)[2:]
  month=hex(month)[2:]
  year=hex(year)[2:]
  hour=hex(hour)[2:]
  minute=hex(minute)[2:]
  clock=hex(clock)[2:]
  lcd.print(employee_id+"."+day+"."+month+"."+year+"."+hour+"."+minute+"."+clock+"."+device_id, 0, 130, 0xffffff)
  lcd.print(str(task), 0, 150, 0xffffff)
  del employee_id
  del day
  del month
  del year
  del hour
  del minute
  del clock
  del device_id
  del task
  del FILE_DATA
 
  
def PASSWORD_WINDOW():
  global PASSWORD
  i=0
  num1=""
  num2=""
  num3=""
  num4=""
  num5=""
  num6=""
  num7=""
  login_id=None
  while True:
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('ENTER ID', 5, 20,  0xffffff)
    lcd.circle(50, 80, 20, color= 0xffffff)
    lcd.print("0", 45, 75, 0xffffff)
    lcd.circle(120, 80, 20, color= 0xffffff)
    lcd.print("1", 115, 75, 0xffffff)
    lcd.circle(190, 80, 20, color= 0xffffff)
    lcd.print("2", 185, 75, 0xffffff)
    lcd.circle(270, 80, 20, color= 0xffffff)
    lcd.print("3", 265, 75, 0xffffff)
    lcd.circle(50, 145, 20, color= 0xffffff)
    lcd.print("4", 45, 140, 0xffffff)
    lcd.circle(120, 145, 20, color= 0xffffff)
    lcd.print("5", 115, 140, 0xffffff)
    lcd.circle(190, 145, 20, color =0xffffff)
    lcd.print("6", 185, 140, 0xffffff)
    lcd.circle(270, 145, 20, color= 0xffffff)
    lcd.print("7", 265, 140, 0xffffff)
    lcd.print('NEXT', 190, 200,  0xffffff)
    lcd.print('BACK', 10, 200, 0xffffff)
    if (touch.status())==1 and (touch.read()[0]) >50 and (touch.read()[0]) <80  and (touch.read()[1]) >90 and  (touch.read()[1]) <115:
      speaker.playWAV('/sd/button.wav')
      lcd.print('0', 45, 75, 0xffffff)                     # 0
      var='0'
      i=i+1
    if (touch.status())==1 and (touch.read()[0]) >100 and (touch.read()[0]) <150  and (touch.read()[1]) >90 and  (touch.read()[1]) <115:
      speaker.playWAV('/sd/button.wav')                                   #1
      lcd.print('1', 115, 75, 0xffffff)
      var='1'
      i=i+1
    if (touch.status())==1 and (touch.read()[0]) >160 and (touch.read()[0]) <250  and (touch.read()[1]) >90 and  (touch.read()[1]) <115:
      speaker.playWAV('/sd/button.wav')                                              #2
      lcd.print('2', 185, 75, 0xffffff) 
      var='2'
      i=i+1
    if (touch.status())==1 and (touch.read()[0]) >220 and (touch.read()[0]) <300  and (touch.read()[1]) >90 and  (touch.read()[1]) <115:
      speaker.playWAV('/sd/button.wav')                                          
      lcd.print('3', 265, 75, 0xffffff) 
      var='3'
      i=i+1
    if (touch.status())==1 and (touch.read()[0]) >50 and (touch.read()[0]) <90  and (touch.read()[1]) >125 and  (touch.read()[1]) <170:
      speaker.playWAV('/sd/button.wav')
      lcd.print('4', 45, 140, 0xffffff) 
      var='4'
      i=i+1
    if (touch.status())==1 and (touch.read()[0]) >100 and (touch.read()[0]) <180  and (touch.read()[1]) >125 and  (touch.read()[1]) <180:
      speaker.playWAV('/sd/button.wav')
      lcd.print('5', 115, 140, 0xffffff) 
      var='5'
      i=i+1
    if (touch.status())==1 and (touch.read()[0]) >155 and (touch.read()[0]) <230  and (touch.read()[1]) >125 and  (touch.read()[1]) <185:
      speaker.playWAV('/sd/button.wav')
      lcd.print('6', 185, 140, 0xffffff) 
      var='6'
      i=i+1
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <290  and (touch.read()[1]) >125 and  (touch.read()[1]) <185:
      speaker.playWAV('/sd/button.wav')
      lcd.print('7', 265, 140, 0xffffff) 
      var='7'
      i=i+1
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <300  and (touch.read()[1]) >200 and  (touch.read()[1]) <300: ## verified
      login_id=str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)+str(num7)
      
      if login_id==PASSWORD:
        del num1
        del num2
        del num3
        del num4
        del num5
        del num6
        del num7
        del login_id
        del i
        del var
        return 1
      else:
        del num1
        del num2
        del num3
        del num4
        del num5
        del num6
        del num7
        del login_id
        del i
        return -1
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <100  and (touch.read()[1]) >200 and  (touch.read()[1]) <250: #back
        del num1
        del num2
        del num3
        del num4
        del num5
        del num6
        del num7
        del login_id
        del i
        return 0
         
    if i==1:
      num1=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print('*', 150, 20,  0x66ff99)
    if i==2:
      num2=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print('*', 170, 20, 0x66ff99)
    if i==3:
      num3=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print('*', 190, 20, 0x66ff99)
    if i==4:
      num4=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print('*', 210, 20, 0x66ff99)
    if i==5:
      num5=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print('*', 230, 20, 0x66ff99)
    if i==6:
      num6=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print('*', 250, 20, 0x66ff99)
    if i==7:
      num7=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print('*', 270, 20, 0x66ff99)
    if i==8:
      num8=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print('*', 290, 20, 0x66ff99)
          
    if i==9:
      num9=var
      lcd.font(lcd.FONT_DejaVu24)
      lcd.print('*', 300, 20, 0x66ff99)
        
    
    
def Date_set():
  global CURRENT_HOUR
  global CURRENT_MINUTE
  CURRENT_HOUR=(rtc.datetime()[4])
  CURRENT_MINUTE=(rtc.datetime()[5])
  set_new_day=1
  set_new_month=2
  set_new_year=21
  mode=0
  x=0
  while True:
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print("Day", 20, 10, 0xffffff)
    lcd.print("Month", 100, 10, 0xffffff)
    lcd.print("Year", 200, 10, 0xffffff)
    lcd.print('SAVE', 10, 200, 0xffffff)
    lcd.print('BACK', 190, 200,  0xffffff)
    lcd.font(lcd.FONT_DejaVu40)
    lcd.print('|', 90, 40, 0xffffff)
    lcd.print('|', 180, 40, 0xffffff)
    lcd.print('<-', 30, 130, 0xffffff)
    lcd.print('M', 130, 130, 0xffffff)
    lcd.print('->', 250, 130, 0xffffff)
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <300  and (touch.read()[1]) >200 and  (touch.read()[1]) <300:  # back
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      return 0
      
    if mode==0:
      lcd.print("__", 30, 70, 0x00ff55)
      if x>31:
        x=31
      if x<1:
        x=1
      set_new_day=x
    if mode==1:
      lcd.print("__", 130, 70, 0x00ff55)
      lcd.print("__", 30, 70, 0x000000)
      if x>12:
        x=12
      if x<1:
        x=1
      set_new_month=x
      
    if mode==2:
      lcd.print("__", 220, 70, 0x00ff55)
      lcd.print("__", 30, 70, 0x000000)
      lcd.print("__", 30, 70, 0x000000)
      if x<21:
        x=21
      if x>99:
        x=21
      if x==0:
        x=0
      set_new_year=x
      
    if mode>2:
      mode=0
      
    lcd.print(set_new_day, 30, 40, 0xffffff)
    lcd.print(set_new_month, 120, 40, 0xffffff)
    lcd.print(set_new_year, 200, 40, 0xffffff)
      
    if (touch.status())==1 and (touch.read()[0]) >40 and (touch.read()[0]) <90  and (touch.read()[1]) >150 and  (touch.read()[1]) <180: 
       speaker.playWAV('/sd/button.wav')
       x=x-1
       lcd.clear()
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <300  and (touch.read()[1]) >150 and  (touch.read()[1]) <180:
       speaker.playWAV('/sd/button.wav')
       x=x+1
       lcd.clear()
    if (touch.status())==1 and (touch.read()[0]) >120 and (touch.read()[0]) <180  and (touch.read()[1]) >150 and  (touch.read()[1]) <180:
       speaker.playWAV('/sd/button.wav')
       mode=mode+1
       lcd.clear()
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <100  and (touch.read()[1]) >200 and  (touch.read()[1]) <250: 
       speaker.playWAV('/sd/button.wav')
       rtc.datetime((set_new_year, set_new_month, set_new_day, 0, CURRENT_HOUR, CURRENT_MINUTE, 0, 0))
       del x
       del set_new_day
       del set_new_month
       del set_new_year
       del mode
       gc.collect()
       return 1
       
def Time_set():
  current_year=str(rtc.datetime()[0])
  current_year=str(current_year[2])+str(current_year[3])
  CURRENT_DAY=rtc.datetime()[2]
  CURRENT_MONTH=rtc.datetime()[1]
 
  set_new_hour=1
  set_new_minute=1
  mode=0
  x=0
  while True:
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print("Hour", 20, 10, 0xffffff)
    lcd.print("Minute", 100, 10, 0xffffff)
    lcd.print('SAVE', 10, 200, 0xffffff)
    lcd.print('BACK', 190, 200,  0xffffff)
    lcd.font(lcd.FONT_DejaVu40)
    lcd.print('<-', 30, 130, 0xffffff)
    lcd.print('M', 130, 130, 0xffffff)
    lcd.print('->', 250, 130, 0xffffff)
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <300  and (touch.read()[1]) >200 and  (touch.read()[1]) <300: 
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      return 0
    if mode==0:
      lcd.print("__", 30, 70, 0x00ff55)
      if x>23:
        x=23
      if x<0:
        x=0
      set_new_hour=x
    if mode==1:
      if x>59:
        x=0
      if x<1:
        x=1
      set_new_minute=x
      lcd.print("__", 130, 70, 0x00ff55)
      lcd.print("__", 30, 70, 0x000000)
    if mode>1:
      lcd.clear()
      mode=0
      
    lcd.print(set_new_hour, 30, 40, 0xffffff)
    lcd.print(':', 90, 40, 0xffffff)
    lcd.print(set_new_minute, 120, 40, 0xffffff)
    
    if set_new_hour>=12 and set_new_hour!=23 or set_new_hour==23:
      lcd.print(str("PM"), 180, 40, 0x199f44)
    if set_new_hour <12 and set_new_hour!=23 or set_new_hour==0:
      lcd.print(str("AM"), 180, 40, 0x199f44)
      
    if (touch.status())==1 and (touch.read()[0]) >40 and (touch.read()[0]) <90  and (touch.read()[1]) >150 and  (touch.read()[1]) <180:
      speaker.playWAV('/sd/button.wav')
      x=x-1
      lcd.clear()
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <300  and (touch.read()[1]) >150 and  (touch.read()[1]) <180:
      speaker.playWAV('/sd/button.wav')
      x=x+1
      lcd.clear()
    if (touch.status())==1 and (touch.read()[0]) >120 and (touch.read()[0]) <180  and (touch.read()[1]) >150 and  (touch.read()[1]) <180: 
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      mode=mode+1
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <100  and (touch.read()[1]) >200 and  (touch.read()[1]) <250:
       speaker.playWAV('/sd/button.wav')
       rtc.datetime((int(current_year), CURRENT_MONTH, CURRENT_DAY, 0, set_new_hour, set_new_minute, 0, 0))
       del x
       del set_new_hour
       del set_new_minute
       del mode
       del current_year
       gc.collect()
       return 1

  
  

def MENU():
  time_status=0
  date_status=0
  erase_status=0
  while True:
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('DATE', 50, 80, 0xffffff)
    lcd.print('TIME', 200, 80, 0xffffff)
    lcd.print('BACK', 10, 200, 0xffffff)
    lcd.print('ERASE',200, 140, 0xffffff)
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <100  and (touch.read()[1]) >200 and  (touch.read()[1]) <250:
      speaker.playWAV('/sd/button.wav')
      del time_status
      del date_status
      gc.collect()
      return 0
    if (touch.status())==1 and (touch.read()[0]) >40 and (touch.read()[0]) <150  and (touch.read()[1]) >100 and  (touch.read()[1]) <150: 
       speaker.playWAV('/sd/button.wav')
       lcd.clear()
       date_status=Date_set()
       if date_status==1:
         lcd.clear()
         lcd.font(lcd.FONT_DejaVu18)
         lcd.print(str("DATE UPDATED"), 100, 100, 0xffffff)
         speaker.playWAV('/sd/success.wav')
         wait(1)
         lcd.clear()
      
         
          
         
    if (touch.status())==1 and (touch.read()[0]) >190 and (touch.read()[0]) <300  and (touch.read()[1]) >90 and  (touch.read()[1]) <150:
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      time_status=Time_set()
      if time_status==1:
        lcd.clear()
        lcd.font(lcd.FONT_DejaVu18)
        lcd.print(str("TIME UPDATED"), 100, 100, 0xffffff)
        speaker.playWAV('/sd/success.wav')
        wait(1)
        lcd.clear()
     
         
    if (touch.status())==1 and (touch.read()[0]) >180 and (touch.read()[0]) <260  and (touch.read()[1]) >140 and  (touch.read()[1]) <200:
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      while True:
        lcd.print("ERASE HISTORY IN SD ?", 40, 100,  0xff2727)
        lcd.print('NO', 10, 200, 0xffffff)
        lcd.print('YES', 190, 200,  0xffffff)
        if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <100  and (touch.read()[1]) >200 and  (touch.read()[1]) <250:
          speaker.playWAV('/sd/button.wav')
          lcd.clear()
          break
        if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <350  and (touch.read()[1]) >200 and  (touch.read()[1]) <350:
          speaker.playWAV('/sd/button.wav')
          lcd.clear()
          lcd.print("ERASING...", 100, 100,  0xfffe38)
          wait(1)
          try:
            os.remove('/sd/history.text')
            with open('/sd/history.text', 'a') as fs:
              lcd.clear()
              lcd.print("DONE", 100, 100,0x18f830)
              wait(1)
              lcd.clear()
              break
          except:
            lcd.clear()
            while True:
              lcd.print('INSERT SD CARD & RESTART!!', 10, 100, 0xcc0000)
              
              
              
              
              
def POWER():
  charge_state=power.getChargeState()
  charge_voltage=power.getBatVoltage()
  charge_current=power.getBatCurrent()
  if charge_state == False and  charge_current < -1.0:    # plugged out discharge
    gc.collect()
    return -1
  if charge_state == True and charge_current > 0:  # plugged in charging
    gc.collect()
    return -2
  
  if charge_state == False and charge_current == -1.0:  # plugged in full charge
    gc.collect()
    return -3
    
  if charge_state == False and charge_current == 0.0: ## plugged in but cureent 0.0
    gc.collect()
    return -4
     
     
def DST_SETTING():
  speaker.playWAV('/sd/button.wav')
  dst_value=None
  dst_value= nvs.read_str('5')
  if (dst_value==str('0')):
    lcd.font(lcd.FONT_DefaultSmall)
    lcd.print('NOT AVAILABLE', 190, 170, 0xff0808)
  else:
    lcd.font(lcd.FONT_DefaultSmall)
    lcd.print('NOT AVAILABLE', 35, 170, 0xff0808)
    
    
  while True:
    set_new_hour=rtc.datetime()[4]
    set_new_minute=rtc.datetime()[5]
    set_new_day=rtc.datetime()[2]
    set_new_month=rtc.datetime()[1]
    set_new_year=str(rtc.datetime()[0])
    set_new_year=str(set_new_year[2])+str(set_new_year[3])
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('DST SELECTION', 80, 70, 0xffffff)
    lcd.print('BACKWARD',  20, 130, 0xff0808)
    lcd.print('[-1 HR]',  35, 150, 0xffffff)
    lcd.print('FORWARD', 190, 130, 0x08ff62)
    lcd.print('[+1 HR]',  210, 150, 0xffffff)
    lcd.print('BACK', 10, 200, 0xffffff)
    if (touch.status())==1 and (touch.read()[0]) >50 and (touch.read()[0]) <100  and (touch.read()[1]) >150 and  (touch.read()[1]) <170 and dst_value!=str('1'):
      speaker.playWAV('/sd/button.wav')
      set_new_hour-=1
      rtc.datetime((int(set_new_year), int(set_new_month), int(set_new_day), 0, int(set_new_hour), int(set_new_minute), 0, 0))
      nvs.write(str('5'), '1')
      return 1
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <250  and (touch.read()[1]) >150 and  (touch.read()[1]) <170 and dst_value!=str('0'):
      speaker.playWAV('/sd/button.wav')
      set_new_hour+=1
      rtc.datetime((int(set_new_year), int(set_new_month), int(set_new_day), 0, int(set_new_hour), int(set_new_minute), 0, 0))
      nvs.write(str('5'), '0')
      return 1
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <100  and (touch.read()[1]) >200 and  (touch.read()[1]) <250:
      rtc.datetime((int(set_new_year), int(set_new_month), int(set_new_day), 0, int(set_new_hour), int(set_new_minute), 0, 0))
      del set_new_hour
      del set_new_minute
      del set_new_day
      del set_new_month
      del set_new_year
      del dst_value
      gc.collect()
      return 0
    
  
  
     
     
     
  
  

def main():
  lcd.clear()
  gc.collect()
  RAM = gc.mem_free()
  global EMPLOYEE_ID
  global CURRENT_MINUTE
  global CURRENT_HOUR
  global CURRENT_YEAR
  global CURRENT_MONTH
  global CURRENT_DAY
  global CLOCK
  global TASK_NUMBERS
  global QR_CLOCK
  
  TIME_DATA=0
  REFRESH_SCREEN=1  # screen REFRESH RATE IN SEC
  VALID_ID=0  ## Validating EMPLOYEE_ID
  CHECK_CLOCK=0  # validating ALREADY CLOCKIN OR NOT
  ID_WRITE=0  # validating ID_WRITE TO ID FILE
  SD_WRITE=0
  SD_CHECK=0   ## 1 -> VALID , -1 -> NOT FOUND
  TASK_CHECK=0 # CHECKING YES OR NO
  TASK_FINISH=0 # CHECKING TASK FINISH OR NOT OR EXIT
  HISTORY_STATUS=0 #  CHECKING HISTORY STATUS 
  MENU_STATUS=0
  LOCK=0
  POWER_STATUS=0
  DST_STATUS=0
  
  
     
    
  while True:
    
    POWER_STATUS=POWER()
    if POWER_STATUS==-2 or  POWER_STATUS==-3 or  POWER_STATUS==-4:
      lcd.font(lcd.FONT_Default)
      lcd.print(str("Plugged"),220, 10, 0x00ff63)
      lcd.print(str("OUT"),285, 10, 0x000000) 
    else:
      lcd.font(lcd.FONT_Default)
      lcd.print(str("Plugged"),220, 10, 0xff0050)
      lcd.print(str("OUT"),285, 10, 0xff0050)
      
    CURRENT_MINUTE=rtc.datetime()[5]
    CURRENT_HOUR=rtc.datetime()[4]
    CURRENT_YEAR=rtc.datetime()[0]
    CURRENT_MONTH=rtc.datetime()[1]
    CURRENT_DAY=rtc.datetime()[2]
    lcd.font(lcd.FONT_DejaVu24)
    lcd.print('CIN', 65, 130, 0x009900)
    lcd.print('COUT', 190, 130, 0xcc0000)
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print(' --------------------------------------', 0, 180, 0x64e6e7)
    lcd.print("HISTORY", 220, 40,  0xffffff)
    lcd.print("SETTINGS", 110, 40,  0xffffff)
    lcd.print('-', 25, 10, 0xffffff)
    lcd.print('-', 63, 10, 0xffffff)
    lcd.print((rtc.datetime()[0]), 72, 10, 0xffffff) # year
    lcd.print(':', 30, 40, 0xffffff)
    lcd.print("MAC ID : ", 20, 200,  0xffffff)
    lcd.print((espnow.get_mac_addr()), 120, 200, 0xffffff)
    lcd.print("[ DST ]", 5, 70, 0xffe700) # year
    #lcd.print(str(RAM), 100, 70, 0xffe700) # year
    lcd.print("VER : 1.5", 220, 70,  0xffffff)
    
    if CURRENT_MONTH==1 or CURRENT_MONTH==2 or  CURRENT_MONTH ==3 or CURRENT_MONTH==4 or CURRENT_MONTH==5 or  CURRENT_MONTH ==6 or  CURRENT_MONTH ==7 or  CURRENT_MONTH ==8 or  CURRENT_MONTH==9:
      lcd.print("0", 35, 10, 0xffffff) # month
      lcd.print((rtc.datetime()[1]), 50, 10, 0xffffff) # month
    else:
      lcd.print((rtc.datetime()[1]), 35, 10, 0xffffff) 
    if CURRENT_DAY==1 or CURRENT_DAY ==2 or  CURRENT_DAY ==3 or CURRENT_DAY ==4 or  CURRENT_DAY ==5 or CURRENT_DAY ==6 or CURRENT_DAY ==7 or CURRENT_DAY==8 or CURRENT_DAY==9:
      lcd.print("0", 0, 10, 0xffffff) # day
      lcd.print((rtc.datetime()[2]), 10, 10, 0xffffff) # day
    else:
      lcd.print((rtc.datetime()[2]), 0, 10, 0xffffff) # day
    if CURRENT_MINUTE ==0 or CURRENT_MINUTE ==1 or CURRENT_MINUTE ==2 or  CURRENT_MINUTE ==3 or CURRENT_MINUTE==4 or  CURRENT_MINUTE==5 or CURRENT_MINUTE==6 or CURRENT_MINUTE ==7 or  CURRENT_MINUTE ==8 or CURRENT_MINUTE==9:
      lcd.print(str(CURRENT_MINUTE), 55, 40, 0xffffff) #40
      lcd.print("0", 40, 40, 0xffffff) #40
    else:
      lcd.print(str(CURRENT_MINUTE), 40, 40, 0xffffff) #40
    if CURRENT_HOUR ==0 or CURRENT_HOUR ==1 or CURRENT_HOUR==2 or CURRENT_HOUR==3 or CURRENT_HOUR==4 or CURRENT_HOUR==5 or CURRENT_HOUR==6 or CURRENT_HOUR==7 or CURRENT_HOUR==8 or CURRENT_HOUR==9:
      lcd.print(str(CURRENT_HOUR), 15, 40, 0xffffff) #40
      lcd.print("0", 0, 40, 0xffffff) #40
    else:
      lcd.print(str(CURRENT_HOUR), 0, 40, 0xffffff) #40
      
    if REFRESH_SCREEN==rtc.datetime()[6]:
       lcd.clear()
       
    if (touch.status()) == 1 and (touch.read()[0]) > 90 and (touch.read()[0]) < 115  and (touch.read()[1]) > 140 and  (touch.read()[1])  < 170 : # CIN
      CLOCK="00000001"
      QR_CLOCK="1"
      TASK_NUMBERS="-----------------------------"
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      SD_CHECK=SD()
      if SD_CHECK==1:
        lcd.clear()
        VALID_ID=EMP_KEYPAD()
        if VALID_ID==1:
          TIME_DATA=GET_TIME_DATE() ## getting VALID TIME & DATE
          lcd.clear()
          CHECK_CLOCK=CLOCK_IN_CHECK()
          if CHECK_CLOCK==1:
            lcd.clear()
            lcd.font(lcd.FONT_DejaVu18)
            lcd.print(str("CIN VERIFIED"), 80, 100,  0x18f830)  ## CIN CONFIRMED
            speaker.playWAV('/sd/success.wav')
            wait(1)
            lcd.clear()
            SD_CHECK=SD()
            if SD_CHECK==1:
              SD_WRITE=PATTERN_CIN_SAVE()
              if SD_WRITE==1:
                lcd.clear()
                lcd.font(lcd.FONT_DejaVu18)
                lcd.print("DATA SAVED", 100, 100,0xffffff)
                speaker.playWAV('/sd/success.wav')
                wait(1)
                lcd.clear()
                ID_WRITE=CLOCK_IN_WRITE()
                if ID_WRITE==1:
                  lcd.clear()
                  lcd.font(lcd.FONT_DejaVu18)
                  lcd.print("ID UPDATED", 80, 100,  0x18f830)
                  speaker.playWAV('/sd/success.wav')
                  wait(1)
                  lcd.clear()
                  EMPLOYEE_ID=None
                  
                else:
                  EMPLOYEE_ID=None
                  lcd.clear()
                  lcd.print("ERROR UPDATING", 80, 100,  0xff2727)
                  speaker.playWAV('/sd/warning.wav')
                  wait(20)
            elif SD_CHECK==-1:
              lcd.clear()
              while True:
                lcd.font(lcd.FONT_DejaVu18)
                lcd.print('INSERT SD CARD & RESTART!!', 10, 100, 0xcc0000)
      
          elif CHECK_CLOCK==0:
            lcd.clear()
            lcd.font(lcd.FONT_DejaVu18)
            lcd.print("ALREADY CLOCKED IN", 40, 100, 0xcc0000)
            speaker.playWAV('/sd/warning.wav')
            wait(2)
            lcd.clear()
          
        elif VALID_ID==0:  # back
          lcd.clear()
        elif VALID_ID==2:  # ALREADY clkin
          lcd.clear()
          lcd.font(lcd.FONT_DejaVu18)
          lcd.print("INVALID ID", 100, 100, 0xcc0000)
          speaker.playWAV('/sd/warning.wav')
          wait(2)
          lcd.clear()
  
      elif SD_CHECK==-1: # sd not found
        lcd.clear()
        while True:
          lcd.font(lcd.FONT_DejaVu18)
          lcd.print('INSERT SD CARD & RESTART!!', 10, 100, 0xcc0000)
                    
    if (touch.status()) == 1 and (touch.read()[0]) > 190 and (touch.read()[0]) < 230  and (touch.read()[1]) > 140 and  (touch.read()[1])  < 170 :
      CLOCK="00000000"
      QR_CLOCK="0"
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      SD_CHECK=SD()
      if SD_CHECK==1:
        lcd.clear()
        VALID_ID=EMP_KEYPAD()
        if VALID_ID==1:
          TIME_DATA=GET_TIME_DATE()
          lcd.clear()
          CHECK_CLOCK=CLOCK_IN_CHECK()
          if CHECK_CLOCK==0:
            lcd.clear()
            lcd.font(lcd.FONT_DejaVu18)
            lcd.print(str("COUT VERIFIED"), 80, 100,  0x18f830)  ## CIN CONFIRMED
            speaker.playWAV('/sd/success.wav')
            wait(1)
            TASK_CHECK=TASK_QN()
            if TASK_CHECK==1:
              TASK_NUMBERS="-----------YES-TO-ALL--------"
              SD_CHECK=SD()
              if SD_CHECK==1:
                lcd.clear()
                SD_WRITE=PATTERN_CIN_SAVE()
                if SD_WRITE==1:
                  lcd.clear()
                  lcd.font(lcd.FONT_DejaVu18)
                  lcd.print("DATA SAVED", 100, 100,0xffffff)
                  speaker.playWAV('/sd/success.wav')
                  wait(1)
                  lcd.clear()
                  ID_WRITE=UPDATE_ID()
                  if ID_WRITE==1:
                    lcd.clear()
                    lcd.font(lcd.FONT_DejaVu18)
                    lcd.print("ID UPDATED", 80, 100,  0x18f830)
                    speaker.playWAV('/sd/success.wav')
                    wait(1)
                    lcd.clear()
                    EMPLOYEE_ID=None
                    
                  else:
                    EMPLOYEE_ID=None
                    lcd.clear()
                    lcd.print("ERROR UPDATING", 80, 100,  0xff2727)
                    speaker.playWAV('/sd/warning.wav')
                    wait(20)

                else:
                  EMPLOYEE_ID=None
                  lcd.clear()
                  lcd.print("ERROR UPDATING", 80, 100,  0xff2727)
                  speaker.playWAV('/sd/warning.wav')
                  wait(20)
              
              else:
                lcd.clear()
                while True:
                  lcd.font(lcd.FONT_DejaVu18)
                  lcd.print('INSERT SD CARD & RESTART!!', 10, 100, 0xcc0000)

            elif TASK_CHECK==2:
              lcd.clear()
              TASK_FINISH=TASK_WINDOW()
              if TASK_FINISH==-1:
                lcd.clear()
                SD_WRITE=PATTERN_CIN_SAVE()
                if SD_WRITE==1:
                  lcd.clear()
                  lcd.font(lcd.FONT_DejaVu18)
                  lcd.print("DATA SAVED", 100, 100,0xffffff)
                  speaker.playWAV('/sd/success.wav')
                  wait(1)
                  ID_WRITE=UPDATE_ID()
                  lcd.clear()
                  if ID_WRITE==1:
                    lcd.clear()
                    lcd.font(lcd.FONT_DejaVu18)
                    lcd.print("ID UPDATED", 80, 100,  0x18f830)
                    speaker.playWAV('/sd/success.wav')
                    wait(1)
                    lcd.clear()
                    EMPLOYEE_ID=None
                  else:
                    EMPLOYEE_ID=None
                    lcd.clear()
                    lcd.print("ERROR UPDATING", 80, 100,  0xff2727)
                    speaker.playWAV('/sd/warning.wav')
                    wait(20)
                
              elif TASK_FINISH==0:  # BACK
                EMPLOYEE_ID=None
                lcd.clear()
                
                
            elif TASK_CHECK==0:
              lcd.clear()
              
          elif CHECK_CLOCK==1:
            lcd.clear()
            lcd.font(lcd.FONT_DejaVu18)
            lcd.print("NOT CLOCKED IN", 80, 100, 0xcc0000)
            speaker.playWAV('/sd/warning.wav')
            wait(2)
            lcd.clear()
            
        elif VALID_ID==0:
          lcd.clear()
        elif VALID_ID==2:
          lcd.clear()
          lcd.font(lcd.FONT_DejaVu18)
          lcd.print("INVALID ID", 100, 100, 0xcc0000)
          speaker.playWAV('/sd/warning.wav')
          wait(2)
          lcd.clear()
      elif SD_CHECK==-1:
        lcd.clear()
        while True:
          lcd.font(lcd.FONT_DejaVu18)
          lcd.print('INSERT SD CARD & RESTART!!', 10, 100, 0xcc0000)
        
    if (touch.status())==1 and (touch.read()[0]) > 240 and (touch.read()[0]) <280  and (touch.read()[1]) >70 and  (touch.read()[1]) <100:
       speaker.playWAV('/sd/button.wav')
       SD_CHECK=SD()
       if SD_CHECK==1:
         lcd.clear()
         HISTORY_STATUS=HISTORY()
         if HISTORY_STATUS==-1:
           lcd.clear()
         elif HISTORY_STATUS==0:
           lcd.clear()
           lcd.print('NO RECORD', 100, 100, 0xcc0000)
           speaker.playWAV('/sd/warning.wav')
           wait(1)
           lcd.clear()
       else:
         while True:
           lcd.font(lcd.FONT_DejaVu18)
           lcd.print('INSERT SD CARD & RESTART!!', 10, 100, 0xcc0000)
           
    if (touch.status())==1 and (touch.read()[0]) >130 and (touch.read()[0]) <175  and (touch.read()[1]) >70 and  (touch.read()[1]) <100:
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      LOCK=PASSWORD_WINDOW()
      if LOCK==1:
        lcd.clear()
        lcd.print(str("success"), 100, 100, 0xffffff)
        speaker.playWAV('/sd/success.wav')
        wait(1)
        lcd.clear()
        MENU_STATUS=MENU()
        if MENU_STATUS==0:
          lcd.clear();
      

      elif LOCK==-1:
        lcd.clear()
        lcd.print("WRONG!!", 100, 100,0xff2727)                                # wrong password
        speaker.playWAV('/sd/warning.wav')
        wait(1)
        lcd.clear()
      elif LOCK==0:
        lcd.clear()
        
    if (touch.status()) == 1 and (touch.read()[0]) > 20 and (touch.read()[0]) < 70  and (touch.read()[1]) > 100 and  (touch.read()[1])  < 110:
      lcd.clear()
      DST_STATUS=DST_SETTING()
      if DST_STATUS==1:
        lcd.clear()
        lcd.print('DST UPDATED', 100, 100, 0xffffff)
        wait(1)
        lcd.clear()
      elif DST_STATUS==0:
        lcd.clear()
        
        
      
      
      
      


power.setVibrationIntensity(5)
lcd.font(lcd.FONT_DejaVu40)
screen.set_screen_brightness(100)
lcd.print('C', 100, 100,0xe937ff)
wait(2)
lcd.print('I', 130, 100, 0xff0d0d)
wait(2)
lcd.print('C', 145, 100, 0xfff60b)
wait(2)
lcd.print('O', 175, 100, 0xb1cfff)
wait(1)
lcd.font(lcd.FONT_DefaultSmall)
lcd.print('Employee Interactive Voice Response System', 30, 150, 0xffffff)
speaker.playWAV('/sd/sd_ok.wav')
wait(1)
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
lcd.clear()
lcd.font(lcd.FONT_DejaVu18)
lcd.print('SD FOUND', 100, 100, 0xffffff)
speaker.playWAV('/sd/sd_ok.wav')
wait_ms(200)
login_id=None
DEVICE_CHECK= str(nvs.read_str('2'))  ## CHECKING NEW DEVICE OR NOT
lcd.clear()
if DEVICE_CHECK=="1":
  main()
else:
  lcd.clear()
  login_id=PASSWORD_WINDOW()
  if login_id==1:
    lcd.print("DEVICE ACTIVATED", 65, 100, 0xaaff82)
    speaker.playWAV('/sd/welcome.wav')
    wait(2)
    lcd.clear()
    lcd.print("| WELCOME |", 90, 100, 0xffffff)
    wait(2)
    lcd.clear()
    lcd.print("CREATING FILES...", 0, 100, 0xffffff)
    wait(3)
    rtc.datetime((21, 01, 02, 0, 14, 15, 0, 0))
    with open('/sd/id.text', 'a') as fs:
      lcd.clear()
      lcd.print("ID FILE CREATED", 0, 100, 0xffffff)
      wait_ms(100)
      lcd.clear()
    with open('/sd/date.text','a')as fs:
      lcd.clear()
      lcd.print("DATE FILE CREATED", 0, 100, 0xffffff)
      wait_ms(100)
      lcd.clear()
    with open('/sd/history.text', 'a') as fs:
      lcd.clear()
      lcd.print("HISTORY FILE CREATED", 0, 100, 0xffffff)
      wait_ms(100)
      lcd.clear()
    lcd.print("Files created", 0, 80, 0xffffff)
    lcd.print("Don't replace sd for this device", 0, 100, 0xffffff)
    wait(5)
    nvs.write_str(str('2'), '1')
  else:
    lcd.clear()
    while True:
      lcd.print("WRONG !!", 100, 100, 0xffffff)
      lcd.print("RESTART AGAIN", 100, 150, 0xff2727)
      speaker.playWAV('/sd/warning.wav')
      wait(3)
      lcd.clear()
  main()   
    
      
    
      
     
       
   
    
  
    
      
 
 
    
   
    
     
   
      
      
    
     
    
      
   
      
  
      
      
    
      
    
  
  
  
  
  
  
  
  
  
  
  
  
 
 
  
    
 
  
  
 
    
    
  
 
 





  

 





