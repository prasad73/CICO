from m5stack import *
from m5stack_ui import *
from uiflow import *
import espnow
import wifiCfg
import nvs


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x000000)

wifiCfg.wlan_ap.active(True)
wifiCfg.wlan_sta.active(True)
espnow.init()

global str


sd = None
string=None
list_length=0




login_id=""
num_id1=""
num_id2=""
num_id3=""
num_id4=""
num_id5=""
num_id6=""
num_id7=""
num_id8=""


login_flag=1
Activate_status=0
home_status=0
Emp_id_status=0

Hour=None
Min=None
Day=None
Month=None
Year=None

clk=0


login_password="01"
sd_data=None
id_count=0
data_file = []
clockout_list=[]

new_day=0
new_month=0
new_year=0

new_hour=0
new_minute=0




Final_code=0
Final_code_len=0








  
  



def Task(Emp_ID):
  lcd.clear()
  code1=None
  code2=None
  code3=None
  code4=None
  code5=None
  code6=None
  code7=None
  code8=None
  code9=None
  code10=None
  code11=None
  code12=None
  code13=None
  code14=None
  code15=None
  code16=None
  code17=None
  code18=None
  code19=None
  code20=None
  code21=None
  code22=None
  code23=None
  code24=None
  code25=None
  code26=None
  code27=None
  code28=None
  code29=None
 
  answer_code=0
  global Final_code
  j=0
  var2=None
  
  while answer_code==0:
   
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
      j=j+1#
      var2='0'
     
    if (touch.status())==1 and (touch.read()[0]) >100 and (touch.read()[0]) <130  and (touch.read()[1]) >75 and  (touch.read()[1]) <90:
      speaker.playWAV('/sd/button.wav')
      j=j+1#
      var2='1'
    
    if (touch.status())==1 and (touch.read()[0]) >170 and (touch.read()[0]) <200  and (touch.read()[1]) >75 and  (touch.read()[1]) <100:
      speaker.playWAV('/sd/button.wav')
      j=j+1#
      var2='2'
     
   
    if (touch.status())==1 and (touch.read()[0]) >250 and (touch.read()[0]) <280  and (touch.read()[1]) >75 and  (touch.read()[1]) <100:
      speaker.playWAV('/sd/button.wav')
      j=j+1#
      var2='3'
     
     
     
     
    if (touch.status())==1 and (touch.read()[0]) >0 and (touch.read()[0]) <80  and (touch.read()[1]) >120 and  (touch.read()[1]) <140:
      speaker.playWAV('/sd/button.wav')
      j=j+1#
      var2='4'
     

   
    if (touch.status())==1 and (touch.read()[0]) >90 and (touch.read()[0]) <130  and (touch.read()[1]) >120 and  (touch.read()[1]) <140:
      speaker.playWAV('/sd/button.wav')
      j=j+1#
      var2='5'
      
     
     
   
    if (touch.status())==1 and (touch.read()[0]) >165 and (touch.read()[0]) <195  and (touch.read()[1]) >120 and  (touch.read()[1]) <140:
      speaker.playWAV('/sd/button.wav')
      j=j+1#
      var2='6'
     
     
     
   
    if (touch.status())==1 and (touch.read()[0]) >220 and (touch.read()[0]) <300  and (touch.read()[1]) >120 and  (touch.read()[1]) <140:
      speaker.playWAV('/sd/button.wav')
      j=j+1#
      var2='7'
      
   
   
   
    if (touch.status())==1 and (touch.read()[0]) >0 and (touch.read()[0]) <80  and (touch.read()[1]) >170 and  (touch.read()[1]) <200:
      speaker.playWAV('/sd/button.wav')
      j=j+1#
      var2='8'
     
      
     
     
     
    if (touch.status())==1 and (touch.read()[0]) >100 and (touch.read()[0]) <130  and (touch.read()[1]) >170 and  (touch.read()[1]) <200:
      speaker.playWAV('/sd/button.wav')
      j=j+1#
      var2='9'
      
    
     
    if (touch.status())==1 and (touch.read()[0]) >155 and (touch.read()[0]) <200  and (touch.read()[1]) >170 and  (touch.read()[1]) <200:
      speaker.playWAV('/sd/button.wav')
      j=j+1#
      var2=','
     
      
     
    
    
    if (touch.status())==1 and (touch.read()[0]) >50 and (touch.read()[0]) <70  and (touch.read()[1]) >200 and  (touch.read()[1]) <250:
      speaker.playWAV('/sd/button.wav')
      j=0
      lcd.clear()
      answer_code=1
      Emp_id_status=0
      home_screen()                                            ## back
     
    
      
    if (touch.status())==1 and (touch.read()[0]) >130 and (touch.read()[0]) <200  and (touch.read()[1]) >200 and  (touch.read()[1]) <260:
      speaker.playWAV('/sd/button.wav')
     
      
      lcd.clear()
      code1=None
      code2=None
      code3=None
      code4=None
      code5=None
      code6=None
      code7=None
      code8=None
      code9=None
      code10=None
      code11=None
      code12=None
      code13=None
      code14=None
      code15=None
      code16=None
      code17=None
      code18=None
      code19=None
      code20=None
      code21=None
      code22=None
      code23=None
      code24=None
      code25=None
      code26=None
      code27=None
      code28=None
      code29=None
      j=0
      #id_check_clkout(Emp_ID)
      #return Final_code
      #answer_code=1
      
     
    
    
     
     
    if (touch.status())==1 and (touch.read()[0]) >235 and (touch.read()[0]) <290  and (touch.read()[1]) >170 and  (touch.read()[1]) <200:
      speaker.playWAV('/sd/button.wav')
      if code1==None:
        
        lcd.clear()
        lcd.print(str("NO TASk CODE FOUND.!"), 40, 100, 0xffffff)
        speaker.playWAV('/sd/warning.wav')
        wait(1)
        lcd.clear()
        Task(Emp_ID)
        
      if code1==None:
        code1="*"
      if code2==None:
        code2="*"
      if code3==None:
        code3="*"
      if code4==None:
        code4="*"
      if code5==None:
        code5="*"
      if code6==None:
        code6="*"
      if code7==None:
        code7="*"
      if code8==None:
        code8="*"
      if code9==None:
        code9="*"
      if code10==None:
        code10="*"
      if code11==None:
        code11="*"
      if code12==None:
        code12="*"
      if code13==None:
        code13="*"
      if code14==None:
        code14="*"
      if code15==None:
        code15="*"
      if code16==None:
        code16="*"
      if code17==None:
        code17="*"
      if code18==None:
        code18="*"
      if code19==None:
        code19="*"
      if code20==None:
        code20="*"
      if code21==None:
        code21="*"
      if code22==None:
        code22="*"
      if code23==None:
        code23="*"
      if code24==None:
        code24="*"
      if code25==None:
        code25="*"
      if code26==None:
        code26="*"
      if code27==None:
        code27="*"
      if code28==None:
        code28="*"
      if code29==None:
        code29="*"
        
      
      
      Final_code=str(code1)+str(code2)+str(code3)+str(code4)+str(code5)+str(code6)+str(code7)+str(code8)+str(code9)+str(code10)+str(code11)+str(code12)+str(code13)+str(code14)+str(code15)+str(code16)+str(code17)+str(code18)+str(code19)+str(code20)+str(code21)+str(code22)+str(code23)+str(code24)+str(code25)+str(code26)+str(code27)+str(code28)+str(code29)               
      #lcd.print(str(Final_code), 0, 100, 0xffffff)
      #wait(3)
      
      j=0
      id_check_clkout(Emp_ID)
      answer_code=1
      return Final_code
     
      
      
     
      
      
    
     
      
      
      
    if j==1:
      code1=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code1, 0, 10,  0x66ff99)
    if j==2:
      code2=var2
      lcd.print(code2, 10, 10,  0x66ff99)
     
    if j==3:
      code3=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code3, 20, 10,  0x66ff99)
      
    if j==4:
      code4=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code4, 30, 10,  0x66ff99)
    if j==5:
      code5=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code5, 40, 10,  0x66ff99)
      
    if j==6:
      code6=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code6, 50, 10,  0x66ff99)
    if j==7:
      code7=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code7, 60, 10,  0x66ff99)
    if j==8:
      code8=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code8, 70, 10,  0x66ff99)
     
    if j==9:
      code9=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code9, 80, 10,  0x66ff99)
    if j==10:
      code10=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code10, 90, 10,  0x66ff99)
    if j==11:
      code11=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code11, 100, 10,  0x66ff99)
      
    if j==12:
      code12=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code12, 110, 10,  0x66ff99)
    if j==13:
      code13=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code13, 120, 10,  0x66ff99)
    if j==14:
      code14=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code14, 130, 10,  0x66ff99)
      
    if j==15:
       code15=var2
       lcd.font(lcd.FONT_DejaVu18)
       lcd.print(code15, 140, 10,  0x66ff99)
    if j==16:
       code16=var2
       lcd.font(lcd.FONT_DejaVu18)
       lcd.print(code16, 150, 10,  0x66ff99)
    if j==17:
      code17=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code17, 160, 10,  0x66ff99)
     
    if j==18:
      code18=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code18, 170, 10,  0x66ff99)
    if j==19:
      code19=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code19, 180, 10,  0x66ff99)
    if j==20:
      code20=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code20, 190, 10,  0x66ff99)
     
    if j==21:
      code21=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code21, 200, 10,  0x66ff99)
    if j==22:
      code22=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code22, 210, 10,  0x66ff99)
    if j==23:
      code23=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code23, 220, 10,  0x66ff99)
      
    if j==24:
      code24=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code24, 230, 10,  0x66ff99)
    if j==25:
      code25=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code25, 240, 10,  0x66ff99)
    if j==26:
      code26=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code26, 250, 10,  0x66ff99)
      
    if j==27:
      code27=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code27, 260, 10,  0x66ff99)
    if j==28:
      code28=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code28, 270, 10,  0x66ff99)
    if j==29:
      code29=var2
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(code29, 280, 10,  0x66ff99)
    if j==30:
      lcd.print(" ", 290, 10,  0x66ff99)
  
  
    
  
    




