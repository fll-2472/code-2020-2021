from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor, gyro
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from drive_tools.straight_line import straight_line_distance, straight_line
from drive_tools.turn import turn
import os
from essential.Object_creator import drive_base
def run_1():
    gyro.reset_angle(0)
    straight_line_distance(0, -300, 100)
    straight_line_distance(-50, -100, 50)
    straight_line_distance(-50, -100, 87)
    straight_line_distance(16.5, -1000, 650)
    straight_line_distance(16.5, 100, 70)
    turn(40, 2)
    turn(-340, 2)
    straight_line_distance(0, -100, 150)
    drive_base.stop()