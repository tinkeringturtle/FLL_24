from TurtleDrive import *
from TurtleAttachement import *


# from pybricks.tools import wait, multitask, run_task
async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


# line nine
def Run_blank(td, ta):
    print("start run")
    td.straight_drive(200)
    td.curve(520, -70)
    td.straight_drive(280)
    td.turn(80)
    run_task(ta.move_D_angle(300))


# Main Function
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    Run_blank(td, ta)
