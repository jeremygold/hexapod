from math import *
from Servo import *

THIGH_LENGTH = 80 # mm
SHIN_LENGTH = 101.35 # mm
MAX_ANGLE = 0
MAX_HIP_ANGLE = 0
    
class Side:
    left = 1
    right = 2

class Leg:

    def __init__(self, hip_servo_number, thigh_servo_number, shin_servo_number, side):
        self.hip_servo = Servo(hip_servo_number)
        self.thigh_servo = Servo(thigh_servo_number)
        self.shin_servo = Servo(shin_servo_number)
        self.side = side

    def set_hip_angle(self, angle):
        self.hip_angle = angle
        if(self.side == Side.right):
            self.hip_servo.set_servo_angle(-angle)
        else:
            self.hip_servo.set_servo_angle(angle)

    def set_thigh_angle(self, angle):
        self.thigh_angle = angle
        if(self.side == Side.right):
            self.thigh_servo.set_servo_angle(-angle)
        else:
            self.thigh_servo.set_servo_angle(angle)

    def set_shin_angle(self, angle):
        self.shin_angle = angle
        if(self.side == Side.right):
            self.shin_servo.set_servo_angle(angle)
        else:
            self.shin_servo.set_servo_angle(-angle)
	
    def calc_shin_angle(self):
        result = -self.thigh_angle
        alpha = acos((THIGH_LENGTH * (cos(self.thigh_angle) - cos(MAX_ANGLE))) / SHIN_LENGTH)
        omega = acos((THIGH_LENGTH * (cos(self.hip_angle) - cos(MAX_HIP_ANGLE))) / SHIN_LENGTH)

        result += alpha
        result += omega
        result -= pi

        self.set_shin_angle(result)

    def set_leg_pos(self, hip_angle, thigh_angle):
        self.set_hip_angle(hip_angle)
        self.set_thigh_angle(thigh_angle)
        self.calc_shin_angle()

    def set_hip_only(self, hip_angle):
        self.set_hip_angle(hip_angle)
        self.calc_shin_angle()

    def set_thigh_only(self, thigh_angle):
        self.set_thigh_angle(thigh_angle)
        self.calc_shin_angle()
