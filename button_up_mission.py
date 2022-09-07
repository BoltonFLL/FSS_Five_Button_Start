#button_up_mission

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.media.ev3dev import Font

# Initialize the EV3.
ev3 = EV3Brick()

# Initialize motors
motor_A = Motor(Port.A)
motor_B = Motor(Port.B)
motor_C = Motor(Port.C)
motor_D = Motor(Port.D)

# Initialize the drive base
robot = DriveBase(motor_B, motor_C, wheel_diameter=55.9, axle_track=89.0)

# Initialize the sensors
sensor_1 = ColorSensor(Port.S1)
sensor_4 = ColorSensor(Port.S4)

small_font = Font(size=14)  # Define font sizes to use on the screen
normal_font = Font(size=20)
ev3.screen.set_font(normal_font)

def button_up_mission():  # Put up button code below this line *************

    ev3.speaker.beep(200, 100)  # Make a unique beep for up button
    ev3.speaker.beep(200, 100)  # Make a unique beep for up button
    ev3.speaker.beep(200, 100)  # Make a unique beep for up button

    print("Now running button up")
    # End of button_up mission ****************************************
