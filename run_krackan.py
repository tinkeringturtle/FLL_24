# Author: Meghana, Emma
from TurtleDrive import *
from TurtleAttachement import *

def run_kracken():
    td = TurtleDrive()
    ta = TurtleAttachment()
    # to drive stright do - td.drive(x mm)
    #td.straight_drive(200)
    td.set_speed_percentage(speed_percentage=40)
    td.straight_drive(220)
    td.curve(300,90)
    td.set_speed_percentage(speed_percentage=5)
    td.straight_drive(65)

if __name__ == "__main__":
    run_kracken()
