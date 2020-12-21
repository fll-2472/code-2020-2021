from pybricks.tools import StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port

K_P = 70
def p_controller(set_point, gyro):
    return K_P * (set_point - gyro.angle())


def turn(angle, speed, threshold, drive_base, gyro):
    while angle - threshold < gyro.angle() < angle + threshold: 
        fix_amount=p_controller(angle, gyro)
        drive_base.drive(speed, -fix_amount)

turn(30 200 2 drive_base gyro)