import rospy
from Leg import Leg
from time import sleep
from IdleGait import IdleGait

class Robot:
    def __init__(self):
        self.left_front = Leg("left", "front")
        self.left_mid = Leg("left", "mid")
        self.left_back = Leg("left", "back")
        self.right_front = Leg("right", "front")
        self.right_mid = Leg("right", "mid")
        self.right_back = Leg("right", "back")

        self.gait = IdleGait()

        sleep(1)

    def update(self):
        self.gait.update(self)

    def center(self):
        self.left_front.set_leg_pos(0, 0, 0)
        self.left_mid.set_leg_pos(0, 0, 0)
        self.left_back.set_leg_pos(0, 0, 0)
        self.right_front.set_leg_pos(0, 0, 0)
        self.right_mid.set_leg_pos(0, 0, 0)
        self.right_back.set_leg_pos(0, 0, 0)

