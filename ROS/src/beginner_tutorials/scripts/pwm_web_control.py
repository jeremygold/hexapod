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

@app.route("/set")
def setValue():
    value = int(request.args.get("value"))
    rospy.loginfo("Setting Servo Position value to {0:d}".format(value))
    pub.publish(value)
    return "PWM value {0:d}".format(value)

def initRospy():
    global pub
    rospy.init_node('web_servo_control', anonymous=True)
    pub = rospy.Publisher('command', Int16, queue_size=10)

def sigintHandler(signal, frame):
    rospy.loginfo("Terminating webserver")
    sys.exit(0)

if __name__ == '__main__':
    signal(SIGINT, sigintHandler)
    initRospy()
    print "Starting webserver"
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
