#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from flask import Flask
from flask import render_template

app = Flask(__name__)

pub = rospy.Publisher('command', String, queue_size=10)
led_state = "low"

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route("/on")
def turnOn():
    rospy.loginfo("Turning LED on")
    pub.publish("high")
    return "LED on"

@app.route("/off")
def turnOff():
    rospy.loginfo("Turning LED off")
    pub.publish("low")
    return "LED off"

def initRospy():
    global led_state
    rospy.init_node('led_control', anonymous=True)

    # rate = rospy.Rate(2)

    # while not rospy.is_shutdown():
        # if led_state == "low":
            # led_state = "high"
        # else:
            # led_state = "low"
# 
        # rospy.loginfo("LED is " + led_state)
        # pub.publish(led_state)
        # rate.sleep()

if __name__ == '__main__':
    initRospy()
    app.run(debug=True, host='0.0.0.0')
