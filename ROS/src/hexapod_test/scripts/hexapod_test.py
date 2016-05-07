#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import Int16

def set_hip(value):
    rospy.loginfo("Setting Hip Position value to {0:d}".format(value))
    hip_pub.publish(value)

def set_thigh(value):
    rospy.loginfo("Setting Thigh Position value to {0:d}".format(value))
    thigh_pub.publish(value)

def set_shin(value):
    rospy.loginfo("Setting Shin Position value to {0:d}".format(value))
    shin_pub.publish(value)

def init_rospy():
    global hip_pub
    global thigh_pub
    global shin_pub
    rospy.init_node('hexapod_test', anonymous=True)

    hip_pub = rospy.Publisher('/left/front/hip/command', Int16, queue_size=10)
    thigh_pub = rospy.Publisher('/left/front/thigh/command', Int16, queue_size=10)
    shin_pub = rospy.Publisher('/left/front/shin/command', Int16, queue_size=10)

def center_pos():
    set_hip(0)
    set_thigh(0)
    set_shin(0)

def basic_test():
    set_hip(-45)
    time.sleep(1)
    set_hip(45)
    time.sleep(1)
    set_hip(0)
    time.sleep(1)

    set_thigh(-45)
    time.sleep(1)
    set_thigh(45)
    time.sleep(1)
    set_thigh(0)
    time.sleep(1)

    set_shin(-45)
    time.sleep(1)
    set_shin(45)
    time.sleep(1)
    set_shin(0)
    time.sleep(1)

if __name__ == '__main__':
    init_rospy()
    center_pos()
    time.sleep(1)
    basic_test()

