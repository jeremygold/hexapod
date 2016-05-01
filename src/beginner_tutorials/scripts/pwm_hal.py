#!/usr/bin/env python
## RPI SERVO PWM HAL
## Broadcast Servo Position (angle in degrees) at specified rate, and listen for commands to change position
## Some good reference data on HX12K servos here:
    ## http://www.rcuniverse.com/forum/rc-radios-transmitters-receivers-servos-gyros-157/11523159-hextronik-hx12k-standard-metal-gear-servo-55g-10kg-16sec.html

import rospy
import os

from std_msgs.msg import Int16
from Servo import *

angle_deg = 0

lfs_servo = Servo(8)

# Set servo position in degrees
def setServoPosition(data):
    global angle_deg
    rospy.loginfo(rospy.get_caller_id() + ' Command Received: %s ', data.data)
    lfs_servo.set_servo_angle(data.data)

def led_hal():
    global angle_deg
    pub = rospy.Publisher('state', Int16, queue_size=10)
    rospy.Subscriber('command', Int16, setServoPosition)

    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():
        angle_deg = lfs_servo.get_servo_angle()
        # rospy.loginfo("Servo Position is {:d}".format(angle_deg))
        pub.publish(angle_deg)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('servo_hal', anonymous=False)
        rospy.loginfo("Initializing")
        led_hal()

    except rospy.ROSInterruptException:
        pass
