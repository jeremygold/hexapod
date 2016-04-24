#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

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
    rospy.loginfo("Setting PWM value to {0:d}".format(value))
    pub.publish(value)
    return "PWM value {0:d}".format(value)

def initRospy():
    global pub
    rospy.init_node('led_control', anonymous=True)
    pub = rospy.Publisher('command', Int16, queue_size=10)

if __name__ == '__main__':
    initRospy()
    print "Starting webserver"
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