def pass_window(pass_status):
  login_id=None
  num_id1=""
  num_id2=""
  num_id3=""
  num_id4=""
  num_id5=""
  num_id6=""
  num_id7=""
  num_id8=""
  var=None
  i=0
  while pass_status==1:
    
    
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('ENTER ID', 0, 20,  0xffffff)
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
      #num_id1="0"
      var='0'
      i=i+1
     
      
    if (touch.status())==1 and (touch.read()[0]) >100 and (touch.read()[0]) <150  and (touch.read()[1]) >90 and  (touch.read()[1]) <115:
      
      speaker.playWAV('/sd/button.wav')                                   #1
      lcd.print('1', 115, 75, 0xffffff)
      #num_id2="1"
      var='1'
      i=i+1
      
      
     
     
    if (touch.status())==1 and (touch.read()[0]) >160 and (touch.read()[0]) <250  and (touch.read()[1]) >90 and  (touch.read()[1]) <115:
      speaker.playWAV('/sd/button.wav')                                              #2
      lcd.print('2', 185, 75, 0xffffff) 
      #num_id3="2"
      var='2'
      i=i+1
     
     
    if (touch.status())==1 and (touch.read()[0]) >220 and (touch.read()[0]) <300  and (touch.read()[1]) >90 and  (touch.read()[1]) <115:
      speaker.playWAV('/sd/button.wav')                                          
      lcd.print('3', 265, 75, 0xffffff) 
      #num_id4="3"
      var='3'
      i=i+1
     
      
      
    
    if (touch.status())==1 and (touch.read()[0]) >50 and (touch.read()[0]) <90  and (touch.read()[1]) >125 and  (touch.read()[1]) <170:
      speaker.playWAV('/sd/button.wav')
      lcd.print('4', 45, 140, 0xffffff) 
      #num_id5="4"
      var='4'
      i=i+1
      
      
      
      
    if (touch.status())==1 and (touch.read()[0]) >100 and (touch.read()[0]) <180  and (touch.read()[1]) >125 and  (touch.read()[1]) <180:
      speaker.playWAV('/sd/button.wav')
      lcd.print('5', 115, 140, 0xffffff) 
      #num_id6="5"
      var='5'
      i=i+1
      
      
    if (touch.status())==1 and (touch.read()[0]) >155 and (touch.read()[0]) <230  and (touch.read()[1]) >125 and  (touch.read()[1]) <185:
      
      speaker.playWAV('/sd/button.wav')
      lcd.print('6', 185, 140, 0xffffff) 
      #num_id7="6"
      var='6'
      i=i+1
      
      
      
      
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <290  and (touch.read()[1]) >125 and  (touch.read()[1]) <185:
      
      speaker.playWAV('/sd/button.wav')
      lcd.print('7', 265, 140, 0xffffff) 
      #num_id8="7"
      var='7'
      i=i+1
      
      
    
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <300  and (touch.read()[1]) >200 and  (touch.read()[1]) <300:#next
      speaker.playWAV('/sd/button.wav')
      
      lcd.clear()
      login_id=str(num_id1)+str(num_id2)+str(num_id3)+str(num_id4)+str(num_id5)+str(num_id6)+str(num_id7)  # valid password
      lcd.print(login_id, 150, 200, 0xffffff)
      if login_password==login_id:
        lcd.print(str("Plz wait.."), 100, 100, 0xffffff)
        wait(1)
        pass_status=0
      else:
        lcd.print("WRONG!!", 100, 100, 0xffffff)                                # wrong password
        speaker.playWAV('/sd/warning.wav')
        
        wait(4)
        lcd.clear()
        pass_status=0
        home_status=1
        num_id1=None
        num_id2=None
        num_id3=None
        num_id4=None
        num_id5=None
        num_id6=None
        num_id7=None
        num_id8=None
        home_screen()
        
       
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <100  and (touch.read()[1]) >200 and  (touch.read()[1]) <250:
        speaker.playWAV('/sd/button.wav')
       
        pass_status=0                 # back
        home_status=1
        num_id1=None
        num_id2=None
        num_id3=None
        num_id4=None
        num_id5=None
        num_id6=None
        num_id7=None
        num_id8=None
        home_screen()
        
    if i==1:
          num_id1=var
          lcd.font(lcd.FONT_DejaVu24)
          lcd.print('*', 150, 20,  0x66ff99)
    if i==2:
          num_id2=var
          lcd.font(lcd.FONT_DejaVu24)
          lcd.print('*', 170, 20, 0x66ff99)
    if i==3:
          num_id3=var
          lcd.font(lcd.FONT_DejaVu24)
          lcd.print('*', 190, 20, 0x66ff99)
    if i==4:
          num_id4=var
          lcd.font(lcd.FONT_DejaVu24)
          lcd.print('*', 210, 20, 0x66ff99)
          #lcd.print(" ", 260, 20, 0x66ff99)
    if i==5:
          num_id5=var
          lcd.font(lcd.FONT_DejaVu24)
          lcd.print('*', 230, 20, 0x66ff99)
          
    if i==6:
          num_id6=var
          lcd.font(lcd.FONT_DejaVu24)
          lcd.print('*', 250, 20, 0x66ff99)

    if i==7:
         num_id7=var
         lcd.font(lcd.FONT_DejaVu24)
         lcd.print('*', 270, 20, 0x66ff99)
          
         
    if i==8:
         num_id8=var
         lcd.font(lcd.FONT_DejaVu24)
         lcd.print('*', 290, 20, 0x66ff99)
          
    if i==9:
         num_id9=var
         lcd.font(lcd.FONT_DejaVu24)
         lcd.print('*', 300, 20, 0x66ff99)
    





