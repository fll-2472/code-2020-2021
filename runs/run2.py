from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor, right_mission_motor
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from drive_tools.straight_line import straight_line, straight_line_distance
from drive_tools.follow_line import follow_line_left, follow_line_right
from essential.Object_creator import gyro

def run_2():
    gyro.reset_angle(0)
    straight_line_distance(0, -100, 800)
    left_mission_motor.run_time(-800, 2500)
    # left_mission_motor.run_time(800, 2500)
    straight_line_distance(-3, -25, 210)
    straight_line_distance(0, 100, 180)
    straight_line_distance(-45, -100, 190)
    straight_line_distance(0, -100, 90)
    straight_line_distance(0, -100, 400)
    straight_line_distance(0, -100, 260)
    right_mission_motor.run_time(-800, 3200)
    straight_line_distance(0, 200, 2000)