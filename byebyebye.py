from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
sensor = ColorSensor(Port.F)

while True:
    hsv = sensor.hsv()
    print("H:", hsv.h, "S:", hsv.s, "V:", hsv.v)
    wait(200)