def data_formatting(Emp_ID,Day,Month,Year,Hour,Min,clk, mac_id_hex):
  task_value=None
  task_status=0
  
  if clk==1:
    id_check_clkin(Emp_ID)
    task_value=str("00000000000000000000000000000")
  if clk==0:
    while task_status==0:
      lcd.print('DID YOU COMPLETE ALL TASKS', 0, 100, 0xffffff)
      lcd.print('NO', 30, 160, 0xff0808)
      lcd.print('YES TO ALL', 150, 160, 0x08ff62)
      if (touch.status())==1 and (touch.read()[0]) >150 and (touch.read()[0]) <220  and (touch.read()[1]) >170 and  (touch.read()[1]) <200: # yes
        
        speaker.playWAV('/sd/button.wav')
        task_value=str("00000000000000000000000000000")
        id_check_clkout(Emp_ID)
        task_status=1
      
      
      
      
      
      if (touch.status())==1 and (touch.read()[0]) >0 and (touch.read()[0]) <60  and (touch.read()[1]) >170 and  (touch.read()[1]) <200: # no
        
        lcd.clear()
        speaker.playWAV('/sd/button.wav')
        lcd.print("ENTER TASK CODES", 65, 100,  0xffffff)
        wait(3)
        task_value=Task(Emp_ID)
        task_status=1
        
    
  read_tc1_tsk    =task_value[0]
  read_tc2_tsk    =task_value[1]
  read_tc3_tsk    =task_value[2]
  read_tc4_tsk    =task_value[3]
  read_tc5_tsk    =task_value[4]
  read_tc6_tsk    =task_value[5]
  read_tc7_tsk    =task_value[6]
  read_tc8_tsk    =task_value[7]
  read_tc9_tsk    =task_value[8]
  read_tc10_tsk   =task_value[9]
  read_tc11_tsk   =task_value[10]
  read_tc12_tsk   =task_value[11]
  read_tc13_tsk   =task_value[12]
  read_tc14_tsk   =task_value[13]
  read_tc15_tsk   =task_value[14]
  read_tc16_tsk   =task_value[15]
  read_tc17_tsk   =task_value[16]
  read_tc18_tsk   =task_value[17]
  read_tc19_tsk   =task_value[18]
  read_tc20_tsk   =task_value[19]
  read_tc21_tsk   =task_value[20]
  read_tc22_tsk   =task_value[21]
  read_tc23_tsk   =task_value[22]
  read_tc24_tsk   =task_value[23]
  read_tc25_tsk   =task_value[24]
  read_tc26_tsk   =task_value[25]
  read_tc27_tsk   =task_value[26]
  read_tc28_tsk   =task_value[27]
  read_tc29_tsk   =task_value[28]
  
  
  if read_tc1_tsk=="*":
    read_tc1_tsk =" "
    
  if read_tc2_tsk=="*":
    read_tc2_tsk =" "
    
  if read_tc3_tsk=="*":
    read_tc3_tsk =" "
    
  if read_tc4_tsk=="*":
    read_tc4_tsk =" "
    
  if read_tc5_tsk=="*":
    read_tc5_tsk =" "
    
  if read_tc6_tsk=="*":
    read_tc6_tsk =" "
    
  if read_tc7_tsk=="*":
    read_tc7_tsk =" "
    
  if read_tc8_tsk=="*":
    read_tc8_tsk =" "
    
  if read_tc9_tsk=="*":
    read_tc9_tsk =" "
    
  if read_tc10_tsk=="*":
    read_tc10_tsk =" "
    
  if read_tc11_tsk=="*":
    read_tc11_tsk =" "
    
  if read_tc12_tsk=="*":
    read_tc12_tsk =" "
    
  if read_tc13_tsk=="*":
    read_tc13_tsk =" "
    
  if read_tc14_tsk=="*":
    read_tc14_tsk =" "
    
  if read_tc15_tsk=="*":
    read_tc15_tsk =" "
    
  if read_tc16_tsk=="*":
    read_tc16_tsk =" "
    
  if read_tc17_tsk=="*":
    read_tc17_tsk =" "
    
  if read_tc18_tsk=="*":
    read_tc18_tsk =" "
    
  if read_tc19_tsk=="*":
    read_tc19_tsk =" "
    
  if read_tc20_tsk=="*":
    read_tc20_tsk =" "
    
  if read_tc21_tsk=="*":
    read_tc21_tsk =" "
    
  if read_tc22_tsk=="*":
    read_tc22_tsk =" "
    
  if read_tc23_tsk=="*":
    read_tc23_tsk =" "
    
  if read_tc24_tsk=="*":
    read_tc24_tsk =" "
    
  if read_tc25_tsk=="*":
    read_tc25_tsk =" "
    
  if read_tc26_tsk=="*":
    read_tc26_tsk =" "
    
  if read_tc27_tsk=="*":
    read_tc27_tsk =" "
    
  if read_tc28_tsk=="*":
    read_tc28_tsk =" "
  if read_tc29_tsk=="*":
    read_tc29_tsk =" "
    
  task_value_dsp=str(read_tc1_tsk)+str(read_tc2_tsk)+str(read_tc3_tsk)+str(read_tc4_tsk)+str(read_tc5_tsk)+str(read_tc6_tsk)+str(read_tc7_tsk)+str(read_tc8_tsk)+str(read_tc9_tsk)+str(read_tc10_tsk)+str(read_tc11_tsk)+str(read_tc12_tsk)+str(read_tc13_tsk)+str(read_tc14_tsk)+str(read_tc15_tsk)+str(read_tc16_tsk)+str(read_tc17_tsk)+str(read_tc18_tsk)+str(read_tc19_tsk)+str(read_tc20_tsk)+str(read_tc21_tsk)+str(read_tc22_tsk)+str(read_tc23_tsk)+str(read_tc24_tsk)+str(read_tc25_tsk)+str(read_tc26_tsk) +str(read_tc27_tsk)+str(read_tc28_tsk)+str(read_tc29_tsk)  
    
  
  if task_value=="00000000000000000000000000000":
    
    task_value_dsp="YES TO ALL"
    
   
  task_status=1
  int_Emp=int(Emp_ID,10)
  hex_emp=hex(int_Emp)[2:]
  qr_emp=hex_emp
  length_emp=len(hex_emp)

  hex_day=hex(Day)[2:]
  qr_day=hex_day
  length_day=len(hex_day)
  
  hex_month=hex(Month)[2:]
  qr_month=hex_month
  length_month=len(hex_month)
  
  hex_year=hex(Year)[2:]
  qr_year=hex_year
  length_year=len(hex_year)
  
  hex_hour=hex(Hour)[2:]
  qr_hour=hex_hour
  length_hour=len(hex_hour)
  
  hex_min=hex(Min)[2:]
  qr_min=hex_min
  length_min=len(hex_min)
  
  
  hex_clk=hex(clk)[2:]
  qr_clk=hex_clk
  length_clk=len(hex_clk)
  
  qr_mac_id_hex=mac_id_hex
  
  if length_clk==1:
    hex_clk="0"+"0"+"0"+"0"+"0"+"0"+"0"+hex_clk # 8
  
  
  
  if length_emp==1:# length is 1
    hex_emp="0"+"0"+"0"+"0"+"0"+"0"+"0"+hex_emp # 7+1
           
  if length_emp==2:       
    hex_emp="0"+"0"+"0"+"0"+"0"+"0"+hex_emp #  6+2
           
  if length_emp==3:
    hex_emp="0"+"0"+"0"+"0"+"0"+hex_emp # 5+3
      
  if length_emp==4:
    hex_emp="0"+"0"+"0"+"0"+hex_emp   #4+4
        
  if length_emp==5:
    hex_emp="0"+"0"+"0"+hex_emp #3+5
    
  if length_emp==6:
    hex_emp="0"+"0"+hex_emp #2+6
    
  if length_emp==7:
    hex_emp="0"+hex_emp #1+6
    
    
    
  if length_day==1:# length is 1
    hex_day="0"+"0"+"0"+"0"+"0"+"0"+"0"+hex_day # 7+1
           
  if length_day==2:       
    hex_day="0"+"0"+"0"+"0"+"0"+"0"+hex_day #  6+2
           
  if length_day==3:
    hex_day="0"+"0"+"0"+"0"+"0"+hex_day # 5+3
      
  if length_day==4:
    hex_day="0"+"0"+"0"+"0"+hex_day   #4+4
        
  if length_day==5:
    hex_day="0"+"0"+"0"+hex_day #3+5
    
  if length_day==6:
    hex_day="0"+"0"+hex_day #2+6
    
  if length_day==7:
    hex_day="0"+hex_day #1+6
    
    
  if length_month==1:# length is 1
    hex_month="0"+"0"+"0"+"0"+"0"+"0"+"0"+hex_month # 7+1
           
  if length_month==2:       
    hex_month="0"+"0"+"0"+"0"+"0"+"0"+hex_month#  6+2
           
  if length_month==3:
    hex_month="0"+"0"+"0"+"0"+"0"+hex_month # 5+3
      
  if length_month==4:
    hex_month="0"+"0"+"0"+"0"+hex_month   #4+4
        
  if length_month==5:
    hex_month="0"+"0"+"0"+hex_month#3+5
    
  if length_month==6:
    hex_month="0"+"0"+hex_month #2+6
    
  if length_month==7:
    hex_month="0"+hex_month #1+6
    
    
  if length_year==1:# length is 1
    hex_year="0"+"0"+"0"+"0"+"0"+"0"+"0"+hex_year # 7+1
           
  if length_year==2:       
    hex_year="0"+"0"+"0"+"0"+"0"+"0"+hex_year#  6+2
           
  if length_year==3:
    hex_year="0"+"0"+"0"+"0"+"0"+hex_year # 5+3
      
  if length_year==4:
    hex_year="0"+"0"+"0"+"0"+hex_year   #4+4
        
  if length_year==5:
    hex_year="0"+"0"+"0"+hex_year#3+5
    
  if length_year==6:
    hex_year="0"+"0"+hex_year #2+6
    
  if length_year==7:
    hex_year="0"+hex_year #1+6
    
  
  if length_hour==1:# length is 1
    hex_hour="0"+"0"+"0"+"0"+"0"+"0"+"0"+hex_hour # 7+1
           
  if length_hour==2:       
    hex_hour="0"+"0"+"0"+"0"+"0"+"0"+hex_hour#  6+2
           
  if length_hour==3:
    hex_hour="0"+"0"+"0"+"0"+"0"+hex_hour # 5+3
      
  if length_hour==4:
    hex_hour="0"+"0"+"0"+"0"+hex_hour   #4+4
        
  if length_hour==5:
    hex_hour="0"+"0"+"0"+hex_hour#3+5
    
  if length_hour==6:
    hex_hour="0"+"0"+hex_hour #2+6
    
  if length_hour==7:
    hex_hour="0"+hex_hour #1+6
    
  
  
  if length_min==1:# length is 1
    hex_min="0"+"0"+"0"+"0"+"0"+"0"+"0"+hex_min # 7+1
           
  if length_min==2:       
    hex_min="0"+"0"+"0"+"0"+"0"+"0"+hex_min#  6+2
           
  if length_min==3:
    hex_min="0"+"0"+"0"+"0"+"0"+hex_min # 5+3
      
  if length_min==4:
    hex_min="0"+"0"+"0"+"0"+hex_min #4+4
        
  if length_min==5:
    hex_min="0"+"0"+"0"+hex_min #3+5
    
  if length_hour==6:
    hex_hour="0"+"0"+hex_hour #2+6
    
  if length_hour==7:
    hex_hour="0"+hex_hour #1+6
    
    
  sd_data=hex_emp+hex_day+hex_month+hex_year+hex_hour+hex_min+hex_clk+mac_id_hex+str(task_value)
  qr_sd_data=qr_emp+"."+qr_day+"."+qr_month+"."+qr_year+"."+qr_hour+"."+qr_min+"."+qr_clk+"."+qr_mac_id_hex
  lcd.clear()
  lcd.font(lcd.FONT_DejaVu18)
  lcd.print("Please write down or scan QR ", 0, 20,0x00cccc)
  lcd.font(lcd.FONT_Default)
  lcd.print(str(qr_sd_data), 0, 60,0xffffff)
  lcd.font(lcd.FONT_DejaVu24)
  lcd.print("OK", 140, 170,0xFFFFFF)
  lcd.qrcode(qr_sd_data, 0, 110, 130)
  if clk==0:
    lcd.font(lcd.FONT_Default)
    lcd.print(str(task_value_dsp), 0, 80,0xffffff)
    
  
  
  
  
  exit=1
  while exit==1:
    if (touch.status())==1 and (touch.read()[0]) >120 and (touch.read()[0]) <200  and (touch.read()[1]) >150 and  (touch.read()[1]) <230:
      speaker.playWAV('/sd/button.wav')
      power.setVibrationEnable(True)
      wait_ms(100)
      power.setVibrationEnable(False)
      sd_write(sd_data+"\n")
      lcd.clear()
      lcd.font(lcd.FONT_DejaVu18)
      
      lcd.print("DATA SAVED", 100, 100,0xffffff)
      #speaker.playWAV("/sd/success.wav", rate=44100, dataf=speaker.F16B)
      speaker.playWAV('/sd/success.wav')
      wait(1)
      sd_data=None
      qr_sd_data=None
      num1=None
      num2=None
      num3=None
      num4=None
      num5=None
      num6=None
      num7=None
      num8=None
      exit=0
      Emp_id_status=0
      Emp_ID=None
      task_value_dsp=None
      home_screen()# exit
    
    
  
  








