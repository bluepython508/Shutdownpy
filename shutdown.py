import gpiozero as IO
from signal import pause
from subprocess import call
import time
import threading
shutdown = IO.Button(21, pull_up=False)
indicator = IO.PWMLED(17)
def call_shutdown():
        for x in range(10):
                indicator.value(1.0)
                time.sleep(1)
                indicator.value(0.0)
                time.sleep(1)
        call("sudo shutdown -h now", shell=True)
def frange(start, stop, step):
        i = start
        if (start < stop):
                while i <= stop:
                        yield i
                        i += step
# For some reason, += doesn't always add an exact decimal, so we have to round the value
                        i = round(i, 1)
        else:
                while i >= stop:
                        yield i
                        i += step
# For some reason, += doesn't always add an exact decimal, so we have to round the value
                        i = round(i, 1)
shutdown.when_pressed = call_shutdown
class RandomLEDs(threading.Thread):
        def __init__(self, threadID, name):
                threading.Thread.__init__(self)
                self.threadID = threadID
                self.name = name

        def run(self):
                while True:
                        the_led = indicator
                        self.fade_in_led(the_led, 0.03)
                        time.sleep(0.3)
                        self.fade_out_led(the_led, 0.02)
                        time.sleep(0.3)

# PWM the LED value from 0 to 1 (or from 1 to 0) with a 0.1 step
        def fade_in_led(self, led, speed):
                for i in frange(0.0, 1.0, 0.1):
                        led.value = i
                        time.sleep(speed)

        def fade_out_led(self, led, speed):
                for i in frange(1.0, 0.0, -0.1):
                        led.value = i
                        time.sleep(speed)
pause()
