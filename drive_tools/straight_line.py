from pybricks.tools import StopWatch
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port
from essential.Object_creator import gyro, screen
from essential.Object_creator import drive_base

K_P = 20 
    
def p_controller(set_point, gyro):
    return K_P * (set_point - gyro.angle())


def straight_line(angle, speed, duration):
    timer = StopWatch()
    while timer.time() <= duration: 
        screen.clear()
        
        screen.print(gyro.angle())

        fix_amount=p_controller(angle, gyro)
        drive_base.drive(speed, -fix_amount)   
    
def straight_line_distance(angle, speed, distance):
    drive_base.reset()
    while abs(drive_base.distance()) <= distance:
        fix_amount=p_controller(angle, gyro)

        screen.print(gyro.angle())

        drive_base.drive(speed, -fix_amount)    
    drive_base.stop()  

def straight_line_light_white(angle, speed, color_sensor):
    drive_base.reset()
    while color_sensor.reflection() >= 60:
        fix_amount=p_controller(angle, gyro)

        drive_base.drive(speed, -fix_amount)    
    drive_base.stop()  

def straight_line_light_black(angle, speed, color_sensor):
    drive_base.reset()
    while color_sensor.reflection() <= 10:
        fix_amount=p_controller(angle, gyro)

        drive_base.drive(speed, -fix_amount)    
    drive_base.stop()  