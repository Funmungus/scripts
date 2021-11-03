#!/usr/bin/env python3

import time
import serial
import uinput

events = (
        uinput.REL_X,
        uinput.REL_Y,
        uinput.REL_WHEEL,
        # uinput.REL_HWHEEL,
        uinput.BTN_LEFT,
        uinput.BTN_RIGHT,
        )

with uinput.Device(events) as device:
    ser = serial.Serial(
            port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
    )
    # device.emit(uinput.REL_X, x, syn=False)
    # device.emit(uinput.REL_Y, y, syn=False)
    # device.emit(uinput.WHEEL, wheel)

    counter=0
