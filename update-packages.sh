#!/bin/zsh

# Ref http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Indigo%20on%20Raspberry%20Pi, section Maintaining a Source Checkout
 
cd ~/ros_catkin_ws
rosinstall_generator ros_comm sensor_msgs tf --rosdistro indigo --deps --wet-only --exclude roslisp --tar > indigo-ros.rosinstall

wstool merge -t src indigo-ros.rosinstall
wstool update -t src

rosdep install --from-paths src --ignore-src --rosdistro indigo -y -r --os=debian:jessie

sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/indigo

