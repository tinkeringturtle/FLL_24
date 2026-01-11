from TurtleDrive import *
from TurtleAttachement import *

# from pybricks.tools import wait, multitask, run_task


# line nine
def Run_silo(td, ta):
    print("start run")
    td.straight_drive(700)
    td.turn(-90)
    td.straight_drive(35)
    td.straight_drive(-60)
    td.set_speed_percentage(20)
    td.straight_drive(-65)
    run_task(ta.move_D_angle(-300))
    run_task(ta.move_D_angle(300))
    run_task(ta.move_D_angle(-300))
    run_task(ta.move_D_angle(-300))
    run_task(ta.move_D_angle(-300))


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_silo(td, ta)
