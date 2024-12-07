# Elly, Abby hi
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
    td.set_speed_percentage(50)
    td.curve(100, 45)
    td.straight_drive(350) #adjust length to get past banana boat
    td.curve(100, 45)
    td.straight_drive(180)  # collect seaweed
    run_task(ta.move_D_angle(150))
    td.set_speed_percentage(50)
    td.curve(-230, 80) #adjust radius to go around banana boat
    td.curve(540, -53) #adjust radium to get closer or further from angular fish)
    td.straight_drive(630)  # drive past angler fish
    run_task(ta.move_D_angle(-150))
    td.straight_drive(50)
    td.curve(400, -45)
    td.turn(-45)
    td.straight_drive(200)
    td.curve(500, 50)


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Krillies(td, ta)
