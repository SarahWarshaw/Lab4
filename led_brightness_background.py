#!/usr/bin/python3

import RPi.GPIO as gpio
import time
import json

while True:
  with open('led_brightness_multiple.txt','r') as f:
    data = json.load(f)

  dutyCycle = float(data['slider'])
  ledPin = int(data['LED'])

  gpio.setmode(gpio.BCM)
  gpio.setup(ledPin, gpio.OUT)
  pwm = gpio.PWM(ledPin, 100) # PWM object on our pin at 100 Hz
  pwm.start(0)


  pwm.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)
