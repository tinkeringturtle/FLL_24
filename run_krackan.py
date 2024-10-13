# Author: Meghana, Emma (awesome Team)
#
from TurtleDrive import *
from TurtleAttachement import *

async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=10)

def run_kracken():
    td = TurtleDrive()
    ta = TurtleAttachment()
    # to drive stright do - td.drive(x mm)
    # td.straight_drive(200)
    td.set_speed_percentage(speed_percentage=40)
    td.straight_drive(220)
    td.curve(300, 90)
    td.set_speed_percentage(speed_percentage=50)
    td.straight_drive(20)
    td.set_speed_percentage(speed_percentage=1, acceleration_percentage=1)
    td.straight_drive(55)
    # getting qrill
    run_task(runAttachemnt(ta, 118))
    # returning back
    td.straight_drive(-90)
    td.set_speed_percentage(speed_percentage=30)
    td.curve(-300, 90)
    td.set_speed_percentage(speed_percentage=70)
    td.straight_drive(-220)
    run_task(runAttachemnt(ta, -118))
    td.stop()



if __name__ == "__main__":
    run_kracken()
    ta = TurtleAttachment()
    
    