#!/usr/bin/env python

from Leg import *
from math import *
import time

limit = 2.5 * pi / 8

front_right = Leg(6, 7, 8, Side.right)

# front_right.set_hip_angle(pi/4)
# time.sleep(1)
# front_right.set_hip_angle(-pi/4)
# time.sleep(1)
# 
# front_right.set_thigh_angle(pi/4)
# time.sleep(1)
# front_right.set_thigh_angle(-pi/4)
# time.sleep(1)
# 
# front_right.set_shin_angle(pi/4)
# time.sleep(1)
# front_right.set_shin_angle(-pi/4)
# time.sleep(1)

front_right.set_leg_pos(0, limit)
time.sleep(1)
front_right.set_leg_pos(0, -limit)
time.sleep(1)
# 
# for i in range(0, 5):
    # front_right.set_leg_pos(pi / 4, 0)
    # time.sleep(1)
    # front_right.set_leg_pos(-pi / 4, 0)
    # time.sleep(1)

front_right.set_leg_pos(0, 0)
