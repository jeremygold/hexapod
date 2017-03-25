#!/bin/zsh

echo
echo "##### initRos.sh Starting #####"

# Master is running on HexapodPi
# export ROS_MASTER_URI=http://HexapodPi:11311
#
# Master is running on current host
all_ips=`hostname -I`
ip_array=("${(@s/ /)all_ips}")
export LOCAL_IP=$ip_array[1] # Assume first IP address is the one we're after
# export LOCAL_IP=`hostname -I | tr -d '[:space:]'`

export ROS_MASTER_URI=http://$LOCAL_IP:11311
export ROS_IP=$LOCAL_IP

echo "ROS_IP =" $ROS_IP
echo "ROS_MASTER_URI =" $ROS_MASTER_URI
echo "Configuring on" `hostname`

case `hostname` in 
    ubuntu-vbox)
        source /pub/projects/hexapod/ROS/devel/setup.zsh
        ;;

    Cappuccino)
        source /pub/projects/hexapod/ROS/devel/setup.zsh
        ;;
    *)
        source /home/pi/hexapod/ROS/devel/setup.zsh
        ;;
esac

echo "##### initRos.sh Done #####"
echo

