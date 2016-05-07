#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import Int16

delay = 0.3

publishers = dict({})

def set_position(joint_name, position):
    # rospy.loginfo("Setting {0:s} Position to {1:d}".format(joint_name, position))
    publishers[joint_name].publish(position)

def init_rospy():
    rospy.init_node('hexapod_test', anonymous=True)

    for side in ["left", "right"]:
        for pos in ["front", "mid", "back"]:
            for joint in ["hip", "thigh", "shin"]:
                joint = "/" + side + "/" + pos + "/" + joint
                publishers[joint] = rospy.Publisher(joint + '/command', Int16, queue_size=10)

def center_pos():
    for joint in publishers:
        set_position(joint, 0)

def basic_test(joint_name):
    rospy.loginfo("Basic test: {:s}".format(joint_name))
    set_position(joint_name, 20)
    time.sleep(delay)
    set_position(joint_name, 0)
    time.sleep(delay)

if __name__ == '__main__':
    init_rospy()
    center_pos()
    time.sleep(delay)

    for side in ["left", "right"]:
        for pos in ["front", "mid", "back"]:
            for joint in ["hip", "thigh", "shin"]:
                joint = "/" + side + "/" + pos + "/" + joint
                basic_test(joint)

