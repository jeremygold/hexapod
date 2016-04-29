#!/usr/bin/env python
## RPI GPIO LED HAL
## broadcast LED state at specified rate, and listen for commands to change state

import rospy
import os

from std_msgs.msg import Int16

pwmValue = 0

def setpwmValue(data):
    global pwmValue
    rospy.loginfo(rospy.get_caller_id() + ' Command Received: %s ', data.data)
    pwmValue = data.data

    # Send to PWM output
    servo_command = "%u=%u\n" % (3, pwmValue)
    with open("/dev/servoblaster", "wb") as servo_device:
        servo_device.write(servo_command)

def led_hal():
    global pwmValue
    pub = rospy.Publisher('state', Int16, queue_size=10)
    rospy.Subscriber('command', Int16, setpwmValue)

    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():
        rospy.loginfo("PWM Value is {:d}".format(pwmValue))
        pub.publish(pwmValue)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('led_hal', anonymous=False)
        rospy.loginfo("Initializing")
        led_hal()

    except rospy.ROSInterruptException:
        pass
