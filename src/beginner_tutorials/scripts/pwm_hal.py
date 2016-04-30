#!/usr/bin/env python
## RPI SERVO PWM HAL
## Broadcast Servo Position (angle in degrees) at specified rate, and listen for commands to change position
## Some good reference data on HX12K servos here:
    ## http://www.rcuniverse.com/forum/rc-radios-transmitters-receivers-servos-gyros-157/11523159-hextronik-hx12k-standard-metal-gear-servo-55g-10kg-16sec.html

import rospy
import os

from std_msgs.msg import Int16

angle_deg = 0

# Set servo position in degrees
def setServoPosition(data):
    global angle_deg
    rospy.loginfo(rospy.get_caller_id() + ' Command Received: %s ', data.data)

    # Compensate for 500us - 2500us representing +/- 90 degrees, and ServoBlaster is in units of 10us
    angle_deg = data.data
    pwm_delay = 150 - ((angle_deg) * 100 / 90)

    # Send to PWM output
    servo_command = "%u=%u\n" % (3, pwm_delay)
    with open("/dev/servoblaster", "wb") as servo_device:
        servo_device.write(servo_command)

def led_hal():
    global angle_deg
    pub = rospy.Publisher('state', Int16, queue_size=10)
    rospy.Subscriber('command', Int16, setServoPosition)

    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():
        rospy.loginfo("Servo Position is {:d}".format(angle_deg))
        pub.publish(angle_deg)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('servo_hal', anonymous=False)
        rospy.loginfo("Initializing")
        led_hal()

    except rospy.ROSInterruptException:
        pass
