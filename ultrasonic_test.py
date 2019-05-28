import ev3dev.ev3 as ev3
from threading import Thread
from time import sleep
ir_right=ev3.InfraredSensor('in3')
ir_left=ev3.UltrasonicSensor('in1')
ir_left.mode="US-DIST-CM"
ir_right.mode='IR-PROX'
color=ev3.ColorSensor() #in2
color.mode='COL-COLOR'
while True:
    dist1=ir_right.value()
    dist2=ir_left.value()/10
    if dist1<=80 or dist2<60:
        print ('True')
        if color.value()!=6:
            
            print("Drive")
        else:
            print("Stop")

    else:
        print("Far", dist1)
        print("Close", dist2)
        if color.value()!=6:
            
            print("Search")
        else:
            print("Stop")

    sleep(1)
    
    
    