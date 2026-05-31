from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line nine
def Run_silo(td, ta):

    td.straight_drive(170)
    td.turn(90)
    td.straight_drive(1225)
    td.turn(35)
    td.straight_drive(620)
    td.turn(-105)
    td.straight_drive(330)
    td.turn(-98)
    td.turn(8)
    # gussing things after this
    td.straight_drive(85)


#   ta.move_D_time(speed_percentage=-100, time_millisec=500)

# ta.move_C_time(speed_percentage=100, time_millisec=500)


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_silo(td, ta)
