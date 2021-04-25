from pybricks.ev3devices import Motor
from essential.Object_creator import left_mission_motor, gyro
from essential.Object_creator import right_color_sensor, left_color_sensor
from essential.Object_creator import right_motor, left_motor
from pybricks.tools import wait
from drive_tools.straight_line import straight_line, straight_line_distance, straight_line_light_black
from drive_tools.turn import turn
from essential.Object_creator import DriveBase
from essential.Object_creator import right_mission_motor
from drive_tools.follow_line import follow_line_distance_left, follow_line_distance_right, follow_line_left, follow_line_right

def run_3():
  gyro.reset_angle(0)
  straight_line_distance(-15, -200, 200)
  follow_line_distance_right(-200, 940)
  straight_line_distance(-60, 100, 260)
  straight_line_distance(-85, -200, 150)
  follow_line_distance_right(-100, 450)
  straight_line_distance(-35, -100, 90)
  straight_line_distance(-35, 100, 120)
  straight_line_distance(-60, -100, 140)
  turn(-190, 2)
  right_mission_motor.run_time(200, 1800)
  straight_line_distance(-205, 100, 80)
  straight_line_distance(-220, -500, 150)
  straight_line_distance(-195, 100, 230)
  straight_line_distance(-180, -100, 300)
  straight_line_distance(-210, -2000, 10000)