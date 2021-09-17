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
       return 1
     if (touch.status())==1 and (touch.read()[0]) >0 and (touch.read()[0]) <60  and (touch.read()[1]) >170 and  (touch.read()[1]) <200:
       return 2
       
      
          
          
          
          
          

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
  while True:
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
    lcd.print(str(RAM), 100, 70, 0xffe700) # year
    
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

DEVICE_CHECK= str(nvs.read_str('2'))  ## CHECKING NEW DEVICE OR NOT
lcd.clear()
if DEVICE_CHECK=="1":
  main()
else:
  while True:
    lcd.clear()
    lcd.font(lcd.FONT_DefaultSmall)
    lcd.print('NEW DEVICE', 100, 100, 0xffffff)
    lcd.print('KINDLY UPLOAD FIRMWARE IN OLD DEVICE', 0, 150, 0xffffff)
    lcd.print('THIS IS TESTING MODE', 0, 150, 0xffffff)
    
    
  
 
 





  

 
 


