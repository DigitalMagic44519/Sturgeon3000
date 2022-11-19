def wait_for_button(ev3):
    """
    This function shows a picture of the buttons on the EV3 screen.

    Then it waits until you press a button.

    It returns which button was pressed.
    """

    # Show a picture of the buttons on the screen.
    # ev3.screen.load_image('zbuttons.png')

    # Tip: add text or icons to the image to help you
    # remember what each button will do in your program.

    # Wait for a single button to be pressed and save the result.
    pressed = []
    while len(pressed) != 1:
        pressed = ev3.buttons.pressed()
    button = pressed[0]

    # Print which button was pressed
    # ev3.screen.draw_text(2, 100, button)

    # Now wait for the button to be released.
    while any(ev3.buttons.pressed()):
        pass

    # Return which button was pressed.
    return button
    
def make_screen(ev3, run_name, page, check1, check2, check3, check4):
    ev3.screen.clear()
    ev3.screen.draw_text(1, 1, run_name)
    ev3.screen.draw_text(1, 20, page)
    ev3.screen.draw_text(1, 40, "> " + check1)
    ev3.screen.draw_text(1, 60, "> " + check2)
    ev3.screen.draw_text(1, 80, "> " + check3)
    ev3.screen.draw_text(1, 100, "> " + check4)



    