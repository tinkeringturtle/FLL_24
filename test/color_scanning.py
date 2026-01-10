from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize
hub = PrimeHub()
sensor = ColorSensor(Port.F)

# Visual confirmation the program is active
hub.light.animate([Color.RED, Color.GREEN, Color.BLUE], interval=200)

print("--- STARTING SENSOR READ ---")

# Loop forever
while True:
    # 1. Read the color data
    data = sensor.hsv()

    # 2. Print it to the "Output" terminal at the bottom
    # We use a f-string for clear formatting
    print("H: {} | S: {} | V: {}".format(data.h, data.s, data.v))

    # 3. Wait 500ms (half a second) so it's readable
    wait(500)
