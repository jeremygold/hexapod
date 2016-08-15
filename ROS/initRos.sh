#!/bin/zsh

# Master is running on HexapodPi
# export ROS_MASTER_URI=http://HexapodPi:11311
#
# Master is running on current host
export ROS_MASTER_URI=http://`hostname`:11311

# Note: ROS_IP is this hosts IP address
case `hostname` in 
    ubuntu-vbox)
        export ROS_IP=10.0.2.15
        source /pub/projects/hexapod/ROS/devel/setup.zsh
        ;;

    Cappuccino)
        export ROS_IP=192.168.1.107
        source /pub/projects/hexapod/ROS/devel/setup.zsh
        ;;
    *)
        export ROS_IP=192.168.1.117
        source /home/pi/hexapod/ROS/devel/setup.zsh
        ;;
esac


