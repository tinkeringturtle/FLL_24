from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


# line nine
def run_Map_Reveal(td, ta):
    print("start run")
    td.set_speed_percentage(85)
    td.straight_drive(705)  # Go to get brush
    td.straight_drive(-200)
    run_task(ta.move_C_angle(50))
    td.straight_drive(85)
    run_task(ta.move_C_angle(-55))
    run_task(ta.move_C_angle(100))  # should have brush
    wait(1.5)
    td.set_speed_percentage(50)
    td.turn(35)
    td.straight_drive(175)
    td.turn(-80)  # about to go into 3 thing
    td.straight_drive(253)
    td.straight_drive(-45)
    td.set_speed_percentage(100)
    run_task(ta.move_D_angle(-150))
    td.set_speed_percentage(100)
    td.straight_drive(-150)
    td.curve(-100, -60)
    td.set_speed_percentage(100)
    td.straight_drive(-700)


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Map_Reveal(td, ta)
