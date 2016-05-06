#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
from signal import signal,SIGINT
import sys

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/hip")
def setHip():
    value = int(request.args.get("hip"))
    rospy.loginfo("Setting Hip Position value to {0:d}".format(value))
    hip_pub.publish(value)
    return "Hip value {0:d}".format(value)

@app.route("/thigh")
def setThigh():
    value = int(request.args.get("thigh"))
    rospy.loginfo("Setting Thigh Position value to {0:d}".format(value))
    thigh_pub.publish(value)
    return "Thigh value {0:d}".format(value)

@app.route("/shin")
def setShin):
    value = int(request.args.get("shin"))
    rospy.loginfo("Setting Shin Position value to {0:d}".format(value))
    shin_pub.publish(value)
    return "Shin value {0:d}".format(value)

def initRospy():
    global hip_pub
    global thigh_pub
    global shin_pub
    rospy.init_node('web_servo_control', anonymous=True)
    hip_pub = rospy.Publisher('hip', Int16, queue_size=10)
    thigh_pub = rospy.Publisher('thigh', Int16, queue_size=10)
    shin_pub = rospy.Publisher('shin', Int16, queue_size=10)

def sigintHandler(signal, frame):
    rospy.loginfo("Terminating webserver")
    sys.exit(0)

if __name__ == '__main__':
    signal(SIGINT, sigintHandler)
    initRospy()
    print "Starting webserver"
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
