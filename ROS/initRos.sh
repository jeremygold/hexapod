#!/bin/zsh

# Master is running on HexapodPi
# export ROS_MASTER_URI=http://HexapodPi:11311
#
# Master is running on current host
LOCAL_IP=`hostname -I | tr -d '[:space:]'`
export ROS_MASTER_URI=http://$LOCAL_IP:11311
export ROS_IP=$LOCAL_IP

# Note: ROS_IP is this hosts IP address
case `hostname` in 
    ubuntu-vbox)
        # export ROS_IP=10.0.2.15
        source /pub/projects/hexapod/ROS/devel/setup.zsh
        ;;

    Cappuccino)
        echo "Configuring on Cappucino"
        # export ROS_IP=192.168.1.107
        source /pub/projects/hexapod/ROS/devel/setup.zsh
        ;;
    *)
        echo "Configuring on HexapodPi"
        # at ike: export ROS_IP=192.168.2.125
        # export ROS_IP=192.168.1.129
        source /home/pi/hexapod/ROS/devel/setup.zsh
        ;;
esac