def update_date(clock_data):
  with open('/sd/date.text', 'w') as fs:
     fs.write(clock_data)
     os.remove('/sd/id.text')
     sd_id_write_s()
     
    
    



def clear_clocks():
  try:
    with open('/sd/date.text', 'r') as fs:
      Day=rtc.datetime()[2]
      clock_data=str(fs.read())
      if str(clock_data)!=str(Day):
        update_date(str(Day))
  except:
     while True:
       lcd.clear()
       lcd.font(lcd.FONT_DejaVu18)
       lcd.print('INSERT SD CARD & RESTART!!', 10, 100, 0xcc0000)
       wait(5)
      
    
       


def time(new_day,new_month,new_year):
  
  count=0
  time_status=1
  ch_status=0
  hour_data=0
  minute_data=0
  while time_status==1:
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print("Hour", 20, 0, 0xffffff)
    lcd.print("Minute", 100, 0, 0xffffff)
    lcd.print('SAVE', 10, 200, 0xffffff)
    lcd.print('BACK', 190, 200,  0xffffff)
   
    lcd.font(lcd.FONT_DejaVu40)
    lcd.print('<-', 30, 130, 0xffffff)
    lcd.print('M', 130, 130, 0xffffff)
    lcd.print('->', 250, 130, 0xffffff)
    if ch_status==0:
       lcd.print("__", 30, 70, 0x00ff55)
       if count>23:
          count=23
       if count<0:
          count=0
          
       hour_data=count
    if ch_status==1:
      if count>59:
         count=0
      if count<1:
         count=1
      lcd.print("__", 130, 70, 0x00ff55)
      lcd.print("__", 30, 70, 0x000000)
      minute_data=count
      
    if ch_status>1:
      lcd.clear()
      ch_status=0
    lcd.print(hour_data, 30, 40, 0xffffff)
    lcd.print(':', 90, 40, 0xffffff)
    lcd.print(minute_data, 120, 40, 0xffffff)
    
    prev_month=rtc.datetime()[1]
    
    
    if hour_data>=12 and hour_data!=23:
      lcd.print(str("PM"), 180, 40, 0x199f44)
    if hour_data==23:
      lcd.print(str("PM"), 180, 40, 0x199f44)
    if hour_data <12 and hour_data!=23:
      lcd.print(str("AM"), 180, 40, 0x199f44)
    if hour_data==0:
      lcd.print(str("AM"), 180, 40, 0x199f44)
      
    if prev_month>=3 and prev_month<=11:
       lcd.print(str("DST"), 180, 80, 0xc9af0a)
      
      
   
      
      
    
    if (touch.status())==1 and (touch.read()[0]) >40 and (touch.read()[0]) <90  and (touch.read()[1]) >150 and  (touch.read()[1]) <180: # INCREMENT
      speaker.playWAV('/sd/button.wav')
      
      wait_ms(50)
      count=count-1
      lcd.clear()
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <300  and (touch.read()[1]) >150 and  (touch.read()[1]) <180: # DECREMENT
      speaker.playWAV('/sd/button.wav')
     
      wait_ms(50)
      count=count+1
      lcd.clear()
    if (touch.status())==1 and (touch.read()[0]) >120 and (touch.read()[0]) <180  and (touch.read()[1]) >150 and  (touch.read()[1]) <180: # MODE
      speaker.playWAV('/sd/button.wav')
     
      lcd.clear()
      ch_status=ch_status+1
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <100  and (touch.read()[1]) >200 and  (touch.read()[1]) <250:# SAVE
      speaker.playWAV('/sd/button.wav')
      
      lcd.clear()
      if prev_month>=3 and prev_month<=11:
        new_hour=hour_data+1
      else:
        new_hour=hour_data
      
      
      
      new_minute=minute_data
      time_status=0
      date_status=0
      settings=1
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(str("UPDATE success"), 100, 100, 0xffffff)
      speaker.playWAV('/sd/success.wav')
      wait(1)
      new_day=rtc.datetime()[2]
      new_month=rtc.datetime()[1]
      year=str(rtc.datetime()[0])
      new_year=str(year[2])+str(year[3])
     
       
     
      
      
      rtc.datetime((int(new_year), new_month, new_day, 0, new_hour, new_minute, 0, 0))
      lcd.clear()
      setgs(new_day,new_month,new_year,new_hour,new_minute)
      
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <300  and (touch.read()[1]) >200 and  (touch.read()[1]) <300: # back
      speaker.playWAV('/sd/button.wav')
     
      prev_hour=0
      prev_min=0
      prev_month=0
      prev_date=0
      year=str(rtc.datetime()[0])
      prev_year=str(year[2])+str(year[3])
      prev_hour=rtc.datetime()[4]
      prev_minute=rtc.datetime()[5]
      prev_day=rtc.datetime()[2]
      prev_month=rtc.datetime()[1]
      
      lcd.clear()
      time_status=0
      date_status=0
      settings=1
      setgs(prev_day,prev_month,prev_year,prev_hour,prev_minute)
      
      
        
      
       
def date(new_hour,new_minute): 
  count=0
  date_status=1
  ch_status=0
  day_data=0
  month_data=0
  year_data=0
  while date_status==1:
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print("Day", 20, 0, 0xffffff)
    lcd.print("Month", 100, 0, 0xffffff)
    lcd.print("Year", 200, 0, 0xffffff)
    lcd.print('SAVE', 10, 200, 0xffffff)
    lcd.print('BACK', 190, 200,  0xffffff)
    lcd.font(lcd.FONT_DejaVu40)
    lcd.print('<-', 30, 130, 0xffffff)
    lcd.print('M', 130, 130, 0xffffff)
    lcd.print('->', 250, 130, 0xffffff)
    
    if ch_status==0:
      lcd.print("__", 30, 70, 0x00ff55)
       
      if count>31:
          count=31
      if count<1:
          count=1
      day_data=count
    if ch_status==1:
      if count>=3 and count<=11:
          
          lcd.print('DST', 80, 180,  0xc9af0a)## DAY LIGHT ADJUSTMENT
      if count>12:
          count=12
         
           
           
        
      if count<1:
          count=1
      lcd.print("__", 130, 70, 0x00ff55)
      lcd.print("__", 30, 70, 0x000000)
      month_data=count
    if ch_status==2:
      lcd.print("__", 220, 70, 0x00ff55)
      lcd.print("__", 30, 70, 0x000000)
      lcd.print("__", 30, 70, 0x000000)
      if count<21:
          count=21
      if count>99:
          count=21
      
      if count==0:
        count=21
      year_data=count
        
    if ch_status>2:
      lcd.clear()
      ch_status=0
      
    lcd.print(day_data, 30, 40, 0xffffff)
    lcd.print('|', 90, 40, 0xffffff)
    lcd.print(month_data, 120, 40, 0xffffff)
    lcd.print('|', 180, 40, 0xffffff)
    lcd.print(year_data, 200, 40, 0xffffff)
          
    if (touch.status())==1 and (touch.read()[0]) >40 and (touch.read()[0]) <90  and (touch.read()[1]) >150 and  (touch.read()[1]) <180: # INCREMENT 
       speaker.playWAV('/sd/button.wav')
      
       wait_ms(50)
       count=count-1
       lcd.clear()
       
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <300  and (touch.read()[1]) >150 and  (touch.read()[1]) <180: # DECREMENT
       speaker.playWAV('/sd/button.wav')
       
       wait_ms(50)
       count=count+1
       lcd.clear()
       
    if (touch.status())==1 and (touch.read()[0]) >120 and (touch.read()[0]) <180  and (touch.read()[1]) >150 and  (touch.read()[1]) <180: # MODE
       speaker.playWAV('/sd/button.wav')
      
       ch_status=ch_status+1
       lcd.clear()
       
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <100  and (touch.read()[1]) >200 and  (touch.read()[1]) <250: #SAVE
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      new_day=day_data
      new_month=month_data
      new_year=year_data
      date_status=0
      settings=1
      if new_day<=0:
        new_day=1
      if new_month<=0:
        new_month=1
      if new_year<=0:
        new_year=21
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print(str("UPDATE success"), 100, 100, 0xffffff)
      speaker.playWAV('/sd/success.wav')
      new_hour=rtc.datetime()[4]
      new_minute=rtc.datetime()[5]
      wait(1)
      rtc.datetime((new_year, new_month, new_day, 0, new_hour, new_minute, 0, 0))
      lcd.clear()
      setgs(new_day,new_month,new_year,new_hour,new_minute)
      
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <300  and (touch.read()[1]) >200 and  (touch.read()[1]) <300:  # back
      speaker.playWAV('/sd/button.wav')
     
      prev_hour=0
      prev_min=0
      prev_month=0
      prev_date=0
      year=str(rtc.datetime()[0])
      prev_year=str(year[2])+str(year[3])
      prev_hour=rtc.datetime()[4]
      prev_minute=rtc.datetime()[5]
      prev_day=rtc.datetime()[2]
      prev_month=rtc.datetime()[1]
      
      lcd.clear()
      time_status=0
      date_status=0
      settings=1
      setgs(prev_day,prev_month,prev_year,prev_hour,prev_minute)
      
      
     
       
       


