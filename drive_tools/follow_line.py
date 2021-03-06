from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from essential.Object_creator import right_color_sensor, left_color_sensor, screen
from pybricks.tools import StopWatch
from essential.Object_creator import drive_base


BLACK = 6
WHITE = 70
setpoint = (BLACK + WHITE) / 2

K_P = 3.65

def follow_line_right(speed, duration): 
    timer=StopWatch() 
    while timer.time() <=duration:
        deviation = right_color_sensor.reflection() - setpoint
        turn_rate = K_P * deviation
        screen.print(right_color_sensor.reflection())

        drive_base.drive(speed, turn_rate)

        wait(10)

def follow_line_left(speed, duration):
    while timer.time() <duration:
        deviation = color_sensor.reflection() - setpoint

        turn_rate = K_P * deviation

        drive_base.drive(speed, turn_rate)

        wait(10)

def follow_line_distance_right(speed, distance): 
    timer=StopWatch()
    drive_base.reset() 
    while abs(drive_base.distance()) <= distance:
        deviation = right_color_sensor.reflection() - setpoint
        turn_rate = K_P * deviation
        screen.print(right_color_sensor.reflection())

        drive_base.drive(speed, turn_rate)

        wait(10)

def follow_line_distance_left(speed, distance): 
    timer=StopWatch() 
    drive_base.reset()
    while abs(drive_base.distance()) <= distance:
        deviation = left_color_sensor.reflection() - setpoint
        turn_rate = K_P * deviation
        screen.print(left_color_sensor.reflection())

        drive_base.drive(speed, turn_rate)

        wait(10)
