from TurtleDrive import *
from TurtleAttachement import *


# line nine
def run_Shipreck(td, ta):
    print("start run")
    td.set_speed_percentage(75)
    td.straight_drive(700)
    td.set_speed_percentage(10)
    run_task(ta.move_C_angle(20))
    td.set_speed_percentage(100)
    td.straight_drive(-120)
    td.straight_drive(-525)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Shipreck(td, ta)
