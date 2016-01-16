#!/usr/bin/env python

from Leg import *
from math import *
import time
from numpy import arange

HIP_MIN = -pi / 6
HIP_MAX = pi / 6
HIP_STEP = pi / 16
THIGH_MIN = -pi / 4
THIGH_MAX = pi / 4
THIGH_STEP = pi / 16

limit = 2.5 * pi / 8
front_right = Leg(6, 7, 8, Side.right)
front_left = Leg(5, 4, 3, Side.left)
mid_right = Leg(9, 10, 11, Side.right)
mid_left = Leg(2, 1, 0, Side.left)

def individual_tests_right():
    front_right.set_hip_angle(pi/4)
    time.sleep(1)
    front_right.set_hip_angle(-pi/4)
    time.sleep(1)

    front_right.set_thigh_angle(pi/4)
    time.sleep(1)
    front_right.set_thigh_angle(-pi/4)
    time.sleep(1)

    front_right.set_shin_angle(pi/4)
    time.sleep(1)
    front_right.set_shin_angle(-pi/4)
    time.sleep(1)

def individual_tests_left():
    front_left.set_hip_angle(pi/4)
    time.sleep(1)
    front_left.set_hip_angle(-pi/4)
    time.sleep(1)

    front_left.set_thigh_angle(pi/4)
    time.sleep(1)
    front_left.set_thigh_angle(-pi/4)
    time.sleep(1)

    front_left.set_shin_angle(pi/4)
    time.sleep(1)
    front_left.set_shin_angle(-pi/4)
    time.sleep(1)

def individual_tests_mid():
    mid_left.set_hip_angle(pi/4)
    mid_right.set_hip_angle(pi/4)
    time.sleep(1)
    mid_left.set_hip_angle(-pi/4)
    mid_right.set_hip_angle(-pi/4)
    time.sleep(1)

    mid_left.set_thigh_angle(pi/4)
    mid_right.set_thigh_angle(pi/4)
    time.sleep(1)
    mid_left.set_thigh_angle(-pi/4)
    mid_right.set_thigh_angle(-pi/4)
    time.sleep(1)

    mid_left.set_shin_angle(pi/4)
    mid_right.set_shin_angle(pi/4)
    time.sleep(1)
    mid_left.set_shin_angle(-pi/4)
    mid_right.set_shin_angle(-pi/4)
    time.sleep(1)

def set_thighs(angle):
    front_right.set_thigh_only(angle)
    mid_left.set_thigh_only(angle)

    mid_right.set_thigh_only(-angle)
    front_left.set_thigh_only(-angle)

def set_hips(angle):
    front_right.set_hip_only(angle)
    mid_left.set_hip_only(angle)

    front_left.set_hip_only(-angle)
    mid_right.set_hip_only(-angle)

def right_up():
    for angle in arange(THIGH_MIN, THIGH_MAX, THIGH_STEP):
        set_thighs(angle)

def left_up():
    for angle in arange(THIGH_MAX, THIGH_MIN, -THIGH_STEP):
        set_thighs(angle)

def right_forward():
    for angle in arange(HIP_MIN, HIP_MAX, HIP_STEP):
        set_hips(angle)

def left_forward():
    for angle in arange(HIP_MAX, HIP_MIN, -HIP_STEP):
        set_hips(angle)

def left_init():
    set_thighs(THIGH_MIN)

    for angle in arange(0, HIP_MIN, -HIP_STEP):
        set_hips(angle)

def right_reset():
    for angle in arange(HIP_MIN, 0, HIP_STEP):
        set_hips(angle)

    time.sleep(0.5)
    set_thighs(0)

def walk_on_spot_tests():
    for i in range(0,2):
        right_up()
        left_up()

def walk_forward():
    right_up()
    right_forward()
    left_up()
    left_forward()

def walk_back():
    right_forward()
    right_up()
    left_forward()
    left_up()

def walk_test():
    left_init()
    for i in range(0, 1):
        walk_forward()

    for i in range(0, 1):
        walk_back()
    right_reset()

def hip_ik_tests():
    for angle in arange(-pi / 4, pi / 4, pi / 64):
        front_right.set_leg_pos(angle, -pi / 4)
        front_left.set_leg_pos(angle, -pi / 4)
        mid_right.set_leg_pos(angle, -pi / 4)
        mid_left.set_leg_pos(angle, -pi / 4)
        time.sleep(0.05)

def reset_all():
    front_right.set_leg_pos(0, 0)
    front_left.set_leg_pos(0, 0)
    mid_left.set_leg_pos(0, 0)
    mid_right.set_leg_pos(0, 0)

reset_all()
# individual_tests_right()
# individual_tests_left()
# individual_tests_mid()
# hip_ik_tests()
# walk_on_spot_tests()

walk_test()

reset_all()
