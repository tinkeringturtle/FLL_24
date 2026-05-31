from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line nine
def Run_silo(td, ta):

    td.straight_drive(170)
    td.turn(90)  # turn towards the field
    td.straight_drive(1250)  # drive out of field towards boulder
    # ta.move_D_time(speed_percentage=100, time_millisec=435)

    # ta.move_C_time(speed_percentage=-100, time_millisec=435)
    td.set_speed_percentage(40)
    td.straight_drive(230)  # drive into the structure with guides
    ta.move_D_time(speed_percentage=-125, time_millisec=400)  # motor for lever

    ta.move_C_time(speed_percentage=125, time_millisec=490)  # motor for lever
    td.straight_drive(15)  # push out boulder
    td.set_speed_percentage(80)
    td.straight_drive(-700)  # going home
    td.turn(30)  # turn
    td.straight_drive(-1200)  # ALL THE WAY HOME.


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_silo(td, ta)
