# Elly, Abby
# line up right side of robot 2 lines from middle black line

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait
from test_run import *

# Initialize the hub.
hub = PrimeHub()


def run_Krillies(td, ta):
    run_task(ta.move_D_angle(-150))
    td.set_speed_percentage(50)
    td.curve(200, -45)
    td.set_speed_percentage(60)
    td.straight_drive(410)  # collect octopus
    td.straight_drive(-340)

    """
    td.turn(30)
    td.straight_drive(175)
    td.turn(40)
    td.straight_drive(125)
    td.turn(-45)
    td.straight_drive(130)
    td.turn(12)
    td.turn(60)
    td.straight_drive(250)
    """

    td.set_speed_percentage(50)
    td.curve(100, 45)
    td.straight_drive(320)
    td.curve(100, 45)
    td.straight_drive(160)  # collect seaweed
    run_task(ta.move_D_angle(150))
    td.set_speed_percentage(50)
    td.curve(-200, 80)
    td.curve(470, -53)
    td.straight_drive(630)  # drive past angler fish
    run_task(ta.move_D_angle(-150))
    td.straight_drive(50)

    """

    td.set_speed_percentage(75)
    td.straight_drive(250)
    td.turn(-20)
    td.straight_drive(95)
    td.turn(10)
    td.straight_drive(60)
    td.turn(15)
    td.straight_drive(300)
    run_task(ta.move_D_angle(-90))
    td.set_speed_percentage(50)
    """
    td.curve(400, -45)
    td.turn(-45)
    td.straight_drive(200)
    td.curve(500, 50)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Krillies(td, ta)
