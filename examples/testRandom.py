# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import math
import random
import sys
import select

print random.random()

# Import the PCA9685 module.
import Adafruit_PCA9685



# class keyevent(PyKeyboardEvent):
#     def __init__(self):
#         super(keyevent, self).__init__()

#     def tap(self, keycode, character, press):
#         print 'event: tab, keycode: {}, character: {}'.format(keycode, character)

# if __name__ == "__main__":
#     k = keyevent()
#     m = mouseevent()
#     m.run()
#     print "Capturing mouse"
#     k.run()
#     print "Capturing keyboard"

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685(0x40)
# pwm2 = Adafruit_PCA9685.PCA9685(0x41)

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)




# Collect events until released


# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 650  # Max pulse length out of 4096

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

# l = True
# while l == True:
#     for number in range(0,8):
#         perc = 1
#         # perc = random.random()
#         pwm.set_pwm(number, 0, servo_max - tick)
#     put = raw_input("Moved to " + str(servo_max - tick) + "Press Enter to continue...")
#     if put == "s":
#         tick = tick + 10
#     if put == "w":
#         tick = tick - 10
#     if put == "t":
#         l = False



print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    tick += 1
    if time.time() - last > .1:
        last = time.time()
        num = int(random.random() * 7)
        print "a"
        perc = (1 + math.sin((time.time() + offset * num) * speed)) / 2 / 2
        print perc
        pwm.set_pwm(num, 0, int(perc * servo_diff + servo_min))
        
        # num = int(random.random() * 16)
        # perc = (1 + math.sin((time.time() + offset * num) * speed)) / 2 / 2
        # pwm2.set_pwm(num, 0, int(perc * servo_diff + servo_min))
        # for number in range(0,16):
        #     perc = (1 + math.sin((time.time() + offset * number) * speed)) / 2 / 2
        #     # perc = random.random()
        #     pwm.set_pwm(number, 0, int(perc * servo_diff + servo_min))
        # for number in range(0,16):
        #     perc = (1 + math.sin((time.time() + offset * number) * speed)) / 2
        #     # perc = random.random()
        #     pwm2.set_pwm(number, 0, int(perc * servo_diff + servo_min))
    
    # pwm2.set_pwm(0, 0, servo_max)
    # time.sleep(1/24)
