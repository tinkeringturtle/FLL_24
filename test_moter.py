from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line up on line 2 form the right
def run_Anshi(td, ta):

    run_task(ta.move_D_angle(-525, speed_percentage=90))  # arm goes down


# MAIN FUNCTION
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
