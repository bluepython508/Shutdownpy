import gpiozero as IO
from signal import pause
from subprocess import call
import syslog
import time
shutdown = IO.Button(21, pull_up=False)
indicator = IO.PWMLED(17)
def call_shutdown():
        indicator.blink(on_time=1, off_time=1, n=10, background=False)
        syslog.syslog("GPIO Interupt Detected. Shutting Down...")
        call("sudo shutdown -h now", shell=True)
shutdown.when_pressed = call_shutdown
indicator.blink(on_time=1, off_time=1, fade_in_time= 0.9, fade_out_time=0.9, n=None, background=False)
pause()
