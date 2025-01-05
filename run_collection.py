# Elly, Abby hi
# line up right side of robot 2 lines from middle black line

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait
from test_run import *

# Initialize the hub.
hub = PrimeHub()
# pybricksdev run ble --name Chaos Master_Program.py


def run_Krillies(td, ta):

    run_task(ta.move_C_angle(140))
    td.set_speed_percentage(100)
    td.curve(200, -45)
    td.set_speed_percentage(50)
    td.set_speed_percentage(60)
    td.straight_drive(410)  # collect octopus
    td.straight_drive(-340)
    td.set_speed_percentage(50)
    td.curve(110, 45)
    td.straight_drive(330)  # adjust length to get past banana boat
    td.curve(120, 50)
    td.straight_drive(120)  # collect seaweed
    run_task(ta.move_C_angle(-140))
    td.set_speed_percentage(50)
    td.curve(-230, 81)  # adjust radius to go around banana boat
    run_task(ta.move_D_angle(250))
    td.curve(470, -57)  # adjust radium to get closer or further from angular fish)
    run_task(ta.move_D_angle(-250))
    td.straight_drive(470)  # drive past angler fish and sample adjust for reach
    run_task(ta.move_D_angle(720))  # send rack out to collect seabed
    td.set_speed_percentage(50, 50)
    run_task(ta.move_C_angle(140))
    td.straight_drive(185)
    run_task(ta.move_D_angle(-700))
    td.turn(-15)
    td.straight_drive(280)  # getting krill and other sample number 3
    td.turn(-40)
    td.straight_drive(50)
    run_task(ta.move_C_angle(-140))
    wait(500)
    run_task(ta.move_C_angle(140))
    td.turn(-50)
    td.set_speed_percentage(100)
    td.straight_drive(100)
    td.turn(40)
    td.set_speed_percentage(1000)
    td.straight_drive(450)

    # td.straight_drive(100)

    # td.straight_drive(60)
    # put a left turn here later if wanted
    # td.straight_drive(135)
    # td.turn(35)
    # td.set_speed_percentage(100)
    # td.straight_drive(600)

    """
    td.straight_drive(100)
    td.curve(320, -755)
    td.turn(-55)
    td.straight_drive(200)
    td.curve(470, 50)
    td.straight_drive(620)
    run_task(ta.move_D_angle(-150))
    td.straight_drive(10)
    """


# td.curve(400, -45)
# td.turn(-45)
# td.straight_drive(200)
# td.curve(500, 50)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()

    run_Krillies(td, ta)
