#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

pub = rospy.Publisher('command', Int16, queue_size=10)
led_state = "low"

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/on")
def turnOn():
    rospy.loginfo("Turning LED on")
    pub.publish(250)
    return "LED on"

@app.route("/off")
def turnOff():
    rospy.loginfo("Turning LED off")
    pub.publish(50)
    return "LED off"

@app.route("/set")
def setValue():
    value = int(request.args.get("value"))
    rospy.loginfo("Setting LED value to {0:d}".format(value))
    pub.publish(value)
    return "LED value {0:d}".format(value)


def initRospy():
    global led_state
    rospy.init_node('led_control', anonymous=True)

if __name__ == '__main__':
    initRospy()
    print "Starting webserver"
    app.run(debug=True, host='0.0.0.0')
