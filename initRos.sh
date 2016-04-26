#!/bin/zsh

# Master is running on HexapodPi
export ROS_MASTER_URI=http://HexapodPi:11311
#
# Master is running on ubuntu VM
# export ROS_MASTER_URI=http://ubuntu:11311

# Note: ROS_IP is this hosts IP address
export ROS_IP=192.168.1.123
source ./devel/setup.zsh

