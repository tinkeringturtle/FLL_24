from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from TurtleDrive import *
from TurtleAttachement import *


def run_Elly(td, ta):

    print("start run")
    run_task(ta.move_D_angle(325.5))  # spins Angler Artifact)


# MAIN FUNCTION
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Elly(td, ta)
