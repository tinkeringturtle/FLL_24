from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from TurtleDrive import *
from TurtleAttachement import *
from test_bottom_color import detect_bottom_color


# from pybricks.tools import wait, multitask, run_task


td = TurtleDrive()
detect_bottom_color(td)


sensor = ColorSensor(Port.E)


def run_Anshi(td, ta):

    print("start run")

    td.straight_drive(150)
    td.turn(-90)
    detect_bottom_color(td)
    # td.straight_drive(150)


# MAIN FUNCTION
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
