#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import TransformStamped
import tf 
import math

def move_robot():
    rospy.init_node('state_publisher')
    joint_pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    broadcaster = tf.TransformBroadcaster()

    degree = math.pi / 180.0

    # robot state
    swivel = 0
    swivinc = 1 * degree

    # message declarations
    joint_state = JointState()
    joint_state.header = Header()
    joint_state.name = ["swivel"]

    rate = rospy.Rate(30)

    while not rospy.is_shutdown():
        # update joint_state
        joint_state.header.stamp = rospy.Time.now()
        joint_state.position = [swivel]
        joint_state.velocity = []
        joint_state.effort = []

        # send the joint state and transform
        joint_pub.publish(joint_state)

        # update transform
        # (moving in a circle with radius=2)
        broadcaster.sendTransform((0, 0, 0),
                                  tf.transformations.quaternion_from_euler(0, 0, swivel + math.pi / 2),
                                  rospy.Time.now(),
                                  "axis",
                                  "odom")

        #  Create new robot state
        swivel += swivinc
        if swivel > math.pi / 4 or swivel < 0:
            swivinc *= -1

        #  This will adjust as needed per iteration
        rate.sleep()

if __name__ == '__main__':
    move_robot()
