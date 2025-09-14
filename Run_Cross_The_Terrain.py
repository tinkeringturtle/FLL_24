from TurtleDrive import *
from TurtleAttachement import *
async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)
#11th line from right
# line nine
def run_Anshi(td, ta):
    print("start run")
    td.straight_drive(-100)
    td.curve(-175, 115, wait=True)
    td.straight_drive(-475)
    td.turn(120)
    td.straight_drive(-70)
    


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
#run_task(ta.move_C_angle(200))