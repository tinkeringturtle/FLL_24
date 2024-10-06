# Author:  Abby, Elly

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from TurtleDrive import *


def runBannana_Boat():
    td = TurtleDrive()
    # to drive stright do - td.drive(x mm)

    td.curve(200, -45)
    td.set_speed_percentage(speed_percentage=40)
    td.straight_drive(390)
    td.straight_drive(-250)
    td.turn(90)
    td.straight_drive(345)
    td.turn(20)
    td.turn(-90)
    td.set_speed_percentage(speed_percentage=100)
    td.straight_drive(-350)


def main():
    # Initialize the hub.
    hub = PrimeHub()

    while True:
        pressed = []
        while not any(pressed):
            # check for the button press
            pressed = hub.buttons.pressed()


        # Display an arrow to indicate which button was pressed.
        if Button.LEFT in pressed:
            hub.display.icon(Icon.HAPPY)
        

        elif Button.RIGHT in pressed:
            hub.display.icon(Icon.ARROW_RIGHT_DOWN)
            runBannana_Boat()


if __name__ == "__main__":
    main()
