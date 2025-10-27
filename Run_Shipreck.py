from TurtleDrive import *
from TurtleAttachement import *


# line nine
def run_Shipreck(td, ta):
    print("start run")
    td.set_speed_percentage(100)
    run_task(ta.move_D_angle(100))
    td.straight_drive(540)
    run_task(ta.move_D_angle(-105))
    td.straight_drive(-40)
    run_task(ta.move_D_angle(300))
    td.straight_drive(-100)
    td.turn(-15.25)
    td.straight_drive(175)
    td.turn(20)
    td.set_speed_percentage(100)
    td.straight_drive(420)
    td.turn(-8)
    td.straight_drive(-600)



if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Shipreck(td, ta)
