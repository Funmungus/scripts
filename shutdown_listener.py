#!/usr/bin/env python3

import pigpio
import atexit
import time
import os

gpio = 3
pi = pigpio.pi()
if not pi.connected:
    sys.exit(1)
    

def cleanup():
    global pi
    if pi:
        pi.stop()
        pi = None

atexit.register(cleanup)


# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
pi.set_mode(gpio, pigpio.INPUT)
pi.set_pull_up_down(gpio, pigpio.PUD_UP)

shutdownCounter = 0

def ShutdownConfirmed():
    print("Shutdown confirmed")
    # ensure clean exit
    os.system("sudo shutdown -h now")
    exit()

def Shutdown(gpioIn, level, tick):
    global shutdownCounter
    if gpioIn != gpio:
        exit(1)
    # pull-up logic, normally high, button goes low
    if level == 1:
        shutdownCounter = 0
    else:
        if shutdownCounter == 0:
            shutdownCounter = 1

#pi.set_noise_filter(gpio, 1000, 5000)
callback=pi.callback(gpio, pigpio.EITHER_EDGE, Shutdown)

try:
    print("Begin shutdown listener")
    while 1:
        time.sleep(3)
        # shutdown has begun
        if shutdownCounter > 0:
            if shutdownCounter == 1:
                # 1 sleep iteration has passed
                shutdownCounter += 1
            else:
                # 6 seconds have passed
                ShutdownConfirmed()

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
