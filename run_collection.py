# Elly, Abby

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.tools import wait
from test_run import *

# Initialize the hub.
hub = PrimeHub()


def run_Krillies():
    td = TurtleDrive()
    td.straight_drive(230)
    td.turn(-40)
    td.straight_drive(180)
    td.turn(45)
    td.straight_drive(130)
    td.turn(-40)
    td.straight_drive(150)
    td.turn(90)
    td.set_speed_percentage(50)
    td.straight_drive(150)


if __name__ == "__main__":
    run_Krillies()
