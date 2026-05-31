from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line nine
def Run_going(td, ta):
    ta.move_D_time(speed_percentage=-1000, time_millisec=1000)

    ta.move_C_time(speed_percentage=1000, time_millisec=1000)
    # run begins here

    # Main Function
    if __name__ == "__main__":
        print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_going(td, ta)
