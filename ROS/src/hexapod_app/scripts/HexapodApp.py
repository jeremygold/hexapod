#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from time import sleep
from Robot import Robot
from IdleGait import IdleGait
from WalkGait import WalkGait
from WalkBackGait import WalkBackGait
from PressupGait import PressupGait
from TurnLeftGait import TurnLeftGait
from TurnRightGait import TurnRightGait
from CrabLeftGait import CrabLeftGait
from CrabRightGait import CrabRightGait
from ForwardRightGait import ForwardRightGait
from ForwardLeftGait import ForwardLeftGait

class HexapodApp:
    def __init__(self):
        rospy.init_node('hexapod_app', anonymous=True)
        self.robot = Robot()
        rospy.Subscriber('gait_command', String, self.handle_gait_command)

    def handle_gait_command(self, data):
        command = data.data
        rospy.loginfo("Changing Gait to " + command)

        if command == "Idle":
            self.robot.gait = IdleGait()

        elif command == "Walk":
            self.robot.gait = WalkGait()

        elif command == "WalkBack":
            self.robot.gait = WalkBackGait()

        elif command == "ForwardRight":
            self.robot.gait = ForwardRightGait()

        elif command == "ForwardLeft":
            self.robot.gait = ForwardLeftGait()

        elif command == "Pressup":
            self.robot.gait = PressupGait()

        elif command == "TurnRight":
            self.robot.gait = TurnRightGait()

        elif command == "TurnLeft":
            self.robot.gait = TurnLeftGait()

        elif command == "CrabLeft":
            self.robot.gait = CrabLeftGait()

        elif command == "CrabRight":
            self.robot.gait = CrabRightGait()

        else:
            self.robot.gait = IdleGait()


    def run(self):
        r = rospy.Rate(50)

        while not rospy.is_shutdown():
            self.robot.update()
            r.sleep()

if __name__ == '__main__':
    app = HexapodApp()
    app.run()

