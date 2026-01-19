from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from TurtleDrive import *
from TurtleAttachement import *
from test_bottom_color import detect_bottom_color


def detect_bottom_color(td):
    td.turn_drive(200, 0, 0)

    while True:
        # Read the current color
        detected_color = sensor.color()

        if detected_color == Color.WHITE:
            print("White detected")
        elif detected_color == Color.BLACK or detected_color == Color.NONE:
            # Pybricks often reports very dark surfaces as Color.NONE
            print("Black detected")
            td.stop()
            break
    wait(10)


td = TurtleDrive()
detect_bottom_color(td)


sensor = ColorSensor(Port.E)


def run_Elly(td, ta):

    print("start run")
    td.straight_drive(40)
    td.turn(-90)
    detect_bottom_color(td)


# MAIN FUNCTION
if __name__ == "__main__":
    print("Hello")
    td = TurtleDrive()
    ta = TurtleAttachment()
    run_Elly(td, ta)
