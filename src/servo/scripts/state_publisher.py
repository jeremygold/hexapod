#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import TransformStamped
import tf 
import math

joint_pub = rospy.Publisher('joint_states', JointState, queue_size=10)
broadcaster = tf.TransformBroadcaster()
# message declarations
joint_state = JointState()
joint_state.header = Header()
joint_state.name = ["swivel"]



def updateState(data):
    # When we receive an updated position, convert to angle, and send to tf subscriber
    global joint_pub
    global broadcaster
    global joint_state

    swivel = (data.data - 150) * math.pi / 180

    rospy.loginfo("Updating servo position: {:d}".format(data.data))

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

def move_robot():
    global joint_pub
    rospy.init_node('state_publisher')
    rospy.Subscriber('state', Int16, updateState)
    rospy.spin()

if __name__ == '__main__':
    move_robot()
