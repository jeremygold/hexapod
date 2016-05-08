# Joint.py - Encapsulates a specific joint that can command the corresponding topic to move to the requested location

import rospy
from std_msgs.msg import Int16
from math import pi

class Joint:
    def __init__(self, joint_name):
        rospy.loginfo("Initializing new Joint: {0:s}".format(joint_name))
        self.joint_name = joint_name

        if joint_name.startswith("/right"):
            self.sense = -1
        else:
            self.sense = 1

        self.publisher = rospy.Publisher(joint_name + "/command", Int16, queue_size = 10)

    def set_joint_angle(self, angle):
        # rospy.loginfo("Setting {0:s} to {1:d}".format(self.joint_name, angle))
        self.publisher.publish(self.sense * angle)
        self.joint_angle = angle

    def get_joint_angle(self):
        return self.joint_angle

    def get_joint_angle_rads(self):
        return self.joint_angle * pi / 180.0
