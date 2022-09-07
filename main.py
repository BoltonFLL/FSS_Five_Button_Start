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

# All initialization is done now define five functions, one associated with each button

def button_up():  # Put up button code below this line *************
    
    print("button_up done")
    # End of button_up function ****************************************



def button_right():  # Put right button code below this line ********

    print("button_right done")
    # End of button_right function ****************************************



def button_down():   # Put down button code below this line *********
    
    print("button_down done")
    # End of button_down function ****************************************



def button_left():  # Put left button code below this line **********

    print("button_left done")
    # End of button_left function **************************************** 



def button_center():  # Put center button code below this line ******
    
    print("button_center done")
    # End of button_center function ****************************************



def setup_screen():    # Set up screen for buttons each time it's needed
    ev3.screen.clear()
    ev3.screen.draw_text(70,4,"Up")
    ev3.screen.draw_text(0,55,"Left     Center    Right")
    ev3.screen.draw_text(60,100,"Down")

# End of function definitions ****************************************


setup_screen()  # Display programs to select

while True:   # Wait for any button to be selected

    pressed = []  # Check if a button has been pressed
    while len(pressed) != 1:  # Loop until a button is pressed
        pressed = ev3.buttons.pressed()
    button = pressed[0]  # Remember which button was pressed
    ev3.screen.clear()  # Clear the screen so it is cleabn for selected program
    ev3.speaker.beep(1500, 100)  # Let user know a button was pressed

    # Now wait for the button to be released before starting selected code
    while any(ev3.buttons.pressed()):  # Don't start new program until button released
        pass

    # Test each button in turn to see which was pressed
    if button == Button.UP:    # Test if up button pressed   
        ev3.speaker.beep(200, 100)  # Make a unique beep for up button
        ev3.screen.clear()     # Clear the screen
        button_up()            # Call function associated with up button
        setup_screen()  # Set up the screen for next action  

    elif button == Button.RIGHT:  # All selections use same logic as up button 
        ev3.speaker.beep(400, 100)     
        ev3.screen.clear()   
        button_right()           
        setup_screen()  

    elif button == Button.DOWN:  # All selections use same logic as up button
        ev3.speaker.beep(600, 100)
        ev3.screen.clear()
        button_down()
        setup_screen()

    elif button == Button.LEFT:  # All selections use same logic as up button
        ev3.speaker.beep(800, 100)
        ev3.screen.clear()
        button_left()
        setup_screen()

    elif button == Button.CENTER:  # All selections use same logic as up button
        ev3.speaker.beep(1000, 100)
        ev3.screen.clear()
        button_center()
        setup_screen()

    

