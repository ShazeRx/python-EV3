import ev3dev.ev3 as ev3
from ev3dev.ev3 import Leds
leds=Leds()
from time import sleep
from threading import Thread
btn=ev3.TouchSensor() #in4
lcd=ev3.Screen()
motor_right=ev3.LargeMotor('outA')
motor_left=ev3.LargeMotor('outC')
ir_right=ev3.InfraredSensor('in3')
ir_left=ev3.UltrasonicSensor('in1')
ir_left.mode="US-DIST-CM"

ir_right.mode='IR-PROX'

color=ev3.ColorSensor() #in2
color.mode='COL-COLOR'
while True:
    print("Waiting for button")
    if btn.is_pressed:
        break
sleep(5)



while True:
    if ir_left.value()/10<80 or ir_right.value()<65:
        print(ir_left.value()/10)
        print(ir_right.value())
        print("True")
        motor_left.stop(stop_action="brake")
        motor_right.stop(stop_action="brake")
        
        while ir_left.value()/10<80 or ir_right.value()<65:

            
            if color.value()!=6:
                motor_left.run_forever(speed_sp=900)
                motor_right.run_forever(speed_sp=850)
            else:
                motor_left.run_timed(time_sp=500, speed_sp=-900)
                motor_right.run_timed(time_sp=500, speed_sp=-900)
                sleep(0.5)

    else:
        if color.value()!=6:
                motor_left.run_forever(speed_sp=-500, stop_action="brake")
                motor_right.run_forever(speed_sp=500, stop_action="brake")
                print("False")
        else:
            motor_left.run_timed(time_sp=500, speed_sp=-900)
            motor_right.run_timed(time_sp=500, speed_sp=-900)
            sleep(0.5)
        
        