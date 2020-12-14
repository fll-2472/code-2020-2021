from pybricks.tools import StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port

def p_controller(SET_POINT, K_P, gyro):
    return K_P * (SET_POINT - gyro.angle())


def straight_line(angle, speed, duration, drive_base, gyro):
    timer = StopWatch()

    while timer.time() <= duration: 
        fix_amount=p_controller(angle, 10, gyro)
        drive_base.drive(speed, -fix_amount)   


