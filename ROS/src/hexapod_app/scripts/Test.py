#!/usr/bin/env python

import rospy
from time import sleep
from Joint import Joint
from Leg import Leg
from Robot import Robot
from numpy import arange
from PressupGait import PressupGait
import time

delay = 0.3

def test_joint(joint):
    joint.set_joint_angle(20)
    sleep(delay)
    joint.set_joint_angle(0)
    sleep(delay)

def init_joints():
    global left_front_hip
    global left_front_thigh
    global left_front_shin

    global left_mid_hip
    global left_mid_thigh
    global left_mid_shin

    global left_back_hip
    global left_back_thigh
    global left_back_shin

    global right_front_hip
    global right_front_thigh
    global right_front_shin

    global right_mid_hip
    global right_mid_thigh
    global right_mid_shin

    global right_back_hip
    global right_back_thigh
    global right_back_shin

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

def test_joints():
    init_joints()

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

def init_legs():
    global left_front 
    global left_mid 
    global left_back 
    global right_front 
    global right_mid 
    global right_back 

    left_front = Leg("left", "front")
    left_mid = Leg("left", "mid")
    left_back = Leg("left", "back")
    right_front = Leg("right", "front")
    right_mid = Leg("right", "mid")
    right_back = Leg("right", "back")

    sleep(1)

def test_legs():
    init_legs()
    for angle in arange(-45, 45, 3):
        left_front.set_leg_pos(angle, -20)
        left_mid.set_leg_pos(angle, -20)
        left_back.set_leg_pos(angle, -20)
        right_front.set_leg_pos(angle, -20)
        right_mid.set_leg_pos(angle, -20)
        right_back.set_leg_pos(angle, -20)

        time.sleep(0.05)

    left_front.set_leg_pos(0, 0)
    left_mid.set_leg_pos(0, 0)
    left_back.set_leg_pos(0, 0)

    right_front.set_leg_pos(0, 0)
    right_mid.set_leg_pos(0, 0)
    right_back.set_leg_pos(0, 0)

def test_robot_legs():
    robot = Robot()
    for angle in arange(-45, 45, 3):
        robot.left_front.set_leg_pos(angle, -20)
        robot.left_mid.set_leg_pos(angle, -20)
        robot.left_back.set_leg_pos(angle, -20)
        robot.right_front.set_leg_pos(angle, -20)
        robot.right_mid.set_leg_pos(angle, -20)
        robot.right_back.set_leg_pos(angle, -20)

        time.sleep(0.05)

    robot.left_front.set_leg_pos(0, 0)
    robot.left_mid.set_leg_pos(0, 0)
    robot.left_back.set_leg_pos(0, 0)

    robot.right_front.set_leg_pos(0, 0)
    robot.right_mid.set_leg_pos(0, 0)
    robot.right_back.set_leg_pos(0, 0)

def test_gait():
    robot = Robot()
    robot.gait = PressupGait()

    r = rospy.Rate(50)

    for i in range(200):
        robot.update()
        r.sleep()

    robot.center()


if __name__ == '__main__':
    rospy.init_node('hexapod_app_test', anonymous=True)

    # test_joints()
    # test_legs()
    # test_robot_legs()
    test_gait()



