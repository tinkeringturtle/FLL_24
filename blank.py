from TurtleDrive import *
from TurtleAttachement import *


# from pybricks.tools import wait, multitask, run_task
async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


# line nine
def Run_blank(td, ta):
    print("start run")
    td.straight_drive(150)
    td.curve(530, -50)
    run_task(ta.move_D_angle(-125))  # lower arm down
    wait(1000)
    td.straight_drive(380)
    td.turn(20)
    run_task(ta.move_D_angle(125))  # pick up Iana
    td.straight_drive(60)  # turn to get flag in
    td.straight_drive(-160)  # back up form Iana
    td.turn(-70)
    return
    td.turn(-90)
    td.straight_drive(445)
    td.turn(-35)
    td.straight_drive(100)
    run_task(ta.move_D_angle(-250))
    return
    td.straight_drive(200)
    td.curve(530, -70)
    td.straight_drive(260)
    td.turn(60)
    run_task(ta.move_D_angle(-130))
    td.straight_drive(30)
    run_task(ta.move_D_angle(130))


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_blank(td, ta)
