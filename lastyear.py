# ---------------------------------------------------------------
# OUR 2021 MISSION FUNCTIONS FOR REFERENCE
# ---------------------------------------------------------------

def flip_engine():
    # ---------------------------------------------------------------
    # way more simple cargo plane only function
    # This is a simplified function from old run_number1b() that just does Flip Engine 
    # ---------------------------------------------------------------

    #set the speed
    straightspeed(109)

    #drive to line Watch Sensors
    robot.straight(280)

    #follow line (until right before the sharp turn)
    followline(550,75)
    robot.stop()
    
    #drive strait ahead then to motor
    robot.straight(210)
    robot.turn(40)
    robot.straight(46)

    # Lift the attachment fliping motor
    am.run_time(speed = -1500,time=1200)

    
    #bring it on home fast
    robot.turn(-50)
    straightspeed(500)
    robot.straight(-800)

def cargo_plane():

    #position the attachment arm
    am.run_time(speed=250,time=950)

    #must stop to change speed
    robot.stop()

    #set the speed
    straightspeed(200)

    #drive to line 
    robot.straight(655)
    ev3.speaker.beep(800)  
    
    #bring da hammer down slightly
    am.run_time(speed=1500,time=1200)

    #must stop to change speed
    robot.stop()

    #drive home fast
    straightspeed(500)
    robot.straight(-750)

def plattooning_trucks(): 
    # ---------------------------------------------------------------
    # This is the function for plattooning trucks  
    # ---------------------------------------------------------------

    #set the speed
    straightspeed(109)

    #drive to line and follow it awhile
    robot.straight(150)
    followline(200,75) 
    ev3.speaker.beep(200)  # DEBUG BEEP 1

    #turn toward the other truck.  The wait is how long it turns
    robot.drive(speed=75, turn_rate=20)
    wait(1500) #2400 ipk
    ev3.speaker.beep(400)  #DEBUG BEEP 2

    #turn less toward the other truck.  The wait is how long it turns
    robot.drive(speed=75, turn_rate=1)
    wait(1200) #2400 ipk
    ev3.speaker.beep(600)  #DEBUG BEEP 3

    #push the truck onto the latch
    straightspeed(75)
    robot.straight(120)
    ev3.speaker.beep(800)  #DEBUG BEEP 4

    #back up to push unused capacity - the wait is how long it turns
    robot.drive(speed=-1000, turn_rate=20)
    wait(1200)
    robot.straight(-300)
    robot.stop()

def plattooning_trucks2(): 

    # ---------------------------------------------------------------
    # This is 2nd version of the function for plattooning trucks testing gyro
    # ---------------------------------------------------------------

    #drive straight out and turn toward other truck and then straight again to latch
    print("Drive North")

    #gyro_straight(500, robotSpeed=150)
    robot.straight(500)

    print("Turn East")
    gyro_turn(88, speed=150)

    print("Drive East")
    #gyro_straight(400, robotSpeed=80)
    robot.straight(400)

def connect_cargo():
    # ---------------------------------------------------------------
    # This is the function for connect cargo   
    # --------------------------------------------------------------- 

    #set the speed
    straightspeed(200)

    #drive to circle 
    robot.straight(620)

    #drive back 
    robot.straight(-700)

def innovation_model(): 
    # ---------------------------------------------------------------
    # This is the function for delivering innovation model  
    # ---------------------------------------------------------------

    #set the speed
    straightspeed(130)

    #drive to circle 
    robot.straight(1130)

    #turn towards circle
    ## COACH THINKS NEED A TURN SPEED SETTER HERE HE MESSED WITH VARIABLE
    #robot.turn(-50) #12-5-21 lmh
    #robot.turn(-90)  #12-6-21 -kahk
    robot.turn(-65)  ##NEED COMMENT

    #drive forward a litttle bit # 
    robot.straight(35)  #12-6-21 -kahk

    #drive back a tiny bit 
    #robot.straight(-70) #12-5-21 -lmh
    robot.straight(-100)  #12-6-21 -kahk

    #turn toward door
    #robot.turn(140) #12-5-21 -lmh
    #robot.turn(190)  #12-6-21 -kahk ipk 220 190
    robot.turn(90) ## NEED COMMENT

    #drive toward door
    robot.straight(250)

    #turn back toward door #12-6-21 -kahk
    robot.turn(-40)  

    #drive toward door
    robot.straight(70)

    #deliver package
    packagedispenser()

    #drive back a tiny bit
    robot.straight(-70)

def new_run():
    '''
    This is the new run for state by ipk that goes to the eastern side of the board and does missions
    '''
    #position the attachment arm
    am.run_time(speed=-400,time=800)
    
    #go to line
    robot.straight(170)

    #follow line
    follow_line2(distance=730, speed = 120, right_or_left_sensor = "right", side_of_line = "left", Kp = 0.6, Ki = 0.0008, Kd = 2.0)

    #lower arm
    am.run_time(speed=400,time=600)

    #knock over bridge
    robot.straight(80)

    #position the attachment arm
    am.run_time(speed=-400,time=600)

    #drive ahead
    robot.straight(270)

    #lower arm
    am.run_time(speed=400,time=600)

    #backup into bridge
    robot.straight(-130)

    #a little turn
    robot.turn(5)

    #position the attachment arm
    am.run_time(speed=-400,time=800)

    #follow line to hellacopter
    follow_line2(distance=800, speed = 120, right_or_left_sensor = "right", side_of_line = "left", Kp = 0.8, Ki = 0.0008, Kd = 2.0)

    #backup a little
    robot.straight(-100)

    #turn and catch line
    robot.turn(85)
    robot.straight(60)
    ev3.speaker.beep(200)  # DEBUG BEEP 1

    #follow line to rr bridge
    follow_line2(distance=350, speed = 80, right_or_left_sensor = "left", side_of_line = "right", Kp = 1.0, Ki = 0.0008, Kd = 2.0)

    #lower arm to rr bridge
    am.run_time(speed=-400,time=1100)

    #raise arm
    am.run_time(speed=400,time=1100)

    #backup to catch train
    robot.straight(-200)    

    #lower arm
    am.run_time(speed=-400,time=800)

    #pull train
    follow_line2(distance=220, speed = 80, right_or_left_sensor = "left", side_of_line = "right", Kp = .8, Ki = 0.0008, Kd = 2.0)

    #raise arm
    am.run_time(speed=400,time=800)

    #backup to catch train
    robot.straight(-220)

    #lower arm
    am.run_time(speed=-400,time=800)

    #pull train
    follow_line2(distance=250, speed = 80, right_or_left_sensor = "left", side_of_line = "right", Kp = .8, Ki = 0.0008, Kd = 2.0)

def blade():
    
    robot.drive(speed = 500, turn_rate = 70)
    wait(1000)
    robot.stop()
    ev3.speaker.beep(800)  
    robot.drive(speed = 500, turn_rate = 10)
    wait(1500)
    robot.drive(speed = -500, turn_rate = 0)
    wait(3000)
    robot.stop()

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
            followline2( 1300, speed = 120, right_or_left_sensor = "left", side_of_line = "left", Kp = 1.0, Ki = 0.0008, Kd =.001)
        elif run_number == 1:
            watch_sensors()

        elif run_number == 2:
            right_motor_run()

        elif run_number == 3:
            watch_sensors()

                    

        # Move on to next run screen
        if run_number < last_run_number: 
            run_number = run_number + 1
        else:
            run_number = 0  
