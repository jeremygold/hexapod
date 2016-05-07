#!/usr/bin/env python
## Hexapod Servo Driver

## Listen for /joint_states updates, and configure servos accordingly

## Some good reference data on HX12K servos here:
    ## http://www.rcuniverse.com/forum/rc-radios-transmitters-receivers-servos-gyros-157/11523159-hextronik-hx12k-standard-metal-gear-servo-55g-10kg-16sec.html

import rospy

from sensor_msgs.msg import JointState
from Servo import *

servos = dict({})

def set_joint_position(joint_state):
    for index, name in enumerate(joint_state.name):
        if name in servos:
            position = joint_state.position[index]
            servos[name].set_servo_angle(position)

def init_servos():
    global servos
    servos['/left/back/hip'] = Servo(0)
    servos['/left/back/thigh'] = Servo(1)
    servos['/left/back/shin'] = Servo(2)

    servos['/left/mid/hip'] = Servo(3)
    servos['/left/mid/thigh'] = Servo(4)
    servos['/left/mid/shin'] = Servo(5)

    servos['/left/front/hip'] = Servo(6)
    servos['/left/front/thigh'] = Servo(7)
    servos['/left/front/shin'] = Servo(8)

    servos['/right/back/hip'] = Servo(9)
    servos['/right/back/thigh'] = Servo(10)
    servos['/right/back/shin'] = Servo(11)

    servos['/right/mid/hip'] = Servo(12)
    servos['/right/mid/thigh'] = Servo(13)
    servos['/right/mid/shin'] = Servo(14)

    servos['/right/front/hip'] = Servo(15)
    servos['/right/front/thigh'] = Servo(16)
    servos['/right/front/shin'] = Servo(17)

def monitor_servos():
    rospy.Subscriber('/joint_states', JointState, set_joint_position)
    rospy.spin()

if __name__ == '__main__':
    try:
        rospy.init_node('servo_driver', anonymous=False)
        init_servos()
        monitor_servos()

    except rospy.ROSInterruptException:
        pass
