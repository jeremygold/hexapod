#!/bin/zsh

# Master is running on HexapodPi
export ROS_MASTER_URI=http://HexapodPi:11311
#
# Master is running on ubuntu VM
# export ROS_MASTER_URI=http://ubuntu:11311

# Note: ROS_IP is this hosts IP address
if [ "$HOSTNAME" = ubuntu ]; then
    export ROS_IP=192.168.1.123
else
    export ROS_IP=192.168.1.128
fi

source /home/pi/hexapod/ROS/devel/setup.zsh

