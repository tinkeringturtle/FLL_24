# Elly, Abby

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait
from test_run import *

# Initialize the hub.
hub = PrimeHub()


def run_Krillies():
    td = TurtleDrive()
    ta = TurtleAttachment()
    td.straight_drive(230)
    td.turn(-40)
    td.straight_drive(180)
    td.turn(45)
    td.straight_drive(130)
    td.turn(-30)
    td.straight_drive(150)
    td.turn(75)
    td.set_speed_percentage(50)
    td.straight_drive(190)
    run_task(ta.move_D_angle(90))
    td.set_speed_percentage(25)
    td.curve(-200, 87)
    td.curve(500, -50)
    td.set_speed_percentage(50)
    td.straight_drive(400)
    #run_task(ta.move_D_angle(-85))
    #td.turn(-40)
    #td.straight_drive(170)
    #td.turn(-45)
    #td.straight_drive(100)
    #td.curve(600, 75)


if __name__ == "__main__":
    run_Krillies()
