from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize the sensor.
bottom_sensor = ColorSensor(Port.E)
front_sensor = ColorSensor(Port.F)


def scan_colors(sensor):
    # Repeat forever.
    while True:

        # Get the ambient color values. Instead of scanning the color of a surface,
        # this lets you scan the color of light sources like lamps or screens.
        hsv = sensor.hsv(surface=True)
        color = sensor.color(surface=True)

        # Get the ambient light intensity.
        ambient = sensor.ambient()

        # Print the measurements.
        print(str(hsv), str(color), ambient)

        # Point the sensor at a computer screen or colored light. Watch the color.
        # Also, cover the sensor with your hands and watch the ambient value.

        # Wait so we can read the printed line
        wait(500)


def set_colors(sensor):
    # First, decide which objects you want to detect, and measure their HSV values.
    # You can do that with the hsv() method as shown in the previous example.
    #
    # Use your measurements to override the default colors, or add new colors:
    Color.GREEN = Color(h=132, s=94, v=26)
    Color.MAGENTA = Color(h=348, s=96, v=40)
    Color.BROWN = Color(h=17, s=78, v=15)
    Color.RED = Color(h=359, s=97, v=39)

    # Put your colors in a list or tuple.
    my_colors = (Color.GREEN, Color.MAGENTA, Color.BROWN, Color.RED, Color.NONE)

    # Save your colors.
    sensor.detectable_colors(my_colors)

    # color() works as usual, but now it returns one of your specified colors.
    while True:
        color = sensor.color()

        # Print the color.
        print(color)

        # Check which one it is.
        if color == Color.MAGENTA:
            print("It works!")

        # Wait so


scan_colors(front_sensor)
