#!/usr/bin/env python
## RPI SERVO PWM HAL
## Broadcast Servo Position (angle in degrees) at specified rate, and listen for commands to change position
## Some good reference data on HX12K servos here:
    ## http://www.rcuniverse.com/forum/rc-radios-transmitters-receivers-servos-gyros-157/11523159-hextronik-hx12k-standard-metal-gear-servo-55g-10kg-16sec.html

import rospy
import os

from std_msgs.msg import Int16
from sensor_msgs.msg import JointState
from Servo import *

rbh_servo = Servo(9)
rbt_servo = Servo(10)
rbs_servo = Servo(11)

rmh_servo = Servo(12)
rmt_servo = Servo(13)
rms_servo = Servo(14)

rfh_servo = Servo(15)
rft_servo = Servo(16)
rfs_servo = Servo(17)

lbh_servo = Servo(0)
lbt_servo = Servo(1)
lbs_servo = Servo(2)

lmh_servo = Servo(3)
lmt_servo = Servo(4)
lms_servo = Servo(5)

lfh_servo = Servo(6)
lft_servo = Servo(7)
lfs_servo = Servo(8)

# Set servo position in degrees
def set_joint_position(joint_state):
    # rospy.loginfo("In set_joint_position, joint_state = %s", repr(joint_state))

    for index, name in enumerate(joint_state.name):
        position = joint_state.position[index]

        if name == "/left/front/hip":
            lfh_servo.set_servo_angle(position)
        elif name == "/left/front/thigh":
            lft_servo.set_servo_angle(position)
        elif name == "/left/front/shin":
            lfs_servo.set_servo_angle(position)

def monitor_servos():
    rospy.Subscriber('/joint_states', JointState, set_joint_position)
    rospy.spin()

if __name__ == '__main__':
    try:
        rospy.init_node('servo_hal', anonymous=False)
        rospy.loginfo("Initializing")
        monitor_servos()

    except rospy.ROSInterruptException:
        pass
