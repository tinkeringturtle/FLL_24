from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

hub = PrimeHub()

for i in range(5):
    hub.light.on(Color.RED)
    wait(1000)
    hub.light.off()
    wait(500)