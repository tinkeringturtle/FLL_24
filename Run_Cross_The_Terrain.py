from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=95)


# from the left 12th line


def run_Anshi(td, ta):
    print("start run")
    td.straight_drive(-150)
    td.turn(-90)
    td.straight_drive(-715)
    td.turn(95)
    td.straight_drive(200)
    run_task(ta.move_D_angle(-900))
    td.turn(-5)
    td.straight_drive(-230)
    run_task(ta.move_C_angle(300))
    run_task(ta.move_C_angle(-300))
    td.straight_drive(15)
    td.turn(90)
    td.straight_drive(1000)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
# run_task(ta.move_C_angle(200))