def setgs(new_day,new_month,new_year,new_hour,new_minute):
  settings=1
  while settings==1:
    
   
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('DATE', 50, 80, 0xffffff)
    lcd.print('TIME', 200, 80, 0xffffff)
    lcd.print('BACK', 10, 200, 0xffffff)
    lcd.print('ERASE',200, 140, 0xffffff)
   
    if (touch.status())==1 and (touch.read()[0]) >40 and (touch.read()[0]) <150  and (touch.read()[1]) >100 and  (touch.read()[1]) <150: #  Date selection
       speaker.playWAV('/sd/button.wav')
       lcd.clear()
       settings=0
       date(new_hour,new_minute)
       
    if (touch.status())==1 and (touch.read()[0]) >190 and (touch.read()[0]) <300  and (touch.read()[1]) >90 and  (touch.read()[1]) <150: # time selection
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      settings=0
      time(new_day,new_month,new_year)
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <100  and (touch.read()[1]) >200 and  (touch.read()[1]) <250: # back selection
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      settings=0
      home_status=1
      lcd.clear()
      home_screen()
    
    if (touch.status())==1 and (touch.read()[0]) >180 and (touch.read()[0]) <260  and (touch.read()[1]) >140 and  (touch.read()[1]) <200:# erase history
      speaker.playWAV('/sd/button.wav')
      erase=0
      lcd.clear()
      while erase==0:
        lcd.print("ERASE HISTORY IN SD ?", 40, 100,  0xff2727)
        lcd.print('NO', 10, 200, 0xffffff)
        lcd.print('YES', 190, 200,  0xffffff)
        if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <100  and (touch.read()[1]) >200 and  (touch.read()[1]) <250:  # no
          lcd.clear()
          erase=1
          settings=0
          wait_ms(500)
          setgs(new_day,new_month,new_year,new_hour,new_minute)
          
        if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <350  and (touch.read()[1]) >200 and  (touch.read()[1]) <350:# yes
           
           speaker.playWAV('/sd/button.wav')
           lcd.clear()
           dot=180
           lcd.print("ERASING", 100, 100,  0xfffe38)
           os.remove('/sd/history.text')
           with open('/sd/history.text', 'a') as fs:
             for y in range(0, 5, 1):
               dot+=10
               lcd.print(".", dot,100,0xfffe38)
               wait(1)
           lcd.clear()
           lcd.print("DONE", 100, 100,0x18f830)
           speaker.playWAV('/sd/success.wav')
           wait(2)
           lcd.clear()
           setgs(new_day,new_month,new_year,new_hour,new_minute)
           
         
      


def id_check_clkin(Emp_ID):
  Emp_id_status=0
  loop=1
  data=None
  lcd.print(str("Plz wait.."), 100, 100, 0xffffff)
  wait(1)
  with open('/sd/id.text', 'r') as fs:
    while loop==1:
      
       
      
       data=fs.readline()
       try:
         if data[0]==Emp_ID[0] and data[1]==Emp_ID[1] and data[2]==Emp_ID[2] and data[3]==Emp_ID[3] and data[4]==Emp_ID[4] and data[5]==Emp_ID[5] and  data[6]==Emp_ID[6] and  data[7]==Emp_ID[7]:                                                          
            
            lcd.clear()
            lcd.print("ALREADY CLOCKED IN !!", 40, 100,  0xff2727)
            #speaker.playWAV("/sd/warning.wav", rate=44100, dataf=speaker.F16B)
            speaker.playWAV('/sd/warning.wav')
            
           
            wait(5)
            num1=None
            num2=None
            num3=None
            num4=None
            num5=None
            num6=None
            num7=None
            num8=None
            data=None
            loop=0
            Emp_id_status=0
            Emp_ID=None
            home_screen()
       except:
         lcd.clear()
         lcd.print("CIN VERIFIED", 70, 100,  0x18f830)
         speaker.playWAV('/sd/success.wav')
         wait(1)
         sd_id_write(Emp_ID+"\n")
         num1=None
         num2=None
         num3=None
         num4=None
         num5=None
         num6=None
         num7=None
         num8=None
         data=None
         Emp_id_status=0
         loop=0
        


def id_check_clkout(Emp_ID):
  loop=1
  lcd.clear()
  lcd.print(str("Plz wait.."), 100, 100, 0xffffff)
  wait(1)
  clkindata=None
  clockinlist_length=None
  int_clockinlist_length=0
  with open('/sd/id.text', 'r') as fs:
     clkindata=fs.read()
     clockin_list = clkindata.split()
     clockinlist_length=str(len(clockin_list))
     int_clockinlist_length=int(clockinlist_length)
     
     x=-1
     z=None
     while loop==1:
        x+=1
        
        try:
          if str(Emp_ID)==str(clockin_list[x]):
            z=str(clockin_list[x])
            lcd.clear()
            lcd.print(str("COUT VERIFIED"), 100, 100,  0x18f830)
            speaker.playWAV('/sd/success.wav')
            wait(1)
            clockin_list.remove(clockin_list[x])
            clockinlist_length=str(len(clockin_list))
            int_clockinlist_length=int(clockinlist_length)
            os.remove('/sd/id.text')
            
            
            with open('/sd/id.text', 'a') as fs:
              for y in range(0, int_clockinlist_length, 1):
                
                fs.write(str(clockin_list[(y)])+"\n")
            x=0
            loop=0
            
                
              
           
           
            
        except:
          lcd.clear()
          lcd.print("NOT CLOCKED IN !!", 50, 100,  0xff2727)
          speaker.playWAV('/sd/warning.wav')
         
          
          wait(5)
          loop=0
          x=0
          home_screen()
          
          
  


def bat_status():
  
  charge_state=power.getChargeState()
  charge_voltage=power.getBatVoltage()
  charge_current=power.getBatCurrent()
  lcd.font(lcd.FONT_Default)
  lcd.print(str("BAT :"), 120, 0, 0xff99ff)
  lcd.print(str(round(charge_voltage,1)), 170, 0, 0xff99ff)
  lcd.print(str("v"), 195, 0, 0xff99ff)
  if charge_state == False and  charge_current < -1.0: 
     lcd.print(str("                                                       "),220, 0, 0x000000)    ## plugged out discharge
     wait_ms(20)
     lcd.print(str("Plugged"),220, 0, 0xff0050)
     lcd.print(str("OUT"),290, 0, 0xff0050)
    
    
  if charge_state == True and charge_current > 0: 
     lcd.print(str("OUT"),290, 0, 0x000000)    ## plugged in charging
     wait_ms(20)
     lcd.print(str("Plugged"),220, 0, 0x00ff63)
    
  
  
  
  if charge_state == False and charge_current == -1.0: 
     lcd.print(str("OUT"),290, 0, 0x000000)      ## plugged in full charge
     wait_ms(20)
     lcd.print(str("Plugged"),220, 0, 0x00ff63)
   
    
  if charge_state == False and charge_current == 0.0: 
     lcd.print(str("OUT"),290, 0, 0x000000)    ## plugged in but cureent 0.0
     wait_ms(20)
     lcd.print(str("Plugged"),220, 0, 0x00ff63)
    
    


 
  
def sd_id_write(emp_id):   
    with open('/sd/id.text', 'a') as fs:## normal id writing
      fs.write(emp_id)
  
    


def sd_write(sd_data):
  with open('/sd/history.text', 'a') as fs: ## normal history writing
    fs.write(sd_data)
    
    
    
def sd_write_s():
  with open('/sd/history.text', 'a') as fs: ## intial data writing for history file creation
    fs.write("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"+"\n")
  
def sd_id_write_s():
  with open('/sd/id.text', 'a') as fs:
    fs.write("00000000"+"\n")## intial data writing for id file creation
  
