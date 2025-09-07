from TurtleDrive import *
from TurtleAttachement import *


# line nine
def run_Map_Reveal(td, ta):
    print("start run")
    td.set_speed_percentage(75)
    td.straight_drive(720)
    td.turn(-60)
    td.set_speed_percentage(35)
    td.straight_drive(200)
    td.curve(-180, -75)
    td.set_speed_percentage(50)
    td.straight_drive(-100)
    td.straight_drive(230)
    td.curve(50, -60)
    td.straight_drive(20)
    ta.run_task(runAttachement(ta, 50))
    td.curve(-50, 60)
    td.set_speed_percentage(100)
    td.straight_drive(320)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Map_Reveal(td, ta)
