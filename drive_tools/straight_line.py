from pybricks.tools import StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port

K_P = 20 
    
def p_controller(set_point, gyro):
    return K_P * (set_point - gyro.angle())


def straight_line(angle, speed, duration, drive_base, gyro):
    timer = StopWatch()

    while timer.time() <= duration: 
        fix_amount=p_controller(angle, gyro)
        drive_base.drive(speed, -fix_amount)   


