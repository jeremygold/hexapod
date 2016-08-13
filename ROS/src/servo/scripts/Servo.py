from math import *
import os

class Servo:
    def __init__(self, number):
        self.number = number
        self.angle = 0
        
    def set_servo_angle(self, angle):
        self.angle = angle
        self.write_value_to_hardware()

    def get_servo_angle(self):
        return self.angle

    def write_value_to_hardware(self):
        # Compensate for 500us - 2500us representing +/- 90 degrees, and ServoBlaster is in units of 10us
        pwm_delay = 150 + (self.angle * 100 / 90)

        if os.path.exists("/dev/servoblaster"):
            # Send to PWM output
            servo_command = "%u=%u\n" % (self.number, pwm_delay)
            with open("/dev/servoblaster", "wb") as servo_device:
                servo_device.write(servo_command)

