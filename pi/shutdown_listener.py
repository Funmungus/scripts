#!/usr/bin/env python3

import pigpio
import atexit
import time
import os
import sys

gpio = 3
pi = pigpio.pi()
if not pi.connected:
    print("Error: pigpio is not connected.  Likely pigpiod is not running.")
    sys.exit(1)

def cleanup():
    global pi
    if pi:
        pi.stop()
        pi = None

atexit.register(cleanup)

pi.set_mode(gpio, pigpio.INPUT)
pi.set_pull_up_down(gpio, pigpio.PUD_UP)

shutdown_counter = 0

def shutdown_confirmed():
    print("Shutdown confirmed")
    # ensure clean exit
    os.system("sudo shutdown -h now")
    exit()

def shutdown(gpioIn, level, tick):
    global shutdown_counter
    if gpioIn != gpio:
        exit(1)
    # pull-up logic, normally high, button goes low
    if level == 1:
        shutdown_counter = 0
    else:
        if shutdown_counter == 0:
            shutdown_counter = 1

#pi.set_noise_filter(gpio, 1000, 5000)
callback=pi.callback(gpio, pigpio.EITHER_EDGE, shutdown)

try:
    print("Begin shutdown listener")
    while 1:
        time.sleep(3)
        # shutdown has begun
        if shutdown_counter > 0:
            if shutdown_counter == 1:
                # 1 sleep iteration has passed
                shutdown_counter += 1
            else:
                # 6 seconds have passed
                shutdown_confirmed()

except KeyboardInterrupt:
    print("\nExiting shutdown button listener.")
    exit()

except:
    print("An unknown error has occured.")

finally:
    print("End program safe cleanup.")
    if pi:
        pi.stop()
        pi = None
