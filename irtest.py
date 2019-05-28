import ev3dev.ev3 as ev3
from threading import Thread
ir_left=ev3.UltrasonicSensor('in1')
ir_left.mode="US-DIST-CM"

def measure():
    while True:
        dist=ir_left.value()
        auth(dist)
    

thread=Thread(target=measure)
thread.start()

def auth(dist):
    if dist==2550:
        dist=0
        
    else:
        print(dist)
        
        



