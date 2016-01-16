#!/usr/bin/env python

from Leg import *
from math import *
import time
from numpy import arange

limit = 2.5 * pi / 8
front_right = Leg(6, 7, 8, Side.right)

def individual_tests():
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

def thigh_ik_tests():
    front_right.set_leg_pos(0, limit)
    time.sleep(1)
    front_right.set_leg_pos(0, -limit)
    time.sleep(1)

def hip_ik_tests():
    for angle in arange(-pi / 4, pi / 4, pi / 64):
        front_right.set_leg_pos(angle, -pi / 4)
        time.sleep(0.05)

individual_tests()
thigh_ik_tests()
hip_ik_tests()

front_right.set_leg_pos(0, 0)
