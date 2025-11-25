from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from TurtleDrive import *
from TurtleAttachement import *
import Run_Cross_The_Terrain, Run_artifact, Run_Bolders
import Run_Map_Reveal, Run_Market, Run_Seal_Deliver, Run_Shipreck
import Run_silo

# Initialize the sensor.
bottom_sensor = ColorSensor(Port.E)  # this is bottom sesor
front_sensor = ColorSensor(Port.F)  # this is front sensor

MY_GREEN = Color(h=155, s=72, v=48)
MY_MAGENTA = Color(h=339, s=88, v=70)
MY_RED = Color(h=353, s=88, v=80)
MY_ORANGE = Color(h=5, s=84, v=43)
MY_BLUE = Color(h=216, s=86, v=32)
MY_BLACK = Color(h=0, s=0, v=0)
MY_YELLOW = Color(h=51, s=72, v=100)
MY_WHITE = Color(h=0, s=0, v=100)
MY_NONE = Color(h=0, s=0, v=0)
# Initialize the hub.
hub = PrimeHub()


def scan_colors(sensor):
    # Repeat forever.
    while True:
        hdv = sensor.hsv(surface=True)

        color = sensor.color()

        ambient = sensor.ambient()

    # print(""HSV:" , hsv, "| Color:, color,"|Ambient:", ambient"")


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    #  scan_colors(front_sensor)

    # set the color as we tested
    # set_colors(front_sensor)
    first_run = False
    # Main loop
    while True:
        color = front_sensor.color()
        pressed = hub.buttons.pressed()

        # run the attachment code is button is pressed
        if Button.RIGHT in pressed and color == Color.BLUE:
            print("Run Cross the Terrain")
            Run_Cross_The_Terrain.run_Anshi(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)

        wait(50)

        if Button.RIGHT in pressed and color == Color.BLACK:
            print("Run Cross the Terrain")
            Run_artifact.Run_Alice(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)
        if Button.RIGHT in pressed and color == Color.Light_Green :
            print("Run Cross the Terrain")
            Run_Shipreck.run_Shipreck(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)

     if Button.RIGHT in pressed and color == Color.Dark_Green :
            print("Run Cross the Terrain")
            Run_Map_Reveal.run_Map_Reveal(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)

    if Button.RIGHT in pressed and color == Color.WHITE :
            print("Run Cross the Terrain")
            Run_Bolders.run_bolders(td, ta) for right 
            Run_Market.run_market(td, ta) for left
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)

        wait(50)

    if Button.RIGHT in pressed and color == Color.ORANGE:
            print("Run Seal Deliver")
            Run_Seal_Deliver.Run_Seal_Deliver(td, ta)
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)