from machine import Pin
from utime import sleep

RL = Pin(21, Pin.OUT)
AC = Pin(20, Pin.OUT)
RR = Pin(19, Pin.OUT)

#version 2 with PULL_UP on pins

start_btn = Pin(22, Pin.IN, Pin.PULL_UP)
stop_btn = Pin(27, Pin.IN, Pin.PULL_UP)


while True:
    RL.value(0)
    RR.value(0)
    AC.value(0)
    
    if start_btn.value() == 0:

        AC.value(1)
        sleep(4)
    
        AC.value(0)
        RL.value(1) 
        RR.value(1)
        sleep(0.4)
    
        AC.value(0)
        RL.value(0)
        RR.value(0)
        sleep(0.25)
        
        while True:
            if stop_btn.value() == 0:
                break
            
            else:
                RL.value(1)
                RR.value(0)
                sleep(0.4)
    
                RL.value(0)
                RR.value(1)
                sleep(0.4)
            

                        
