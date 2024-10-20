# Author: Meghana, Emma (awesome Team)
#
from TurtleDrive import *
from TurtleAttachement import *

async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=10)

def run_boat_shark():
    td = TurtleDrive()
    ta = TurtleAttachment()
    #run starts from here
    td.straight_drive(700)
    td.turn(-50)
    td.straight_drive(-145)
    #run has ended
if __name__ == "__main__":
    run_boat_shark()
   
    
    