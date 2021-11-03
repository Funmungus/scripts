#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

shutdownCounter = 0

def ShutdownConfirmed():
    print("Shutdown confirmed")
    # ensure clean exit
    os.system("sudo shutdown -h now")
    exit()

def Shutdown(channel):
    global shutdownCounter
    # pull-up logic, normally high, button goes low
    if GPIO.input(channel) == GPIO.LOW:
        if shutdownCounter == 0:
            shutdownCounter = 1
    else:
        shutdownCounter = 0

GPIO.add_event_detect(3, GPIO.BOTH, callback=Shutdown, bouncetime=10)

try:
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
    GPIO.cleanup()
