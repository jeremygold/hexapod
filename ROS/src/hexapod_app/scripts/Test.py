#!/usr/bin/env python

import rospy
from time import sleep
from Joint import Joint

delay = 0.3

def test_joint(joint):
    joint.set_joint_angle(20)
    sleep(delay)
    joint.set_joint_angle(0)
    sleep(delay)

if __name__ == '__main__':
    rospy.init_node('hexapod_app_test', anonymous=True)
    left_front_hip = Joint("/left/front/hip")
    left_mid_hip = Joint("/left/mid/hip")
    left_back_hip = Joint("/left/back/hip")

    left_front_thigh = Joint("/left/front/thigh")
    left_mid_thigh = Joint("/left/mid/thigh")
    left_back_thigh = Joint("/left/back/thigh")

    left_front_shin = Joint("/left/front/shin")
    left_mid_shin = Joint("/left/mid/shin")
    left_back_shin = Joint("/left/back/shin")

    right_front_hip = Joint("/right/front/hip")
    right_mid_hip = Joint("/right/mid/hip")
    right_back_hip = Joint("/right/back/hip")

    right_front_thigh = Joint("/right/front/thigh")
    right_mid_thigh = Joint("/right/mid/thigh")
    right_back_thigh = Joint("/right/back/thigh")

    right_front_shin = Joint("/right/front/shin")
    right_mid_shin = Joint("/right/mid/shin")
    right_back_shin = Joint("/right/back/shin")

    sleep(1)

    test_joint(left_front_hip)
    test_joint(left_mid_hip)
    test_joint(left_back_hip)

    test_joint(left_front_thigh)
    test_joint(left_mid_thigh)
    test_joint(left_back_thigh)

    test_joint(left_front_shin)
    test_joint(left_mid_shin)
    test_joint(left_back_shin)

    test_joint(right_front_hip)
    test_joint(right_mid_hip)
    test_joint(right_back_hip)

    test_joint(right_front_thigh)
    test_joint(right_mid_thigh)
    test_joint(right_back_thigh)

    test_joint(right_front_shin)
    test_joint(right_mid_shin)
    test_joint(right_back_shin)