def sd_date_write_s():    
  with open('/sd/date.text','a')as fs: 
    fs.write("0"+"\n") ## intial data writing for date file creation

  
 
  
  
 
 
def sd_check():
  try:
    with open('/sd/check.text', 'r') as fs:
      check=fs.read()
  except:
    while True:
      lcd.clear()
      lcd.font(lcd.FONT_DejaVu18)
      lcd.print('INSERT SD CARD & RESTART!!', 10, 100, 0xcc0000)
      wait(5)
     
      

  
    
def Emp(clk):
  num1=None
  num2=None
  num3=None
  num4=None
  num5=None
  num6=None
  num7=None
  num8=None
  Emp_ID=None
  var=None
  i=0
  
  mac_id=espnow.get_mac_addr()
  mac_id_hex=mac_id[12]+mac_id[13]+mac_id[15]+mac_id[16]
 
  
  

  Emp_id_status=1
  
  
  
  
  
  while Emp_id_status==1:
    sd_check()
    power.setVibrationEnable(False)
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('ID :', 0, 20, 0xffffff)
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
    
    Hour=rtc.datetime()[4]
    Min=rtc.datetime()[5]
    Day=rtc.datetime()[2]
    Month=rtc.datetime()[1]
    Year=rtc.datetime()[0]
    
    if Month>=3 and Month<=11:
      Hour=Hour-1
      

    
    
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <70  and (touch.read()[1]) >80 and  (touch.read()[1]) <110:   # 0
         speaker.playWAV('/sd/button.wav')
         var='0'
         i=i+1
  
    if (touch.status())==1 and (touch.read()[0]) >120 and (touch.read()[0]) <140  and (touch.read()[1]) >80 and  (touch.read()[1]) <110:   # 1
         speaker.playWAV('/sd/button.wav')
         var='1'
         i=i+1
         
         
    if (touch.status())==1 and (touch.read()[0]) >185 and (touch.read()[0]) <220  and (touch.read()[1]) >80 and  (touch.read()[1]) <110:  # 2
         speaker.playWAV('/sd/button.wav')
         var='2'
         i=i+1
         
         
    if (touch.status())==1 and (touch.read()[0]) >265 and (touch.read()[0]) <300  and (touch.read()[1]) >80 and  (touch.read()[1]) <110:  # 3
         speaker.playWAV('/sd/button.wav')
         var='3'
         i=i+1
        
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <70  and (touch.read()[1]) >140 and  (touch.read()[1]) <170:  #4
         speaker.playWAV('/sd/button.wav')
         var='4'
         i=i+1
        
         
    if (touch.status())==1 and (touch.read()[0]) >110 and (touch.read()[0]) <155  and (touch.read()[1]) >140 and  (touch.read()[1]) <170: # 5
         speaker.playWAV('/sd/button.wav')
         var='5'
         i=i+1
         
        
    if (touch.status())==1 and (touch.read()[0]) >170 and (touch.read()[0]) <210  and (touch.read()[1]) >140 and  (touch.read()[1]) <175: # 6
         speaker.playWAV('/sd/button.wav')
         var='6'
         i=i+1
         
        
    if (touch.status())==1 and (touch.read()[0]) >255 and (touch.read()[0]) <280  and (touch.read()[1]) >140 and  (touch.read()[1]) <170:  #7
         speaker.playWAV('/sd/button.wav')
         var='7'
         i=i+1
        
         
    if (touch.status())==1 and (touch.read()[0]) >30 and (touch.read()[0]) <70  and (touch.read()[1]) >200 and  (touch.read()[1]) <210: #8
         speaker.playWAV('/sd/button.wav')
         var='8'
         i=i+1
         
        
    if (touch.status())==1 and (touch.read()[0]) >110 and (touch.read()[0]) <150  and (touch.read()[1]) >200 and  (touch.read()[1]) <230: # 9
         speaker.playWAV('/sd/button.wav')
         var='9'
         i=i+1
         
        
    if (touch.status())==1 and (touch.read()[0]) >200 and (touch.read()[0]) <230  and (touch.read()[1]) >200 and  (touch.read()[1]) <230: #C
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
         
    if (touch.status())==1 and (touch.read()[0]) >230 and (touch.read()[0]) <280  and (touch.read()[1]) >40 and  (touch.read()[1]) <70: #back
        speaker.playWAV('/sd/button.wav')
        Emp_id_status=0
        lcd.clear()
        home_screen()
         
         
         
         
         
         
    if (touch.status())==1 and (touch.read()[0]) >255 and (touch.read()[0]) <290  and (touch.read()[1]) >200 and  (touch.read()[1]) <230: # E
      
    
    
        
    
    
         speaker.playWAV('/sd/button.wav')
         lcd.clear()
         
         if str(num1)==str(None) or str(num2)==str(None) or str(num3)==str(None) or str(num4)==str(None):
           
          
           
           lcd.print("INVALID ID", 100, 100, 0xffffff)
           #speaker.playWAV("/sd/warning.wav", rate=44100, dataf=speaker.F16B)
           speaker.playWAV('/sd/warning.wav')
           wait(2)
           
           num1=None
           num2=None
           num3=None
           num4=None
           num5=None
           num6=None
           num7=None
           num8=None
           Emp_id_status==0
           home_screen()
           
         if str(num5)==str(None) and str(num6)==str(None) and str(num7)==str(None) and str(num8)==str(None): # strings 5 t0 8 empty
           
            Emp_id_status=0
            Emp_ID=str("0")+str("0")+str("0")+str("0")+str(num1)+str(num2)+str(num3)+str(num4)
            data_formatting(Emp_ID,Day,Month,Year,Hour,Min,clk, mac_id_hex)
           
         if  str(num6)==str(None) and str(num7)==str(None) and str(num8)==str(None): #strings  6 to 8 empty
           
            Emp_id_status=0
            Emp_ID=str("0")+str("0")+str("0")+str(num1)+str(num2)+str(num3)+str(num4)+str(num5)
            data_formatting(Emp_ID,Day,Month,Year,Hour,Min,clk, mac_id_hex)
            
            
            
         if  str(num7)==str(None) and str(num8)==str(None): #strings  7 to 8 empty
            
            Emp_id_status=0
            Emp_ID=str("0")+str("0")+str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)
            data_formatting(Emp_ID,Day,Month,Year,Hour,Min,clk, mac_id_hex)
            #Emp_id_status==0
            #home_screen()
           
         if  str(num8)==str(None): #strings  7 to 8 empty
           
            Emp_id_status=0
            Emp_ID=str("0")+str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)+str(num7)
            data_formatting(Emp_ID,Day,Month,Year,Hour,Min,clk, mac_id_hex)
            
           
         if str(num1)!=str(None) and str(num2)!=str(None) and  str(num3)!=str(None) and str(num4)!=None and str(num5)!=str(None) and str(num6)!=str(None) and str(num7)!=str(None) and str(num8)!=str(None):
             Emp_id_status=0
             Emp_ID=str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)+str(num7)+str(num8)
             data_formatting(Emp_ID,Day,Month,Year,Hour,Min,clk, mac_id_hex)
          
           
          #_________________________________________________________________________________________________________
           
          
         
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









