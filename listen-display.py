#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
import time

display = '/sys/class/backlight/fb_ili9341/bl_power'

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    time.sleep(1)
    GPIO.wait_for_edge(27, GPIO.FALLING)

    check = subprocess.Popen(['cat', display], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_value = check.communicate()[0]

    c_off = 'echo "1" > '+ display
    c_on = 'echo "0" > '+ display


    if (stdout_value == "0\n"):
        subprocess.Popen(['/bin/sh', '-c',c_off], stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
       subprocess.Popen(['/bin/sh', '-c',c_on], stdin=subprocess.PIPE, stderr=subprocess.PIPE)
