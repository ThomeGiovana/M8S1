import machine
import time

led = machine.Pin(18, machine.Pin.OUT)

while True:
    led.value(True)
    time.sleep(1)
    led.value(False)
    time.sleep(1)