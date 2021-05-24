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
    straight_line_distance(-3, -150, 200)
    straight_line_distance(0, -170, 580)
    wait(300)
    straight_line_distance(-2, -25, 208)
    straight_line_distance(0, 100, 180)
    straight_line_distance(-45, -100, 152)
    turn(0, 2)
    #straight_line_distance(0, -100, 40)
    follow_line_distance_right(-150, 100)
    straight_line_distance(0, -180, 110)
    straight_line_distance(-45, -100, 35)
    straight_line_distance(-1, -120, 510)
    #straight_line_distance(0, -100, 20)
    right_mission_motor.run_time(-800, 3800)
    #straight_line_distance(0, 200, 590)
    #straight_line_distance(-40, 60, 100)
    #straight_line_distance(-40, 100, 130)
    #left_mission_motor.run_time(-800, 1700) 
    #straight_line_distance(-40, -100, 30)
    #turn(0, 2)
    straight_line_distance(0, 200, 200)
    straight_line_distance(0, 1000, 1800)