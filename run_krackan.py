# Author: Meghana, Emma (awesome Team)
#
from TurtleDrive import *
from TurtleAttachement import *


def run_kracken():
    def runCrab():
    td = TurtleDrive()
    # to drive stright do - td.drive(x mm)
    # td.straight_drive(200)
    td.set_speed_percentage(speed_percentage=40)
    td.straight_drive(220)
    td.curve(300, 90)
    td.set_speed_percentage(speed_percentage=50)
    td.straight_drive(20)
    td.set_speed_percentage(speed_percentage=1, acceleration_percentage=1)
    td.straight_drive(55)
    ta.move_D_time(speed_percentage=10, time_millisec=80)
    # returning back
    td.straight_drive(-90)
    td.set_speed_percentage(speed_percentage=20)
    td.turn(-70)
    td.set_speed_percentage(speed_percentage=70)
    td.straight_drive(-400)
    td.stop()

def turn():
    td = TurtleDrive()
    td.drive(325)
    print(td.get_speed)
    td.set_speed(turn_rate=125, turn_acceleration=75)
    td.turn(90)



if __name__ == "__main__":
    run_kracken()
