# Anshi, Alice

# Anshi, Alice

from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_C_angle(angle=angle, speed_percentage=30)


# line nine
def run_whale(td, ta):
    td.set_speed_percentage(85, 80)
    td.turn(-10)
    td.straight_drive(395)
    td.turn(45)
    td.straight_drive(150)  # Aproaches boat
    td.set_speed_percentage(80, 75)
    td.turn(45)
    td.turn(-65)  # flip yellow boat
    td.set_speed_percentage(65, 60)
    td.straight_drive(170)
    td.set_speed_percentage(30, 25)
    td.turn(15)
    td.straight_drive(160)  # open whale mouth
    run_task(runAttachemnt(ta, -50))  # drop krill in whale mouth
    td.stop()
    td.set_speed_percentage(65, 60)
    td.straight_drive(-250)
    td.set_speed_percentage(15, 10)
    td.turn(140)
    td.set_speed_percentage(44, 39)
    td.straight_drive(-355)
    td.set_speed_percentage(10, 5)
    td.turn(35)  # go behind the sonar
    td.turn(-30)
    td.set_speed_percentage(100, 95)
    td.straight_drive(540)  # Flip the first sonar
    td.curve(450, -45)  # come home


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_whale(td, ta)
