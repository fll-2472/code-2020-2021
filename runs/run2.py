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
    left_mission_motor.run_time(800, 2500)
    straight_line_distance(0, 100, 80)
    straight_line_distance(-70, -50, 30)
    straight_line_distance(0, -100, 40)
    straight_line_distance(-13, -50, 200)
    straight_line_distance(45, 100, 100)
    straight_line_distance(0, -100, 500)
    right_mission_motor.run_time(800, -5000)
    straight_line_distance(0, 100, 2000)
 
    #gyro.reset_angle(0)
    #straight_line_distance(-15, -100, 120)
    #straight_line_distance(16, -150, 680)
    #straight_line_distance(1, -30, 280)
    #straight_line_distance(45, 100, 120)
    #straight_line_distance(0, -150, 750)
    # straight_line(0, -100, 1700)
    # straight_line(-15, -100, 500)
    # follow_line_right(-200, 400)
    # straight_line(5, -200, 2300)
    # straight_line(-5, -30, 20000)
    # straight_line(-10, 200, 3000)
 
    #gyro.reset_angle(0)
    #straight_line_distance(0, -100, 50000)
    #os.exit()