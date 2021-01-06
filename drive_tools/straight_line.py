from pybricks.tools import StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port
from essential.Object_creator import gyro

K_P = 20 
    
def p_controller(set_point):
    return K_P * (set_point - gyro.angle())


def straight_line(angle, speed, duration, drive_base):
    timer = StopWatch()

    while timer.time() <= duration: 
        fix_amount=p_controller(angle)
        drive_base.drive(speed, -fix_amount)   


