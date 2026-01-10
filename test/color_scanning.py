from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialize
hub = PrimeHub()
sensor = ColorSensor(Port.F)

# Visual confirmation
hub.light.on(Color.WHITE)

print("--- STARTING YELLOW DETECTION ---")
while True:
    # 1. Read the color data
    data = sensor.hsv()

    # 2. Extract values for easier reading
    h, s, v = data.h, data.s, data.v

    # 3. Check for Yellow thresholds
    # Hue: 40-70 is yellow | Saturation: > 50 (not gray) | Value: > 50 (not black)
    if 40 <= h <= 70 and s > 50 and v > 50:
        print("YELLOW! (H:{} S:{} V:{})".format(h, s, v))
        hub.light.on(Color.YELLOW)
    else:
        print("H: {} | S: {} | V: {}".format(h, s, v))
        hub.light.off()
