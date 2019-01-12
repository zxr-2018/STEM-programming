# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(13,gpio.OUT)
gpio.setup(15,gpio.IN)
i=0
t=0
print("测量中......")
while i !=10:
    time.sleep(0.3)
    gpio.output(13, True)
    time.sleep(0.00001)
    gpio.output(13,False)
    while gpio.input(15) == False:
        pass
    t1 = time.time()
    while gpio.input(15) == True:
        pass
    t2 = time.time()
    a = (t2-t1) * 34000 / 2
    t = t+a
    i=i+1
d = t/10
print"你要测量的距离为 ", d," cm"
gpio.cleanup()
raw_input()
    
