#!/bin/zsh

# Master is running on HexapodPi
# export ROS_MASTER_URI=http://HexapodPi:11311
#
# Master is running on ubuntu VM
# export ROS_MASTER_URI=http://ubuntu:11311

# Note: ROS_IP is this hosts IP address
if [ `hostname` = Cappuccino ]
then
    export ROS_IP=192.168.1.107
    export ROS_MASTER_URI=http://Cappuccino:11311
    source /pub/projects/hexapod/ROS/devel/setup.zsh
else
    export ROS_IP=192.168.1.128
    source /home/pi/hexapod/ROS/devel/setup.zsh
fi


