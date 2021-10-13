#!/usr/bin/python3

import RPi.GPIO as gpio
import time
import json

with open('led_brightness_multiple.txt','r') as f:
  data = json.load(f)

dutyCycle = float(data['slider'])

if ('1' in data['menu_choice']):
  ledPin = 12
elif ('2' in data['menu_choice']): 
  ledPin = 13
else:
  ledPin = 14

gpio.setmode(gpio.BCM)
gpio.setup(ledPin, gpio.OUT)
pwm = gpio.PWM(ledPin, 100) # PWM object on our pin at 100 Hz
pwm.start(0)

while True:
  pwm.ChangeDutyCycle(dutyCycle)
  time.sleep(0.1)
