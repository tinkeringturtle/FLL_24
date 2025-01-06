# Elly, Abby hi
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
  #  ta.move_C_angle_sync(140)
    td.set_speed_percentage(100,90)
    td.curve(200, -45)
    td.set_speed_percentage(50,45)
    td.straight_drive(410)  # collect octopus
    td.straight_drive(-340)
    td.set_speed_percentage(50,45)
    td.curve(110, 45)
    td.straight_drive(330)  # adjust length to get past banana boat
    td.curve(120, 50)
    td.straight_drive(150)  # collect seaweed
    # run_task(ta.move_C_angle(-140))
    ta.move_C_angle_sync(-140)
    td.set_speed_percentage(50,45)
    td.curve(-230, 81)  # adjust radius to go around banana boat
    td.set_speed_percentage(100,90)
    td.straight_drive(-500)


def run_anglerfish(td, ta):
    td.straight_drive(280)
    td.turn(-90)
    td.straight_drive(475)
    td.turn(52)
    td.straight_drive(700)
    td.turn(-70)
    run_task(ta.move_C_angle(150))
    td.straight_drive(450)
    td.turn(-20)
    td.straight_drive(50)
   


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()

    run_Krillies(td, ta)
    run_anglerfish(td, ta)
