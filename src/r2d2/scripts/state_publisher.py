#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
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
    tilt = 0.0
    tinc = degree
    swivel = 0
    angle = 0
    height = 0
    hinc = 0.005

    # message declarations
    odom_trans = TransformStamped()
    joint_state = JointState()
    joint_state.name = ["swivel", "tilt", "periscope"]

    odom_trans.header.frame_id = "odom"
    odom_trans.child_frame_id = "axis"

    rate = rospy.Rate(30)

    while not rospy.is_shutdown():
        # update joint_state
        joint_state.header.stamp = rospy.Time.now(),
        joint_state.position = [swivel, tilt, height]

        #  update transform
        #  (moving in a circle with radius=2)
        odom_trans.header.stamp = rospy.Time.now()
        q = tf.transformations.quaternion_from_euler(0, 0, angle + math.pi / 2)
        odom_trans.transform.rotation = Quaternion(*q)

        # send the joint state and transform
        joint_pub.publish(joint_state)
        broadcaster.sendTransform((math.cos(angle) * 2, math.sin(angle) * 2, 0.7),
                                  tf.transformations.quaternion_from_euler(0, 0, angle + math.pi / 2),
                                  rospy.Time.now(),
                                  "odom",
                                  "axis")

        #  Create new robot state
        tilt += tinc
        if tilt < -.5 or tilt > 0: 
            tinc *= -1
            height += hinc
        if height > .2 or height < 0:
            hinc *= -1
        swivel += degree
        angle += degree / 4

        #  This will adjust as needed per iteration
        rate.sleep()
    

if __name__ == '__main__':
    move_robot()
