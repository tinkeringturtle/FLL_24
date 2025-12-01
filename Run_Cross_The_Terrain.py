from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=95)


# from the left 12th line


def run_Anshi(td, ta):
    print("start run")
    td.straight_drive(-163)
    td.turn(-90)
    td.straight_drive(-720)
    td.turn(95)
    td.straight_drive(224)
    run_task(ta.move_D_angle(-900))
    td.straight_drive(-226)
    run_task(ta.move_C_angle(330))
    run_task(ta.move_C_angle(-330))
    td.straight_drive(15)
    td.turn(89)
    td.straight_drive(420)
    td.turn(-40)
    td.straight_drive(615)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
# run_task(ta.move_C_angle(200))
