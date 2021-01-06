from pybricks.tools import StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port
from essential.Object_creator import gyro
from essential.Object_creator import drive_base

K_P = 48
def p_controller(set_point, gyro):
    return K_P * (set_point - gyro.angle())


def turn(angle, threshold):
    while gyro.angle() <= angle - threshold or gyro.angle() >= angle + threshold: 
        fix_amount=p_controller(angle, gyro)
        drive_base.drive(0, -fix_amount)

