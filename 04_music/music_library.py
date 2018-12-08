import RPi.GPIO as gpio
import time,sys

def library (number):
   gpio.setmode(gpio.BOARD)
   gpio.setup(18,gpio.OUT)
   ti=0
   tim=1
   music=gpio.PWM(18,262)
   music.start(100)
   music.ChangeDutyCycle(50)
   while True:
        abc=number[ti:tim]
        if abc=='0':
           music.ChangeDutyCycle(100)
           time.sleep(0.01)
           music.ChangeDutyCycle(50)
        elif abc=='1':
           music.ChangeFrequency(523)
           time.sleep(0.5)
        elif abc=='2':
           music.ChangeFrequency(587)
           time.sleep(0.5)
        elif abc=='3':
           music.ChangeFrequency(659)
           time.sleep(0.5)
        elif abc=='4':
           music.ChangeFrequency(698)
           time.sleep(0.5)
        elif abc=='5':
           music.ChangeFrequency(784)
           time.sleep(0.5)
        elif abc=='6':
           music.ChangeFrequency(880)
           time.sleep(0.5)
        elif abc=='7':
           music.ChangeFrequency(988)
           time.sleep(0.5)
        elif abc=='a':
           music.ChangeFrequency(1046)
           time.sleep(0.5)
        elif abc=='b':
           music.ChangeFrequency(1175)
           time.sleep(0.5)
        elif abc=='c':
           music.ChangeFrequency(1318)
           time.sleep(0.5)
        elif abc=='d':
           music.ChangeFrequency(1397)
           time.sleep(0.5)
        elif abc=='e':
           music.ChangeFrequency(1568)
           time.sleep(0.5)
        elif abc=='f':
           music.ChangeFrequency(1760)
           time.sleep(0.5)
        elif abc=='g':
           music.ChangeFrequency(1976)
           time.sleep(0.5)
        elif abc=='':
            music.stop()
            sys.exit()
        ti=ti+1
        tim=tim+1
            
        
