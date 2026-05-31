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
    td.straight_drive(365)
    td.turn(-94)
    """"""
    # ta.move_D_time(speed_percentage=100, time_millisec=100)

    # ta.move_C_time(speed_percentage=-100, time_millisec=100)
    """"""

    td.straight_drive(130)
    wait(5000)
    td.straight_drive(-200)
    td.straight_drive(35)
    # guessing from here
    td.turn(80)
    td.straight_drive(200)
    td.turn(-20)  # out of home after this
    td.straight_drive(300)  # exiting home
    td.turn(27)  # manuever around chicken
    td.straight_drive(200)
    td.turn(10)  # manouver around blue block
    td.straight_drive(
        400
    )  # new home (with boulder and need to get sand and new attachmetn. )

    # ta.move_D_time(speed_percentage=-100, time_millisec=500)

    # ta.move_C_time(speed_percentage=100, time_millisec=500)


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_silo(td, ta)