def home_screen(): # home screen
  lcd.clear()
  home_status=1
  bat_status()
  
  
 
  while home_status==1:
    
    M=rtc.datetime()[5]
    H=rtc.datetime()[4]
    Mnth=rtc.datetime()[1]
    Mnth1=rtc.datetime()[1]
    D=rtc.datetime()[2]
    clear_clocks() 
    sd_check()
   
    lcd.font(lcd.FONT_DejaVu24)
    lcd.print('CIN', 65, 130, 0x009900)
    lcd.print('COUT', 190, 130, 0xcc0000)
    
    
    
   
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('----------------------------------------', 0, 180, 0x64e6e7)
    lcd.print("HISTORY", 220, 40,  0xffffff)
    lcd.print("SETTINGS", 110, 40,  0xffffff)

    #lcd.print((rtc.datetime()[2]), 0, 10, 0xffffff) # day
    lcd.print('-', 25, 10, 0xffffff)
    #lcd.print((rtc.datetime()[1]), 35, 10, 0xffffff) # month
    lcd.print('-', 63, 10, 0xffffff)
    lcd.print((rtc.datetime()[0]), 70, 10, 0xffffff) # year
    #lcd.print((rtc.datetime()[4]), 15, 40, 0xffffff)
    lcd.print(':', 30, 40, 0xffffff)
    #lcd.print((rtc.datetime()[5]), 55, 40, 0xffffff) #40
    lcd.print("MAC ID : ", 20, 200,  0xffffff)
    lcd.print((espnow.get_mac_addr()), 120, 200, 0xffffff)
   
    #lcd.print((touch.read()[0]), 0, 80, 0xffffff)
    #lcd.print((touch.read()[1]), 50, 80, 0xffffff)
    #wait(1)
    #lcd.clear()
    
    if Mnth>=3 and Mnth<=11:
      H=H-1
      lcd.print("[ DST ]", 5, 70, 0xc9af0a) # year
    
    if Mnth1==1 or Mnth1==2 or Mnth1==3 or Mnth1==4 or Mnth1==5 or Mnth1==6 or Mnth1==7 or Mnth1==8 or Mnth1==9:
      lcd.print("0", 35, 10, 0xffffff) # month
      lcd.print((rtc.datetime()[1]), 50, 10, 0xffffff) # month
    else:
      lcd.print((rtc.datetime()[1]), 35, 10, 0xffffff) 
      
    if D==1 or D==2 or D==3 or D==4 or D==5 or D==6 or D==7 or D==8 or D==9:
      lcd.print("0", 0, 10, 0xffffff) # day
      lcd.print((rtc.datetime()[2]), 10, 10, 0xffffff) # day
    else:
      lcd.print((rtc.datetime()[2]), 0, 10, 0xffffff) # day
      
      
      
      
      
    
    
    
    if M==0 or M==1 or M==2 or M==3 or M==4 or M==5 or M==6 or M==7 or M==8 or M==9:
      lcd.print(str(M), 55, 40, 0xffffff) #40
      lcd.print("0", 40, 40, 0xffffff) #40
    else:
       
       lcd.print(str(M), 40, 40, 0xffffff) #40
    if H==0 or H==1 or H==2 or H==3 or H==4 or H==5 or H==6 or H==7 or H==8 or H==9:
      lcd.print(str(H), 15, 40, 0xffffff) #40
      lcd.print("0", 0, 40, 0xffffff) #40
    else:
       
       lcd.print(str(H), 0, 40, 0xffffff) #40
       
       
    
      
  
    refresh=rtc.datetime()[6]
    
    bat_status()
   
    if refresh==1:
      lcd.clear()
      wait(.900)
      
    






    if rtc.datetime()[4]>=12:
      lcd.font(lcd.FONT_Default)
      lcd.print("PM",70,40,0xffffff)
    else:
       lcd.font(lcd.FONT_Default)
       lcd.print("AM",70,40,0xffffff)
      
    if (touch.status()) == 1 and (touch.read()[0]) > 90 and (touch.read()[0]) < 115  and (touch.read()[1]) > 140 and  (touch.read()[1])  < 170 : # cin
      home_status=0
      clk=1
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      Emp(clk)
      
    if (touch.status()) == 1 and (touch.read()[0]) > 190 and (touch.read()[0]) < 230  and (touch.read()[1]) > 140 and  (touch.read()[1])  < 170 : # cout
      home_status=0
      clk=0
      speaker.playWAV('/sd/button.wav')
      lcd.clear()
      Emp(clk)
      
    if (touch.status())==1 and (touch.read()[0]) >130 and (touch.read()[0]) <175  and (touch.read()[1]) >70 and  (touch.read()[1]) <100:   # settings
      lcd.clear()
      speaker.playWAV('/sd/button.wav')
      pass_status=1
      pass_window(pass_status)
      lcd.clear()
      setgs(new_day,new_month,new_year,new_hour,new_minute)
   
     
    if (touch.status())==1 and (touch.read()[0]) > 240 and (touch.read()[0]) <280  and (touch.read()[1]) >70 and  (touch.read()[1]) <100:   # history
      speaker.playWAV('/sd/button.wav')
      history_status=1
      history()
    lcd.font(lcd.FONT_Default)
    lcd.print("VER : 1.1", 220, 70,  0xffffff)
    
def  dsp(line_count,data_file,list_length,list_limit):
  
   string=data_file[line_count]
   list_length=int(list_length)
   read_emp_id =string[0]+string[1]+string[2]+string[3]+string[4]+string[5]+string[6]+string[7]
   read_day    =string[8]+string[9]+string[10]+string[11]+string[12]+string[13]+string[14]+string[15]
   read_month  =string[16]+string[17]+string[18]+string[19]+string[20]+string[21]+string[23] # reading  8 digit for month
   read_year   =string[24]+string[25]+string[26]+string[27]+string[28]+string[29]+string[30]+string[31] # # reading  8 digit for year
   read_hour   =string[32]+string[33]+string[34]+string[35]+string[36]+string[38]+string[39] # reading  8 digit for hour
   read_Min    =string[40]+string[41]+string[42]+string[43]+string[44]+string[45]+string[46]+string[47] # # reading  8 digit for min
   read_clk    =string[48]+string[49]+string[50]+string[51]+string[52]+string[53]+string[54]+string[55] # reading  8 digit for clk
   read_dvid   =string[56]+string[57]+string[58]+string[59] # reading device id
   
   read_tc1    =string[60]
   read_tc2    =string[61]
   read_tc3    =string[62]
   read_tc4    =string[63]
   read_tc5    =string[64]
   read_tc6    =string[65]
   read_tc7    =string[66]
   read_tc8    =string[67]
   read_tc9    =string[68]
   read_tc10   =string[69]
   read_tc11   =string[70]
   read_tc12   =string[71]
   read_tc13   =string[72]
   read_tc14   =string[73]
   read_tc15   =string[74]
   read_tc16   =string[75]
   read_tc17   =string[76]
   read_tc18   =string[77]
   read_tc19   =string[78]
   read_tc20   =string[79]
   read_tc21   =string[80]
   read_tc22   =string[81]
   read_tc23   =string[82]
   read_tc24   =string[83]
   read_tc25   =string[84]
   read_tc26   =string[85]
   read_tc27   =string[86]
   read_tc28   =string[87]
   read_tc29   =string[88]
   
   if read_tc1=="*":
     read_tc1 =" "
   if read_tc2=="*":
     read_tc2 =" "
   if read_tc3=="*":
     read_tc3 =" "
   if read_tc4=="*":
     read_tc4 =" "
   if read_tc5=="*":
     read_tc5 =" "
   if read_tc6=="*":
     read_tc6 =" "
   if read_tc7=="*":
     read_tc7 =" "
   if read_tc8=="*":
     read_tc8 =" "
   if read_tc9=="*":
     read_tc9 =" "
   if read_tc10=="*":
     read_tc10 =" "
     
   if read_tc11=="*":
     read_tc11 =" "
   if read_tc12=="*":
     read_tc12 =" "
   if read_tc13=="*":
     read_tc13 =" "
   if read_tc14=="*":
     read_tc14 =" "
   if read_tc15=="*":
     read_tc15 =" "
   if read_tc16=="*":
     read_tc16 =" "
   if read_tc17=="*":
     read_tc17 =" "
   if read_tc18=="*":
     read_tc18 =" "
   if read_tc19=="*":
     read_tc19 =" "
   if read_tc20=="*":
     read_tc20 =" "
     
   if read_tc21=="*":
     read_tc21 =" "
   if read_tc22=="*":
     read_tc22 =" "
   if read_tc23=="*":
     read_tc23 =" "
   if read_tc24=="*":
     read_tc24 =" "
   if read_tc25=="*":
     read_tc25 =" "
   if read_tc26=="*":
     read_tc26 =" "
   if read_tc27=="*":
     read_tc27 =" "
   if read_tc28=="*":
     read_tc28 =" "
   if read_tc29=="*":
     read_tc29 =" "
     
     









   int_read_emp_id=int(read_emp_id,16)
   int_read_day=int(read_day,16)
   int_read_month=int(read_month,16)
   int_read_year=int(read_year,16)
   int_read_hour=int(read_hour,16)
   int_read_Min=int(read_Min,16)
   int_read_clk=int(read_clk,16)
   
   
   
  
   
   
   task_code=str(read_tc1)+str(read_tc2)+str(read_tc3)+str(read_tc4)+str(read_tc5)+str(read_tc6)+str(read_tc7)+str(read_tc8)+str(read_tc9)+str(read_tc10)+str(read_tc11)+str(read_tc12)+str(read_tc13)+str(read_tc14)+str(read_tc15)+str(read_tc16)+str(read_tc17)+str(read_tc18)+str(read_tc19)+str(read_tc20)+str(read_tc21)+str(read_tc22)+str(read_tc23)+str(read_tc24)+str(read_tc25)+str(read_tc26) +str(read_tc27)+str(read_tc28)+str(read_tc29)                                                                                                                                                                                                                         
   
   
   lcd.font(lcd.FONT_DejaVu18)
   lcd.print('HISTORY', 0, 0, 0xffff33)
   lcd.print(str(line_count+1), 200, 0, 0xffff33)
   lcd.print(str("/"), 230, 0, 0xffff33)
   lcd.print(str(list_length+1), 250, 0, 0xffff33)
   lcd.print(str("LIMIT:"), 200, 30, 0xffff33)
   lcd.print(str(list_limit+1), 270, 30, 0xffff33)
   lcd.print(str(int_read_emp_id), 0, 30, 0xffffff)
   lcd.print(str(int_read_day), 0, 50, 0xffffff)
  #lcd.print(str(":"), 100, 70, 0xffffff)
   lcd.print(str(int_read_month), 30, 50, 0xffffff)
   lcd.print(str(int_read_year), 50, 50, 0xffffff)
   lcd.print(str(int_read_hour), 0, 70, 0xffffff)
   lcd.print(str(int_read_Min), 30, 70, 0xffffff)
   lcd.print(str(read_dvid), 0, 110, 0xffffff)
   if int_read_clk==0:
      lcd.print(str("COUT"), 0, 90, 0xffffff)
      if task_code=="00000000000000000000000000000":
        lcd.print(str("YES TO ALL"), 0, 150, 0xffffff)
      if task_code!="00000000000000000000000000000":
        lcd.print(str(task_code), 0, 150, 0xffffff)
        
        
      #lcd.print(str("COUT"), 0, 90, 0xffffff)
      
   if int_read_clk==1:
      lcd.print(str("CIN"), 0, 90, 0xffffff)
      
   read_hex_emp_id=hex(int_read_emp_id)[2:]
   read_hex_day=hex(int_read_day)[2:]
   read_hex_month=hex(int_read_month)[2:]
   read_hex_year=hex(int_read_year)[2:]
   read_hex_hour=hex(int_read_hour)[2:]
   read_hex_min=hex(int_read_Min)[2:]
   read_read_clk=hex(int_read_clk)[2:]
   
   lcd.font(lcd.FONT_DejaVu18)
   lcd.print(str(read_hex_emp_id+"."+read_hex_day+"."+read_hex_month+"."+read_hex_year+"."+read_hex_hour+"."+read_hex_min+"."+read_read_clk+"."+read_dvid), 0, 130, 0xffffff)
  
   
  
   lcd.font(lcd.FONT_DejaVu18)
  #lcd.qrcode(str(string), 190, 60, 100)
   lcd.print('PREV', 10, 197, 0x208e8a)
   lcd.print('NEXT', 230, 197, 0x208e8a)
   lcd.print('BACK', 130, 197, 0x208e8a)
   
   
   
    
    




