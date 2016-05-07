#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Int16

class JointStatePublisher():
    def __init__(self):
        rospy.init_node('hexapod_controller', anonymous=False)

        rate = rospy.get_param('~rate', 2)
        r = rospy.Rate(rate)
        
        self.joints = list()
        
        for side in ["left", "right"]:
            for pos in ["front", "mid", "back"]:
                for joint in ["hip", "thigh", "shin"]:
                    self.joints.append("/" + side + "/" + pos + "/" + joint)
                        
        self.controllers = list()
        self.joint_states = dict({})
        
        for joint in self.joints:
            self.joint_states[joint] = 0
            self.controllers.append(joint)
                           
        # Start controller state subscribers
        [rospy.loginfo("Using controller: " + c) for c in self.controllers]
        [rospy.Subscriber(c + '/command', Int16, self.controller_state_handler) for c in self.controllers]
     
        # Start publisher
        self.joint_states_pub = rospy.Publisher('/joint_states', JointState, queue_size=1)
       
        rospy.loginfo("Starting Hexapod Joint State Publisher at " + str(rate) + "Hz")
       
        while not rospy.is_shutdown():
            self.publish_joint_states()
            r.sleep()
           
    def controller_state_handler(self, data):
        joint_name = data._connection_header['topic'].replace('/command','')
        self.joint_states[joint_name] = data.data
       
    def publish_joint_states(self):
        # Construct message & publish joint states
        msg = JointState()
        msg.name = []
        msg.position = []
        msg.velocity = []
        msg.effort = []
       
        for joint_name in self.joint_states.keys():
            msg.name.append(joint_name)
            msg.position.append(self.joint_states[joint_name])
            msg.velocity.append(0)
            msg.effort.append(0)
           
        msg.header.stamp = rospy.Time.now()
        self.joint_states_pub.publish(msg)
        
if __name__ == '__main__':
    try:
        s = JointStatePublisher()
        rospy.spin()
    except rospy.ROSInterruptException: pass

