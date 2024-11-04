from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Icon
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from TurtleDrive import *
from TurtleAttachement import *
import run_coral


# Initialize the sensor.
bottom_sensor = ColorSensor(Port.E)  # this is bottom sesor
front_sensor = ColorSensor(Port.F)  # this is front sensor

# Initialize the hub.
hub = PrimeHub()

Color.MY_GREEN = Color(h=155, s=72, v=48)
Color.MY_MAGENTA = Color(h=339, s=79, v=70)
Color.MY_RED = Color(h=352, s=88, v=80)
Color.MY_ORANGE = Color(h=9, s=84, v=99)
Color.MY_BLUE = Color(h=217, s=88, v=69)
Color.MY_BLACK = Color(h=240, s=5, v=24)
Color.MY_YELLOW = Color(h=52, s=71, v=100)
Color.MY_WHITE = Color(h=0, s=0, v=100)
Color.MY_NONE = Color(h=0, s=0, v=0)

colorToDefault = {
    Color.MY_GREEN: Color.GREEN,
    Color.MY_MAGENTA: Color.MAGENTA,
    Color.MY_RED: Color.RED,
    Color.MY_ORANGE: Color.ORANGE,
    Color.MY_BLUE: Color.BLUE,
    Color.MY_BLACK: Color.BLACK,
    Color.MY_WHITE: Color.WHITE,
    Color.MY_NONE: Color.NONE,
}


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

    # Put your colors in a list or tuple.
    my_colors = (
        Color.MY_GREEN,
        Color.MY_MAGENTA,
        Color.MY_RED,
        Color.MY_ORANGE,
        Color.MY_BLUE,
        Color.MY_BLACK,
        Color.MY_WHITE,
        Color.MY_NONE,
    )

    # Save your colors.
    sensor.detectable_colors(my_colors)

    # Wait so


def check_color(color):
    # Check which one it is.
    if color == Color.GREEN:
        print("GREEN")
        hub.light.on(Color.GREEN)
    if color == Color.MAGENTA:
        print("MAGENTA")
        hub.light.on(Color.MAGENTA)
    if color == Color.WHITE:
        print("WHITE")
        hub.light.on(Color.WHITE)
    if color == Color.RED:
        print("RED")
        hub.light.on(color.RED)
    if color == Color.YELLOW:
        print("YELLOW")
        hub.light.on(Color.YELLOW)
    if color == Color.BLACK:
        print("BLACK")
        hub.light.on(Color.BLACK)
    if color == Color.ORANGE:
        print("ORANGE")
        hub.light.on(Color.ORANGE)
    if color == Color.BLUE:
        print("BLUE")
        hub.light.on(Color.BLUE)


def check_button():
    pressed = []
    while not any(pressed):
        # check for the button press
        pressed = hub.buttons.pressed()

    # Display an arrow to indicate which button was pressed.
    if Button.LEFT in pressed:
        hub.display.icon(Icon.ARROW_LEFT)
    elif Button.RIGHT in pressed:
        hub.display.icon(Icon.ARROW_RIGHT)
    return pressed


if __name__ == "__main__":
    td = TurtleDrive()
    ta = TurtleAttachment()
    # scan_colors(front_sensor)
    set_colors(front_sensor)
    # color() works as usual, but now it returns one of your specified colors.
    while True:
        while True:
            color = front_sensor.color()

            if color == Color.MY_NONE:
                hub.display.icon(Icon.EYE_LEFT_BROW_UP)
                hub.light.off()
            else:
                hub.display.icon(Icon.HEART)
                hub.light.on(colorToDefault[color])

            wait(100)
            # check for the button press
            pressed = hub.buttons.pressed()
            print(pressed)

            # Display an arrow to indicate which button was pressed.
            if Button.LEFT in pressed:
                hub.display.icon(Icon.ARROW_LEFT)
            elif Button.RIGHT in pressed:
                hub.display.icon(Icon.ARROW_RIGHT)

            if color == Color.MY_MAGENTA():
                run_coral.runCoral()
