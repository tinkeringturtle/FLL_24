# Author: Meghana, Emma (awesome Team )
#
from TurtleDrive import *
from TurtleAttachement import *


async def runAttachemnt(ta, angle):
    await ta.move_D_angle(angle=angle, speed_percentage=20)


def run_boat_shark2(td, ta):
    # boat/shark woohooo
    td.turn(-15)
    td.set_speed_percentage(90, 85)
    td.straight_drive(790)  # shark is being delivered
    td.straight_drive(-250)  # backing up
    td.turn(55)
    td.straight_drive(230)  # chhange distance depending on whether its going in or not
    td.turn(-35)
    td.straight_drive(300)  # going into crabpot
    run_task(runAttachemnt(ta, 80))
    td.set_speed_percentage(35, 30)
    td.straight_drive(-185)  # lifting crabs up
    wait(250)
    td.straight_drive(20)  # use this if the arm is knocking off the crabbies.
    run_task(runAttachemnt(ta, -80))  # raising arm
    td.set_speed_percentage(65, 60)
    td.straight_drive(-100)
    td.turn(-20)  # change turn to make sre it doenst hit crabs or shark.
    td.set_speed_percentage(105, 100)
    td.straight_drive(450)
    td.turn(45)
    td.straight_drive(730)  # going home
    # WHERE RUN ENDS
    """
    td.set_speed_percentage(50, 45)
    td.curve(1090, -40)
    td.straight_drive(-150)
    td.turn(46)
    # crab
    td.straight_drive(420)
    run_task(runAttachemnt(ta, 110))
    td.straight_drive(-210)
    run_task(runAttachemnt(ta, -1))
    td.straight_drive(-50)
    run_task(runAttachemnt(ta, -110))
    # boat
    td.turn(-55)
    td.straight_drive(-175)
    # going to other side
    td.straight_drive(130)
    td.set_speed_percentage(15, 10)
    td.turn(17)
    td.set_speed_percentage(25, 10)
    td.straight_drive(60)
    td.set_speed_percentage(50, 50)
    td.straight_drive(100)
    td.turn(25)
    td.set_speed_percentage(70, 70)
    td.straight_drive(485)
    td.turn(45)
    td.straight_drive(1200)
    # td.set_speed_percentage(30, 30)
    td.straight_drive(100)
    td.set_speed_percentage(15, 10)
    td.curve(10, 90)
    # td.set_speed_percentage(, 40)
    td.straight_drive(860)
    td.turn(22)
    td.set_speed_percentage(75, 75)
    td.straight_drive(555)
    """


# run has ended


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_boat_shark2(td, ta)
