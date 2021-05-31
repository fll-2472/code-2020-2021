from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor, right_mission_motor
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from drive_tools.straight_line import straight_line, straight_line_distance
from drive_tools.follow_line import follow_line_left, follow_line_right, follow_line_distance_left, follow_line_distance_right
from essential.Object_creator import gyro
from pybricks.tools import wait
from drive_tools.turn import turn

def run_2():
    gyro.reset_angle(0)
    straight_line_distance(-3, -250, 200)
    straight_line_distance(0, -250, 580)
    wait(300)
    straight_line_distance(-2, -25, 208)
    straight_line_distance(0, 100, 180)
    straight_line_distance(-45, -120, 152)
    turn(0, 2)
    follow_line_distance_right(-250, 100)
    straight_line_distance(0, -250, 110)
    straight_line_distance(-45, -120, 18)
    straight_line_distance(-1, -250, 485)
    right_mission_motor.run_time(-800, 3100)
    straight_line_distance(0, 250, 200)
    straight_line_distance(0, 10000, 1800)
