from machine import Pin
from utime import sleep

RL = Pin(21, Pin.OUT)
AC = Pin(20, Pin.OUT)
RR = Pin(19, Pin.OUT)

start_btn = Pin(22, Pin.IN, Pin.PULL_DOWN)
stop_btn = Pin(27, Pin.IN, Pin.PULL_DOWN)


while True:
    RL.value(0)
    RR.value(0)
    AC.value(0)
    
    if start_btn.value():

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
            if stop_btn.value() == 1:
                break
            
            else:
                RL.value(1)
                RR.value(0)
                sleep(0.4)
    
                RL.value(0)
                RR.value(1)
                sleep(0.4)
            

                        
