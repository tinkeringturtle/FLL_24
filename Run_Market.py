from TurtleDrive import *
from TurtleAttachement import *
from pybricks.tools import wait, multitask, run_task

# from pybricks.tools import wait, multitask, run_task


# line up left side second dark line from left
def run_market(td, ta):
    td.straight_drive(305)
    run_task(ta.move_D_angle(-320))


# run_task(ta.move_C_angle(-200))

# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_market(td, ta)
