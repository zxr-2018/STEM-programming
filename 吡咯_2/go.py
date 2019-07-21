import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
IN1 =37
IN2 = 36
IN3 = 38
IN4 = 40
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

def run():
   GPIO.output(IN1, 0)
   GPIO.output(IN2, 1)
   GPIO.output(IN3, 0)
   GPIO.output(IN4, 1)
   

def back():
   GPIO.output(IN1, 1)
   GPIO.output(IN2, 0)
   GPIO.output(IN3, 1)
   GPIO.output(IN4, 0)
   

def left():
   GPIO.output(IN1, 0)
   GPIO.output(IN2, 0)
   GPIO.output(IN3, 0)
   GPIO.output(IN4, 1)
   

def right():
   GPIO.output(IN1, 1)
   GPIO.output(IN2, 0)
   GPIO.output(IN3, 0)
   GPIO.output(IN4, 0)
   
   
def stop():
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 0)
    
def cleanup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.cleanup()    

