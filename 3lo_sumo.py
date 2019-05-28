import ev3dev.ev3 as ev3
from ev3dev.ev3 import Leds
leds=Leds()
from time import sleep
from threading import Thread

lcd=ev3.Screen()
motor_right=ev3.LargeMotor('outB')
motor_left=ev3.LargeMotor('outA')
ir=ev3.InfraredSensor('in3')



ir.mode='IR-PROX'

color_left=ev3.ColorSensor('in4')
color_right=ev3.ColorSensor('in2') 
color_right.mode='COL-COLOR'
color_left.mode="COL-COLOR"

lcd.draw.text((20,20), 'System init success', fill='black')
lcd.update()
lcd.clear()
sleep(5)

def dist_measure():
    measue=ir.value()


    if measue<=60:
        return True
    else:
        return False


while True:
    try:
        if color_left.value()==1 and color_right.value()==1:
            if dist_measure()==True:
                    while True:
                        print("Found!")
                        
                        leds.set_color(Leds.LEFT,Leds.GREEN)
                        leds.set_color(Leds.LEFT, Leds.GREEN)
                        motor_left.run_forever(speed_sp=-900)
                        motor_right.run_forever(speed_sp=-900)
                        if not color_left.value()!=1 or color_right.value()!=1:
                            print("FOund line")
                            break
                            
                    
            
            else:
                motor_left.run_forever(speed_sp=-900)
                motor_right.run_forever(speed_sp=900)
            
                print("Seeking")
        else:
            motor_left.stop(stop_action="brake")
            motor_right.stop(stop_action='brake')
            motor_left.run_timed(time_sp=1000, speed_sp=900,stop_action='brake')
            motor_right.run_timed(time_sp=1000, speed_sp=900,stop_action='brake')
            sleep(1)
            print("Back")

            
            
    except KeyboardInterrupt:
        motor_left.stop(stop_action="brake")
        motor_right.stop(stop_action='brake')



