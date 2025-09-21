from TurtleDrive import *
from TurtleAttachement import *


# line nine
def Run_silo(td, ta):
    print("start run")
    td.straight_drive(400)
    run_task(ta.move_D_angle(-300))
    run_task(ta.move_D_angle(300))
    run_task(ta.move_D_angle(-300))
    run_task(ta.move_D_angle(-300))
    run_task(ta.move_D_angle(-300))


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_silo(td, ta)
