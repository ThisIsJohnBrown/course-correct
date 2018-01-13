from __future__ import division
import time
import math
import random
import sys
import select

import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685(0x40)

servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
# pwm2.set_pwm_freq(60)
tick = 0
servo_diff = servo_max - servo_min
speed = 2
offset = 2
last = time.time()


for number in range(0, 16):
    perc = 1
    # perc = random.random()
    # pwm = Adafruit_PCA9685.PCA9685(0x40)
    # pwm2 = Adafruit_PCA9685.PCA9685(0x41)
    pwm.set_pwm(number, 0, int(perc * servo_diff + servo_min))
    # pwm.set_pwm(number + 8, 0, int(perc * servo_diff + servo_min))
    # pwm2.set_pwm(number, 0, int(perc * servo_diff + servo_min))
    # pwm2.set_pwm(number + 8, 0, int(perc * servo_diff + servo_min))
    time.sleep(.3)

# pwm = Adafruit_PCA9685.PCA9685(0x40)
# pwm2 = Adafruit_PCA9685.PCA9685(0x41)

raw_input("Begin calibration")

for number in range(0, 16):
    print "Calibrating tee # %d" % number
    t = 0
    input = 0
    pwm.set_pwm(number, 0, servo_max)
    while input != "s":
        t = t + 1
        pulse = servo_max - t * 10
        pwm.set_pwm(number, 0, pulse)
        print "Setting tee at %d" % pulse
        input = raw_input()

raw_input("End calibration")

# for number in range(12,16):
#     perc = 0
#     # perc = random.random()
#     # pwm = Adafruit_PCA9685.PCA9685(0x40)
#     # pwm2 = Adafruit_PCA9685.PCA9685(0x41)
#     pwm.set_pwm(number, 0, int(perc * servo_diff + servo_min))
#     # pwm2.set_pwm(number, 0, int(perc * servo_diff + servo_min))
#     time.sleep(.8)


time.sleep(1)