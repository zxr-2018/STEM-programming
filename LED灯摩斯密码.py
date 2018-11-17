import RPi.GPIO as gpio
import time,sys

gpio.setmode(gpio.BOARD)
gpio.setup(16,gpio.OUT)
abc2=input("What's your name?")
print("Hello,",abc2,"!")
time.sleep(0.5)
print("Morse code is already.")
ti=0
tim=1
while tim<100:
   gpio.setmode(gpio.BOARD)
   gpio.setup(16,gpio.OUT)
   abc1=abc2[ti:tim]
   if abc1 == 'a' or abc1 =='A':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
     
   elif abc1 == 'b' or abc1 =='B':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
   elif abc1 == 'c' or abc1 =='C':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
         
   elif abc1 == 'd' or abc1 =='D':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
   elif abc1 == 'e' or abc1 =='E':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
   elif abc1 == 'f' or abc1 =='F':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
   elif abc1 == 'g' or abc1 =='G':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
   elif abc1 == 'h' or abc1 =='H':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
            
   elif abc1 == 'i' or abc1 =='I':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
   elif abc1 == 'j' or abc1 =='J':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
              
   elif abc1 == 'k' or abc1 =='K':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
   elif abc1 == 'l' or abc1 =='L':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
   elif abc1 == 'm' or abc1 =='M':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
   elif abc1 == 'n' or abc1 =='N':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
   elif abc1 == 'o' or abc1 =='O':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
   elif abc1 == 'p' or abc1 =='P':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
   elif abc1 == 'q' or abc1 =='Q':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
   
   elif abc1 == 'r' or abc1=='R':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
   
   elif abc1 == 's' or abc1 =='S':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
   
   elif abc1 == 't' or abc1 =='T':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
    
   elif abc1 == 'u' or abc1 =='U':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
      
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
   
   elif abc1 == 'v' or abc1 =='V':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
   
   elif abc1 == 'w' or abc1 =='W':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
   
   elif abc1 == 'x' or abc1 =='X':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
   
   elif abc1 == 'y' or abc1 =='Y':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
   
   elif abc1 == 'z' or abc1 =='Z':
      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.7)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)

      gpio.output(16,gpio.HIGH)
      time.sleep(0.3)
      gpio.output(16,gpio.LOW)
      time.sleep(0.18)
   
   gpio.cleanup()
   tim=tim+1
   ti=ti+1
   
   