def history():
  line_count=0
 
  with open('/sd/history.text', 'r') as fs:
     sd = fs.read()
     data_file = sd.split()
     list_length=str(len(data_file)-1)
     list_limit=99
     
     
     if list_length==str(-1):
       lcd.clear()
       lcd.font(lcd.FONT_DejaVu24)
       lcd.print(str("NO DATA"), 100, 107, 0xFFFFFF)
       speaker.playWAV('/sd/warning.wav')
       wait(3)
       history_status=0
       home_screen()
       
      
     lcd.clear()
     dsp(line_count,data_file,list_length, list_limit)
     history_status=1
     #line_count=0
     
     while history_status==1:
       sd_check()
        
       if (touch.status())==1 and (touch.read()[0]) >60 and (touch.read()[0]) <80  and (touch.read()[1]) >200 and  (touch.read()[1]) <250: 
         speaker.playWAV('/sd/button.wav')
        
         if str(line_count)==str("0"):                                                          
             lcd.clear()
             line_count=0
             dsp(line_count,data_file,list_length, list_limit)
         else:
           lcd.clear()
           line_count=line_count-1
           dsp(line_count,data_file,list_length,list_limit)
      
       if (touch.status())==1 and (touch.read()[0]) >220 and (touch.read()[0]) <280  and (touch.read()[1]) >200 and  (touch.read()[1]) <250: 
         speaker.playWAV('/sd/button.wav')
         
         if str(line_count)==str(list_length) or str(line_count)==str(list_limit):
                                                                                 
           line_count=0
           lcd.clear()
           dsp(line_count,data_file,list_length, list_limit)
        
         
             
             
         else:
            lcd.clear()
            line_count=line_count+1
            dsp(line_count,data_file,list_length, list_limit)
        
        
            
             
           
              
              
       if (touch.status())==1 and (touch.read()[0]) >150 and (touch.read()[0]) <170  and (touch.read()[1]) >200 and  (touch.read()[1]) <280: 
           
           speaker.playWAV('/sd/button.wav')
           history_status=0
           lcd.clear()
           home_screen()

  
  
  
  
power.setVibrationIntensity(5)
lcd.font(lcd.FONT_DejaVu40)
for bright in range(0, 100, 1):
 
  screen.set_screen_brightness(bright)
  lcd.print('C', 100, 100,0xe937ff)
  wait_ms(5)
  lcd.print('I', 130, 100, 0xff0d0d)
  wait_ms(5)
  lcd.print('C', 145, 100, 0xfff60b)
  wait_ms(5)
  lcd.print('O', 175, 100, 0xb1cfff)
  wait_ms(5)

lcd.font(lcd.FONT_DefaultSmall)
lcd.print('Employee Interactive Voice Response System', 30, 150, 0xffffff)
speaker.playWAV('/sd/sd_ok.wav')
wait(1)
  
     
     
     


try:
  with open('/sd/check.text', 'w') as fs:
    fs.write('OK')
    
    wait(2)
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
wait(1)
#speaker.playWAV("/sd/sd_ok.wav", rate=44100, dataf=speaker.F16B)
#wait(1)




login_flag=1
lcd.clear()

login_flag = str(nvs.read_str('2'))


lcd.clear()
  
while login_flag=="1":
  
  #Activate_status=1
  home_screen()
  
while login_flag !="1":
  
  
  sd_check()
  power.setVibrationEnable(False)
  lcd.font(lcd.FONT_DejaVu18)
  lcd.print('ENTER DEVICE LOGIN ID->', 0, 20,  0xffffff)
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
  lcd.print('ACTIVATE', 190, 200,  0xffffff)
 
  
  
  
  if (touch.status())==1 and (touch.read()[0]) >0 and (touch.read()[0]) <70  and (touch.read()[1]) >90 and  (touch.read()[1]) <110: 
    lcd.circle(50, 80, 20, fillcolor= 0xf80000)
    speaker.playWAV('/sd/button.wav')
                       # 0
    num_id1="0"
   
  if (touch.status())==1 and (touch.read()[0]) >120 and (touch.read()[0]) <130  and (touch.read()[1]) >90 and  (touch.read()[1]) <110:
    lcd.circle(120, 80, 20, fillcolor= 0xf80000)
    speaker.playWAV('/sd/button.wav')#1
    
    num_id2="1"
   
    
  if (touch.status())==1 and (touch.read()[0]) >180 and (touch.read()[0]) <200  and (touch.read()[1]) >90 and  (touch.read()[1]) <110:
    lcd.circle(190, 80, 20, fillcolor= 0xf80000)
    speaker.playWAV('/sd/button.wav')#2
   
    num_id3="2"
   
  
  if (touch.status())==1 and (touch.read()[0]) >245 and (touch.read()[0]) <270  and (touch.read()[1]) >90 and  (touch.read()[1]) <110:
    lcd.circle(270, 80, 20, fillcolor= 0xf80000)
    speaker.playWAV('/sd/button.wav')
   
    num_id4="3"
    
 
  if (touch.status())==1 and (touch.read()[0]) >0 and (touch.read()[0]) <65  and (touch.read()[1]) >150 and  (touch.read()[1]) <170:
    lcd.circle(50, 145, 20, fillcolor= 0xf80000)
    speaker.playWAV('/sd/button.wav')
    
    num_id5="4"
    
    
    
  if (touch.status())==1 and (touch.read()[0]) >110 and (touch.read()[0]) <140  and (touch.read()[1]) >150 and  (touch.read()[1]) <170:
    lcd.circle(120, 145, 20, fillcolor= 0xf80000)
    speaker.playWAV('/sd/button.wav')
    
    num_id6="5"
   
  
  if (touch.status())==1 and (touch.read()[0]) >170 and (touch.read()[0]) <210  and (touch.read()[1]) >145 and  (touch.read()[1]) <165:
    lcd.circle(190, 145, 20, fillcolor= 0xf80000)
    speaker.playWAV('/sd/button.wav')
    
    num_id7="6"
    
  
  if (touch.status())==1 and (touch.read()[0]) >240 and (touch.read()[0]) <280  and (touch.read()[1]) >145 and  (touch.read()[1]) <165:
    lcd.circle(270, 145, 20, fillcolor= 0xf80000)
    speaker.playWAV('/sd/button.wav')
  
    num_id8="7"
    
    
  if (touch.status())==1 and (touch.read()[0]) >240 and (touch.read()[0]) <280  and (touch.read()[1]) >200 and  (touch.read()[1]) <300:
    speaker.playWAV('/sd/button.wav')
    lcd.clear()
    login_id=str(num_id1)+str(num_id2)+num_id3+num_id4+num_id5+num_id6+num_id7
    lcd.print("***", 150, 200, 0xffffff)
    if login_password==login_id:
      
      
      lcd.print("DEVICE ACTIVATED", 65, 100, 0xaaff82)
      speaker.playWAV('/sd/welcome.wav')
      wait(2)
      lcd.clear()
      lcd.print("| WELCOME |", 90, 100, 0xffffff)
      wait(2)
      lcd.clear()
      lcd.print("CREATING FILES...", 0, 100, 0xffffff)
      wait(3)
      lcd.clear()
      sd_id_write_s()
      sd_write_s()
      sd_date_write_s()
      login_id=""
      num_id1=""
      num_id2=""
      num_id3=""
      num_id4=""
      num_id5=""
      num_id6=""
      num_id7=""
      lcd.print("Files created", 0, 80, 0xffffff)
      lcd.print("Don't replace sd for this device", 0, 100, 0xffffff)
      wait(5)
      login_flag=0
      #Activate_status=1
      lcd.clear()
      nvs.write_str(str('2'), '1')
      home_screen()
     
    else:
      lcd.print("LOGIN FAILED", 100, 100, 0xffffff)
      speaker.playWAV('/sd/warning.wav')
      
      wait(1)
      login_id=""
      num_id1=""
      num_id2=""
      num_id3=""
      num_id4=""
      num_id5=""
      num_id6=""
      num_id7=""
      lcd.clear()
    







  
   
  









    
    
    
    
    
    
    
    
 
  
  
