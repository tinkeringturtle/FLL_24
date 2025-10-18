from TurtleDrive import *
from TurtleAttachement import *


# line nine
def run_Shipreck(td, ta):
    print("start run")
    td.set_speed_percentage(100)
    run_task(ta.move_D_angle(100))
    td.straight_drive(535)
    run_task(ta.move_D_angle(-105))
    td.straight_drive(-25)
    run_task(ta.move_D_angle(125))
    td.drive_straight(350)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Shipreck(td, ta)
