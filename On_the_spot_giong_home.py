from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line nine
def Run_going(td, ta):
    """
    td.straight_drive(795)
    td.turn(90)
    td.straight_drive(430)
    td.turn(93)
    """
    td.straight_drive(300)


# run begins here


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_going(td, ta)
