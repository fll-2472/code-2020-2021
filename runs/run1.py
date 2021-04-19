from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor, gyro
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from drive_tools.straight_line import straight_line_distance, straight_line
from drive_tools.turn import turn
import os
from essential.Object_creator import drive_base
from essential.Object_creator import right_mission_motor

def run_1():
    gyro.reset_angle(0)
    straight_line_distance(0, -300, 100)
    straight_line_distance(-50, -100, 50)
    straight_line_distance(-50, -100, 70)
    straight_line_distance(17, -200, 300)
    straight_line_distance(17, 100, 50)
    turn(-25, 2)
    turn(17, 2)
    straight_line_distance(16, -1000, 200)
    drive_base.stop()