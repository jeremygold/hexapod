#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState

class JointStateMessage():
    def __init__(self, name, position, velocity, effort):
        self.name = name
        self.position = position
        self.velocity = velocity
        self.effort = effort

class JointStatePublisher():
    def __init__(self):
        rospy.init_node('hexapod_controller', anonymous=False)
        rate = rospy.get_param('~rate', 10)
        r = rospy.Rate(rate)
        
        self.joints = list()
        
        for side in ["l", "r"]:
            for pos in ["f", "m", "b"]:
                for joint in ["h", "m", "s"]:
                    self.joints.append(side + pos + joint + "_joint")
                        
        self.servos = list()
        self.controllers = list()
        self.joint_states = dict({})
        
        for joint in self.joints:
            # Remove "_joint" from the end of the joint name to get the controller names.
            servo = joint.split("_joint")[0]
            self.joint_states[joint] = JointStateMessage(joint, 0.0, 0.0, 0.0)
            self.controllers.append("/hexapod/" + servo + "_position_controller")
                           
        # Start controller state subscribers
        [rospy.loginfo("Using controller: " + c) for c in self.controllers]
        [rospy.Subscriber(c + '/state', JointState, self.controller_state_handler) for c in self.controllers]
     
        # Start publisher
        self.joint_states_pub = rospy.Publisher('/joint_states', JointState, queue_size=1)
       
        rospy.loginfo("Starting Hexapod Joint State Publisher at " + str(rate) + "Hz")
       
        while not rospy.is_shutdown():
            self.publish_joint_states()
            r.sleep()
           
    def controller_state_handler(self, msg):
        js = JointStateMessage(msg.name, msg.position, msg.velocity, msg.effort)
#        rospy.loginfo("jn="+msg.name+",jp="+str(msg.current_pos*100))
        self.joint_states[msg.name] = js
       
    def publish_joint_states(self):
        # Construct message & publish joint states
        msg = JointState()
        msg.name = []
        msg.position = []
        msg.velocity = []
        msg.effort = []
       
        for joint in self.joint_states.values():
#            rospy.loginfo("jn="+joint.name+",jp="+str(joint.position*100))
            msg.name.append(joint.name)
            msg.position.append(joint.position)
            msg.velocity.append(joint.velocity)
            msg.effort.append(joint.effort)
           
        msg.header.stamp = rospy.Time.now()
        self.joint_states_pub.publish(msg)
        
if __name__ == '__main__':
    try:
        s = JointStatePublisher()
        rospy.spin()
    except rospy.ROSInterruptException: pass

