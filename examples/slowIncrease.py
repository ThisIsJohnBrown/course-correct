
from __future__ import division
import time
import Adafruit_PCA9685
import sys

pwm = Adafruit_PCA9685.PCA9685(0x40)

servo_min = 150  # Min pulse length out of 4096
servo_max = 650  # Max pulse length out of 4096

print {"asdf": "fff"}

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

servo_diff = servo_max - servo_min
speed = 2
offset = 2
last = time.time()



n = int(sys.argv[1])
t = 0

while True:
    t = t + 1
    pulse = servo_min + t * 10
    pwm.set_pwm(n, 0, pulse)
    print raw_input(pulse)
