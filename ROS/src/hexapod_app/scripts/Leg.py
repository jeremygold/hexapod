import rospy
from Joint import Joint
from math import *

THIGH_LENGTH = 80 # mm
SHIN_LENGTH = 101.35 # mm
MAX_ANGLE = 0
MAX_HIP_ANGLE = 0

class Leg:
    def __init__(self, side, pos):
        self.side = side
        self.pos = pos

        topic_base = "/" + side + "/" + pos + "/"

        self.hip = Joint(topic_base + "hip")
        self.thigh = Joint(topic_base + "thigh")
        self.shin = Joint(topic_base + "shin")

    def set_hip_angle(self, angle):
        self.hip.set_joint_angle(angle)

    def set_thigh_angle(self, angle):
        self.thigh.set_joint_angle(angle)

    def set_shin_angle(self, angle):
        self.shin.set_joint_angle(angle)

    def calc_shin_angle(self):
        result = self.thigh.get_joint_angle_rads()
        alpha = acos((THIGH_LENGTH * (cos(-self.thigh.get_joint_angle_rads()) - cos(MAX_ANGLE))) / SHIN_LENGTH)
        omega = acos((THIGH_LENGTH * (cos(self.hip.get_joint_angle_rads()) - cos(MAX_HIP_ANGLE))) / SHIN_LENGTH)

        result -= alpha
        result -= omega
        result += pi

        self.set_shin_angle(int(result * 180 / pi))

    def set_leg_pos(self, hip_angle, thigh_angle, shin_angle):
        self.hip.set_joint_angle(hip_angle)
        self.thigh.set_joint_angle(thigh_angle)
        self.shin.set_joint_angle(shin_angle)

    def set_leg_pos(self, hip_angle, thigh_angle):
        self.hip.set_joint_angle(hip_angle)
        self.thigh.set_joint_angle(thigh_angle)
        self.calc_shin_angle()

    def set_hip_only(self, hip_angle):
        self.set_hip_angle(hip_angle)
        self.calc_shin_angle()

    def set_thigh_only(self, thigh_angle):
        self.set_thigh_angle(thigh_angle)
        self.calc_shin_angle()

