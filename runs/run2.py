from pybricks.ev3devices import (Motor)
from essential.Object_creator import left_mission_motor, right_mission_motor
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from drive_tools.straight_line import straight_line, straight_line_distance
from drive_tools.follow_line import follow_line_left, follow_line_right
from essential.Object_creator import gyro
from pybricks.tools import wait

def run_2():
    gyro.reset_angle(0)
    straight_line_distance(0, -100, 800)
    wait(300)
    straight_line_distance(-3, -25, 208)
    straight_line_distance(0, 100, 180)
    straight_line_distance(-45, -100, 185)
    straight_line_distance(0, -100, 90)
    straight_line_distance(0, -100, 400)
    straight_line_distance(-4, -100, 200)
    straight_line_distance(0, -100, 20)
    right_mission_motor.run_time(-800, 5200)
    straight_line_distance(0, 200, 570)
    straight_line_distance(-40, 60, 100)
    straight_line_distance(-40, 100, 130)
    left_mission_motor.run_time(-800, 2500) 
    straight_line_distance(-40, -100, 60)
    straight_line_distance(0, 200, 1300)