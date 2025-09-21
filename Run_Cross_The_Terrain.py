from TurtleDrive import *
from TurtleAttachement import *
async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)
#11th line from right
# line nine
def run_Anshi(td, ta):
    print("start run")
    td.straight_drive(-100)
    td.curve(-155, 110 )
    td.straight_drive(-220)
    td.turn(50)
    td.straight_drive(60)
    td.turn(20)
    td.straight_drive(15)
    #td.straight_drive(-70)
    


if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Anshi(td, ta)
#run_task(ta.move_C_angle(200))