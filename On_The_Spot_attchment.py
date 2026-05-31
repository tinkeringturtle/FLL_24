from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line nine
def Run_silo(td, ta):

    ta.move_D_time(speed_percentage=-100, time_millisec=400)

    ta.move_C_time(speed_percentage=100, time_millisec=490)


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_silo(td, ta)
