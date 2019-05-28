import ev3dev.ev3 as ev3
from ev3dev.ev3 import Leds
leds=Leds()
from time import sleep
from threading import Thread
btn=ev3.TouchSensor() #in4
lcd=ev3.Screen()
motor_right=ev3.LargeMotor('outA')
motor_left=ev3.LargeMotor('outB')
ir_right=ev3.InfraredSensor('in3')
ir_left=ev3.UltrasonicSensor('in1')
ir_left.mode="US-DIST-CM"

ir_right.mode='IR-PROX'

color=ev3.ColorSensor() #in2
color.mode='COL-COLOR'
lcd.draw.text((20,20), 'System init success', fill='black')
lcd.update()
lcd.clear()



def dist_measure():
    while True:
        
        
        left_measure=ir_left.value()/10    
        right_measure=ir_right.value()
        print ('Close', left_measure)
        print('Far',right_measure)
        
        if right_measure<=60 or left_measure<=60 :
            return True
        #elif left_measure<=40:
            #return 'Left'
        #elif right_measure<=40:
            #return 'Right'
        else:
            return False
while True:
    if btn.is_pressed:
        
        
            lcd.draw.text((20,20), 'Sleeping', fill='black')
            lcd.update()
            print('sleeping...')
            measure_thread=Thread(target=dist_measure)
            measure_thread.start()
            sleep(5)
            lcd.clear()
            while not btn.is_pressed:
                if dist_measure()==True:
                    while dist_measure()==True:
                        
                        if color.value()!=1:
                            print("True drive")
                            leds.set_color(Leds.LEFT,Leds.GREEN)
                            leds.set_color(Leds.LEFT, Leds.GREEN)
                            motor_left.run_forever(speed_sp=900)
                            motor_right.run_forever(speed_sp=900)
                        else:
                            print("True back")
                            motor_left.stop(stop_action="brake")
                            motor_right.stop(stop_action='brake')
                            motor_left.run_timed(time_sp=1, speed_sp=-750)
                            motor_right.run_timed(time_sp=1, speed_sp=-750)


                    motor_left.stop(stop_action="coast")
                    motor_right.stop(stop_action='coast')
                elif dist_measure()==False:
                    while dist_measure()==False:
                        
                        if color.value()!=1:
                            print("True search")
                            leds.set_color(Leds.LEFT, Leds.ORANGE)
                            leds.set_color(Leds.LEFT, Leds.ORANGE)
                            motor_left.run_forever(speed_sp=-700)
                            motor_right.run_forever(speed_sp=700)
                        else:
                            print("False Back")
                            motor_left.stop(stop_action="brake")
                            motor_right.stop(stop_action='brake')
                            motor_left.run_timed(time_sp=1, speed_sp=-750)
                            motor_right.run_timed(time_sp=1, speed_sp=-750)

                    motor_left.stop(stop_action="coast")
                    motor_right.stop(stop_action='coast')
    else:
        print("Waiting for button")
        lcd.draw.text((20,20), 'Waiting for button press', fill='black' )


    
    








