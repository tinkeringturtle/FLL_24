from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line nine
def Run_blank(td, ta):
    print("start run")
    td.straight_drive(200)
    td.curve(520, -70)
    td.straight_drive(260)
    td.turn(80)


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_blank(td, ta)
