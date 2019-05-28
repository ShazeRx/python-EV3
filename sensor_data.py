import ev3dev.ev3 as ev3
from threading import Thread
from time import sleep

color_left=ev3.ColorSensor('in2') 
color_right=ev3.ColorSensor('in4')
color_left.mode="COL-COLOR"
color_right.mode="COL-COLOR"

while True:
    
    print('Left',color_left.value())
    print('Right',color_right.value())
    sleep(2)