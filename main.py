#!/usr/bin/env pybricks-micropython

# ---------------------------------------------------------------
# 2022 Sturgeon 3000
#
# We started with a copy of our 2021 code
#
# Change log now bing in Git Hub
#  
# ---------------------------------------------------------------
 
# ---------------------------------------------------------------
# Initialization section from 2021
#  Mostly from example code
# ---------------------------------------------------------------

# these are the libraries of code writen by pybricks (API)
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop, Direction, Button, Color 
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# we got and Ian changed this code from the samples
from menu import wait_for_button
from menu import make_screen

RIGHT_SENSOR_WHITE=71
LEFT_SENSOR_WHITE=74
RIGHT_SENSOR_BLACK=6
LEFT_SENSOR_BLACK=7

# Initialize the EV3.
ev3 = EV3Brick()

# Initialize the motors.
am = Motor(Port.A)
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)

# Initialize the sensors 
line_sensor = right_line_sensor = ColorSensor(Port.S1)
left_line_sensor = ColorSensor(Port.S4)

# Initialize the drive base. <comment about Sturgeon 3000 being 111mm>
robot = DriveBase(left_motor, right_motor, wheel_diameter=90, axle_track=111)

# ipk did creating and Initialize variables for speed and acceleration
# (209, 837, 400, 1600)
straight_speed = 209
straight_acceleration = 837 #837
turn_rate = 50 #400 
turn_acceleration = 1600

# menu variables by Ian
run_number = 0
last_run_number = 3 

# ---------------------------------------------------------------
# These are our reusable functions from 2021
# ---------------------------------------------------------------

def set_straight_speed(speed):
    # ---------------------------------------------------------------
    # This is the reusable function for changing the straight drive speed
    #  Example: straightspeed(100) to change speed to 100 mm/second
    #  from 2021
    # ---------------------------------------------------------------

    straight_speed = speed
    robot.stop()
    robot.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)    
  
def forklift_move(direction,time):
    # ---------------------------------------------------------------
    # This is the function for the forklift retrofitted from 2020 
    #  code from 2021 - written by Koen
    # forklift_move("up",2500)
    # forklift_move("down",2500)
    # ---------------------------------------------------------------

    speed=200
    if direction == "down":
        speed = speed * -1

    am.run_time(speed,time)

def dispense():
    # ---------------------------------------------------------------
    # This is the reusable function for the 2021 package dispenser
    #  to be used in 2022 for energy units
    # ---------------------------------------------------------------

    am.run_time(-2000,700)# speed and time, negative is dispense
    am.run_time(2000,700)# speed and time, positive is reset

def follow_line2( distance, speed = 80, right_or_left_sensor = "right", side_of_line = "left", Kp = 0.8, Ki = 0.0008, Kd =.001):
    '''
    Version 2 of the Digital Magic function to follow a line.  This version by Koen on 12-18-2020 to make it a PID line follower
    and use 2 sensors!

    Parameters:
        distance - mm you want robot to travel
        speed - speed of robot.
        right_or_left_sensor - which sensor are you using ("right" or "left")
        side_of_line = which side of black line are you following ("right" or "left") 
        Kp - proportional gain
        Ki - integral gain 
        Kd - derivative gain      
    '''

    integral = 0
    derivative = 0
    last_error = 0

        
    if (right_or_left_sensor == "right"):
        sensor = right_line_sensor
        target = (RIGHT_SENSOR_WHITE + RIGHT_SENSOR_BLACK) / 2
    else:
        sensor = left_line_sensor
        target = (LEFT_SENSOR_WHITE + LEFT_SENSOR_BLACK) / 2

    robot.reset()
    robot.stop()

    # PID feedback loop
    while robot.state()[0] < distance:
        
        error = sensor.reflection() - target
        integral = integral + error
        derivative = error - last_error
        
        # this is where the digital magic of a PID line follower happens
        turn_rate = Kp * error + Ki * integral + Kd * derivative
        if side_of_line == "left":
            #print(speed - turn_rate)
            right_motor.run(speed - turn_rate)
            left_motor.run(speed + turn_rate)
        else:
            right_motor.run(speed + turn_rate)
            left_motor.run(speed - turn_rate)
        last_error = error
        wait(10)

    robot.stop()  #make sure this is outside the loop!!

# ---------------------------------------------------------------
# These are our new reusable functions for 2022
# ---------------------------------------------------------------

def wheel_clean():
    # wheel cleaner by Calvin Hill 11-13-22
    robot.straight(2000)

# ---------------------------------------------------------------
# Our 2022 Super Powered mission functions start here
# ---------------------------------------------------------------

def tv_wind():
    # tv windmill by Calvin Hill 11-13-22

    #drive up and do tv. this should give us our first 20 points.
    set_straight_speed(500)
    robot.straight(380)
    set_straight_speed(100)
    robot.straight(90)

    #drive over and push windmill
    set_straight_speed(500)
    robot.straight(-140)
    robot.turn(-45)
    robot.straight(430)
    robot.turn(90)
    robot.straight(250)

    #push on windmill 3 moretimes extra in case one stays put
    robot.straight(-40)
    robot.straight(50)
    robot.straight(-40)
    robot.straight(50)
    robot.straight(-40)
    robot.straight(50)

#Essie Dino() Oil() Power() Storage() 

# ---------------------------------------------------------------
# This is the menu system (changed from the example code by Ian)
# ---------------------------------------------------------------

ev3.speaker.beep(100)
ev3.speaker.beep(900)
ev3.speaker.beep(100)
ev3.speaker.beep(900)


while True:
    # Draw screen based on what run we are on
    if run_number == 0:
        make_screen(ev3,"TV Windmill"," -  -  -  -  -  -  + ","", ""," "," ")

    elif run_number == 1:
        make_screen(ev3,"Dino"," -  -  -  -  -  -  + ","", ""," "," ")

    elif run_number == 2:
        make_screen(ev3,"Beep"," -  -  -  -  -  -  + ","", ""," "," ")

    elif run_number == 3:
        make_screen(ev3,"Beep"," -  -  -  -  -  -  + ","", ""," "," ")

    elif run_number == 4:
        make_screen(ev3,"Beep"," -  -  -  -  -  -  + ","", ""," "," ")

    elif run_number == 5:
        make_screen(ev3,"Clean Wheels"," -  -  -  -  -  -  + ","", ""," "," ")


    # Wait for one button to be selected.
    button = wait_for_button(ev3)

    # Now you can do something, based on which button was pressed.
    if button == Button.LEFT:
        if run_number > 0: 
            run_number = run_number - 1
        else:
            run_number = last_run_number

    elif button == Button.RIGHT:
        if run_number < last_run_number: 
            run_number = run_number + 1
        else:
            run_number = 0

    elif button == Button.UP:
        if run_number > 0: 
            run_number = run_number - 1
        else:
            run_number = last_run_number

    elif button == Button.DOWN:
        if run_number < last_run_number: 
            run_number = run_number + 1
        else:
            run_number = 0

    elif button == Button.CENTER:
        if run_number == 0:
            tv_wind()
        elif run_number == 1:
            ev3.speaker.beep(200)

        elif run_number == 2:
            ev3.speaker.beep(200)

        elif run_number == 3:
            ev3.speaker.beep(200)

        elif run_number == 4:
            ev3.speaker.beep(200)

        elif run_number == 5:
            wheel_clean()

                    

        # Move on to next run screen
        if run_number < last_run_number: 
            run_number = run_number + 1
        else:
            run_number = 0  