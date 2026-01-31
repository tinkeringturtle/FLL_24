from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line up on line nine
def run_2nd_Flag(td, ta):
    print("start run")
    td.set_speed_percentage
    td.straight_drive(4000)
    td.straight_drive(-5700)


# MAIN FUNCTION
if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_2nd_Flag(td, ta)
