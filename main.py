#!/usr/bin/env pybricks-micropython

# # -------------------------------------------------------------------------------------

# 2022 Super Powered Sturgeon 3000
#
# We started with a copy of our 2021 code!  Removed our Cargo Connect Missions 
#   and added our Super Powered missions
#
# Change log now in Git Hub!  
#   https://github.com/DigitalMagic44519/Sturgeon3000/commits?author=DigitalMagic44519
#  
# -------------------------------------------------------------------------------------
 
# -------------------------------------------------------------------------------------
# Initialization section from 2021
#  Mostly from example code
# -------------------------------------------------------------------------------------

# these are the libraries of code writen by pybricks (API)
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop, Direction, Button, Color 
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# we got this from samples and Ian changed it
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

# ipk did this creating and Initialize variables for speed and acceleration in 2021
# (209, 837, 400, 1600)
straight_speed = 209
straight_acceleration = 837 #837
turn_rate = 50 #400 
turn_acceleration = 1600

# menu variables by Ian
run_number = 0
last_run_number = 6 

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

def follow_line( distance, speed = 80, right_or_left_sensor = "right", side_of_line = "left", Kp = 0.8, Ki = 0.0008, Kd =.001):
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
    robot.straight(345)
    set_straight_speed(100)
    robot.straight(90)

    #drive over and push windmill
    set_straight_speed(500)
    robot.straight(-140)
    robot.turn(-45)
    robot.straight(420) # drive east
    robot.turn(90)
    set_straight_speed(300)
    robot.straight(200)

    #push on windmill 3 moretimes extra in case one stays put
    robot.straight(-40)
    robot.straight(50)
    robot.straight(-40)
    robot.straight(50)
    robot.straight(-40)
    robot.straight(50)

    #Pick up rechargable
    robot.straight(-230) #back up to capture rechargeable
    #robot.turn(25)
    #robot.straight(-40)
    robot.turn(-85)  # turn angle to go home
    set_straight_speed(500) # pedal to the metal
    robot.straight(-600)

    #lower the toy power dispenser a little
    #am.run_time(-400,250) 

def oil():
    # oil rig mission by Esther and Brayden
    set_straight_speed(300) 
    robot.straight(-750)
    robot.turn(53)
    robot.straight(250)

    # Pump the well 3 times
    robot.straight(-100)
    robot.straight(120)
    robot.straight(-100)
    robot.straight(120)


    # Harvest energy from solar farm
    robot.straight(-600) #TODO tends to go crooked, follow line?

    #Koen took over, then Lily as she needed to rebuild the reeper
    am.run_time(-2000,700)
    robot.straight(265)  #IAN ADJUSTED THIS IN PRACTICE WITH CLEAN WHEELS
    robot.turn(-60) # Ian adjusted this angle during practice with CLEAN wheels
    robot.straight(1000)
 
def hopper():
    #hopper fill run by Lily Hill
    #set the speed
    set_straight_speed(109)

    #drive to line 
    robot.straight(280)

    #follow line to hopper
    follow_line(520,75,"left","left")
    robot.stop()

    #pull out the drawer
    robot.straight(-300)
    set_straight_speed(500)
    robot.turn(20)
    #robot.drive(100,50)
    robot.straight(-500)
    
def power():
    # powerplant smartgrid power to x (p2x) by Calvin and Koen
    set_straight_speed(250)
    robot.straight(-400)
    robot.turn(-30)
    robot.straight(-510) #485
    robot.turn(-65) #80

    #drive to power plant
    set_straight_speed(200)
    robot.straight(280) #

    #drive ahead to p2xc
    set_straight_speed(300)
    robot.straight(-555)
    
    #slow down as we go in
    set_straight_speed(100)
    robot.straight(-30)
    wait(300)

    #drive to middle
    robot.straight(20)
    wait(300)
    robot.straight(160)

def dino():
    # dino run in 12 parsects 
    set_straight_speed(1000)
    robot.straight(2000)

def toy():
    # Toy factory mission by Ian

    #set the speed
    set_straight_speed(1000)

    #drive out to dump
    robot.straight(350)

    #lower the toy power dispenser the rest of the way
    am.run_time(-400,600) 
 
    #lift the toy power dispenser again
    am.run_time( 400,600) 

    #come back
    robot.straight(-600)


# ---------------------------------------------------------------
# This is the menu system (changed from the example code by Ian)
# ---------------------------------------------------------------

ev3.speaker.beep(100)
ev3.speaker.beep(900)
ev3.speaker.beep(100)
ev3.speaker.beep(900)

#am.run_time(-2000,750)

while True:
    # Draw screen based on what run we are on
    if run_number == 0:
        make_screen(ev3,"TV Windmill"," +  -  -  -  -  -  - ","pins", "dino head pin","dispener up"," ")

    elif run_number == 1:
        make_screen(ev3,"Toy Factory"," -  +  -  -  -  -  - ","load EUs", ""," "," ")

    elif run_number == 2:
        make_screen(ev3,"Dino Sprint"," -  -  +  -  -  -  - ","", "yell HOT","BLOWIN SNOT"," ")

    elif run_number == 3:
        make_screen(ev3,"Oil Rig"," -  -  -  +  -  -  - ","pins!", "lean right"," "," ")

    elif run_number == 4:
        make_screen(ev3,"Hopper Run"," -  -  -  -  +  -  - ","aim for black", ""," "," ")

    elif run_number == 5:
        make_screen(ev3,"Power Tower"," -  -  -  -  -  +  - ","balls first", "rt top corner","forks down","model & EU")

    elif run_number == 6:
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

    # ADD MISSION FCN CALLS HERE
    elif button == Button.CENTER:
        if run_number == 0:
            tv_wind()

        elif run_number == 1:
            toy()

        elif run_number == 2:
            dino()

        elif run_number == 3:
            oil()

        elif run_number == 4:
            hopper()

        elif run_number == 5:
            power()

        elif run_number == 6:
            wheel_clean()
          
        # Move on to next run screen
        if run_number < last_run_number: 
            run_number = run_number + 1
        else:
            run_number = 0

          
