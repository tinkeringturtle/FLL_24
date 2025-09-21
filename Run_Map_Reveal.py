from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


# line nine
def run_Map_Reveal(td, ta):
    print("start run")
    td.set_speed_percentage(100)
    td.straight_drive(690)
    td.straight_drive(-175)
    td.turn(20)
    td.straight_drive(200)
    td.turn(-70)
    td.turn(15)
    td.straight_drive(250)
    td.straight_drive(-40)
    td.set_speed_percentage(50)
    run_task(ta.move_D_angle(-80))
    td.set_speed_percentage(100)
    td.straight_drive(-85)
    


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Map_Reveal(td, ta)
