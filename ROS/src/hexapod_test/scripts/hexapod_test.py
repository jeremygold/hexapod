#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import Int16

def setHip(value):
    rospy.loginfo("Setting Hip Position value to {0:d}".format(value))
    hip_pub.publish(value)

def setThigh(value):
    rospy.loginfo("Setting Thigh Position value to {0:d}".format(value))
    thigh_pub.publish(value)

def setShin(value):
    rospy.loginfo("Setting Shin Position value to {0:d}".format(value))
    shin_pub.publish(value)

def initRospy():
    global hip_pub
    global thigh_pub
    global shin_pub
    rospy.init_node('hexapod_test', anonymous=True)
    hip_pub = rospy.Publisher('hip', Int16, queue_size=10)
    thigh_pub = rospy.Publisher('thigh', Int16, queue_size=10)
    shin_pub = rospy.Publisher('shin', Int16, queue_size=10)

def centerPos():
    setHip(0)
    setThigh(0)
    setShin(0)

def basicTest():
    setHip(-45)
    time.sleep(1)
    setHip(45)
    time.sleep(1)
    setHip(0)
    time.sleep(1)

    setThigh(-45)
    time.sleep(1)
    setThigh(45)
    time.sleep(1)
    setThigh(0)
    time.sleep(1)

    setShin(-45)
    time.sleep(1)
    setShin(45)
    time.sleep(1)
    setShin(0)
    time.sleep(1)

if __name__ == '__main__':
    initRospy()
    centerPos()
    time.sleep(1)
    basicTest()

