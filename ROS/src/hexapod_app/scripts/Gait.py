from enum import Enum

class LegState (Enum):
    idle = 1
    going_up = 2
    going_forward = 3
    going_down = 4
    going_back = 5
    lifting_legs = 6

class Gait:
    def __init__(self):
        self.leg_state = LegState.idle
        self.vert_angle = 0
        self.horiz_angle = 0

    def update(self, robot):
        raise NotImlementedError("Need to implement Gait for subclass")

