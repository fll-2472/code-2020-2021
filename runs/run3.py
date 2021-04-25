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
  # straight_line_light_black(0, -1000, right_color_sensor)
  straight_line_distance(-20, -100, 30)
  straight_line_distance(0, -200, 870)
  turn(-90, 2)
  straight_line_distance(-20, -100, 130)
  straight_line_distance(-90, 100, 80)
  straight_line_distance(-75, -100, 60)
  straight_line_distance(-90, -100, 50)
  follow_line_distance_right(-100, 420)
  straight_line_distance(-35, -100, 90)
  straight_line_distance(-35, 100, 65)
  straight_line_distance(-55, -100, 75)
  turn(-190, 2)
  right_mission_motor.run_time(200, 1300)
  straight_line_distance(-205, 100, 70)
  straight_line_distance(-205, -500, 100)
  straight_line_distance(-195, 100, 190)
  straight_line_distance(-180, -100, 70)
  follow_line_distance_left(-100, 750)
  straight_line_distance(-210, -2000, 10000)