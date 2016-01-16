from math import *
import os

class Servo:
    def __init__(self, number):
        self.number = number
        self.angle = 0
        
    def set_desired_angle(self, angle):
        self.angle = angle
        self.write_value_to_hardware()

    def get_desired_angle(self):
        return self.angle

    def write_value_to_hardware(self):
        # Compensate for 1000 - 2000us representing +/- 90 degrees, and ServoBlaster is in units of 10us
        angle_deg = degrees(self.angle)
        pwmDelay = 150 + ((angle_deg) * 50 / 90)
        print "servo[" + str(self.number) + "][" + str(angle_deg) + "=" + str(pwmDelay*10) + "us]"
        cmd = "echo " + str(self.number) + "=" + str(pwmDelay) + " > /dev/servoblaster"
        os.system(cmd)
        # print "Sending command: " + cmd

