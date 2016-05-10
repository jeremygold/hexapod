import rospy
from Leg import Leg
from time import sleep

class Robot:
    def __init__(self):
        self.left_front = Leg("left", "front")
        self.left_mid = Leg("left", "mid")
        self.left_back = Leg("left", "back")
        self.right_front = Leg("right", "front")
        self.right_mid = Leg("right", "mid")
        self.right_back = Leg("right", "back")

        sleep(1)

    

