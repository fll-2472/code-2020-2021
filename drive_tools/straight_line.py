from pybricks.tools import StopWatch
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port
from essential.Object_creator import gyro
from essential.Object_creator import drive_base

K_P = 20 
    
def p_controller(set_point):
    return K_P * (set_point - gyro.angle())


def straight_line(angle, speed, duration):
    timer = StopWatch()

    while timer.time() <= duration: 
        fix_amount=p_controller(angle)
        drive_base.drive(speed, -fix_amount) 

def straight_line_distance(angle, speed, distance):
    drive_base.reset()
    
    while abs(drive_base.distance()) <= distance:
        fix_amount=p_controller(angle, gyro)
        drive_base.drive(speed, -fix_amount)  


