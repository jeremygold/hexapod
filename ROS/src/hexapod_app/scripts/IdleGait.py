import rospy
from Gait import Gait

class IdleGait(Gait):
    def update(self, robot):
        robot.left_front.set_leg_pos(0, 0)
        robot.left_mid.set_leg_pos(0, 0)
        robot.left_back.set_leg_pos(0, 0)
        robot.right_front.set_leg_pos(0, 0)
        robot.right_mid.set_leg_pos(0, 0)
        robot.right_back.set_leg_pos(0, 0)
