from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait
from test_run import *

# Initialize the hub.
hub = PrimeHub()


while True:
    pressed = []
    while not any(pressed):
        # check for the button press
        pressed = hub.buttons.pressed()

    print(pressed)

    # Display an arrow to indicate which button was pressed.
    if Button.LEFT in pressed:
        hub.display.icon(Icon.HAPPY)
        # if col == Color.SENSOR_RED:
        run2()
        # elif
    elif Button.RIGHT in pressed:
        hub.display.icon(Icon.ARROW_RIGHT_DOWN)
    elif Button.BLUETOOTH in pressed:
        hub.display.icon(Icon.ARROW_RIGHT_UP)
