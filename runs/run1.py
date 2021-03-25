from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor, gyro
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from drive_tools.straight_line import straight_line_distance, straight_line
from drive_tools.turn import turn

def run_1():
    gyro.reset_angle(0)
    straight_line_distance(0, -300, 510)
    straight_line_distance(0, 100, 110)
    turn(20, 3)
    straight_line_distance(-440, -5000, 310)
    straight_line_distance(-440, 100, 100)
    straight_line_distance(40, -100, 250)
   