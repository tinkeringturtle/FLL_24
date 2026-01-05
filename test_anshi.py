from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Assuming these files and functions exist in your project
from TurtleDrive import *
from TurtleAttachement import *

td = TurtleDrive()
ta = TurtleAttachment()
# from the left 11th line
# hi


print("start run")
td.set_speed_percentage(60)
td.straight_drive(-167)
td.set_speed_percentage(75)
td.turn(-90)
td.straight_drive(-715)
td.set_speed_percentage(50)
td.turn(95)
td.straight_drive(245)
run_task(ta.move_D_angle(-650))  # spins Angler Artifact

td.turn(-9)


td.straight_drive(-181)
td.turn(2)  # grabs seabead sample
td.set_speed_percentage(90)
td.straight_drive(125)  # exits seabead area
td.turn(-55)
run_task(ta.move_C_angle(-505, speed_percentage=90))  # arm goes down
td.set_speed_percentage(70)
td.turn(11)
td.straight_drive(-190)  # appraoches seal
td.turn(5)
td.set_speed_percentage(80)
td.straight_drive(-50)
td.turn(-4)
# run_task(ta.move_C_angle(150, speed_percentage=50))  # arm goes up; seal goes up
run_task(ta.move_C_angle(150, speed_percentage=35))  # arm goes up; seal goes up
td.straight_drive(150)
td.turn(-50)
td.straight_drive(-400)  # heads toward anshi area
td.turn(-15)
td.straight_drive(-400)
