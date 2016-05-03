#!/usr/bin/env python
## RPI SERVO PWM HAL
## Broadcast Servo Position (angle in degrees) at specified rate, and listen for commands to change position
## Some good reference data on HX12K servos here:
    ## http://www.rcuniverse.com/forum/rc-radios-transmitters-receivers-servos-gyros-157/11523159-hextronik-hx12k-standard-metal-gear-servo-55g-10kg-16sec.html

import rospy
import os

from std_msgs.msg import Int16
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

# Set servo position in degrees
def setServoPosition(data):
    rospy.loginfo(rospy.get_caller_id() + ' Command Received: %s ', data.data)
    rbh_servo.set_servo_angle(data.data)
    rbt_servo.set_servo_angle(data.data)
    rbs_servo.set_servo_angle(data.data)

    rmh_servo.set_servo_angle(data.data)
    rmt_servo.set_servo_angle(data.data)
    rms_servo.set_servo_angle(data.data)

    rfh_servo.set_servo_angle(data.data)
    rft_servo.set_servo_angle(data.data)
    rfs_servo.set_servo_angle(data.data)

def led_hal():
    pub = rospy.Publisher('state', Int16, queue_size=10)
    rospy.Subscriber('command', Int16, setServoPosition)
    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():
        # rospy.loginfo("Servo Position is {:d}".format(rbs_servo.get_servo_angle()))
        # TODO: How do I publish more servo states?
        pub.publish(rbs_servo.get_servo_angle())
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('servo_hal', anonymous=False)
        rospy.loginfo("Initializing")
        led_hal()

    except rospy.ROSInterruptException:
        pass
