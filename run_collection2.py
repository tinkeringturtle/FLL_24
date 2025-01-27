# Elly, Abby
# line up right side of robot 2 lines from middle black line

# from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait
from test_run import *

# Initialize the hub.
# hub = PrimeHub()
# pybricksdev run ble --name Chaos Master_Program.py


def run_Krillies(td, ta):
    # run_task(ta.move_C_angle(140))
    #  ta.move_C_angle_sync(140)HEAD
    td.set_speed_percentage(80, 75)
    td.straight_drive(25)
    td.curve(210, -45)
    td.set_speed_percentage(80, 75)
    td.straight_drive(410)  # collect octopus
    td.set_speed_percentage(80, 75)
    td.straight_drive(-340)
    td.set_speed_percentage(55, 50)
    td.curve(110, 45)
    td.straight_drive(320)  # adjust length to get past banana boat
    td.curve(120, 50)
    td.straight_drive(125)  # collect seaweed
    # run_task(ta.move_C_angle(-140))
    ta.move_C_angle_sync(-150)
    td.set_speed_percentage(55, 50)
    td.curve(-230, 81)  # adjust radius to go around banana boat
    td.set_speed_percentage(100, 95)
    td.straight_drive(-500)


def run_anglerfish(td, ta):
    td.set_speed_percentage(80, 75)
    td.straight_drive(280)
    td.turn(-90)
    td.straight_drive(475)
    td.turn(52)
    td.straight_drive(700)
    td.turn(-68)
    td.set_speed_percentage(55, 50)
    run_task(ta.move_C_angle(150))
    td.straight_drive(465)
    td.turn(-40)
    td.straight_drive(50)
    td.turn(-17)
    td.set_speed_percentage(100, 95)
    td.straight_drive(700)
    # td.turn(20)
    # td.straight_drive(350)
    # td.curve(300, 40)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()

    run_Krillies(td, ta)
    run_anglerfish(td, ta)
