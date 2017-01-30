#!/bin/zsh

# Ref http://raspberrypi.stackexchange.com/questions/58897/run-script-in-terminal-after-boot
/usr/bin/tmux new-session -d -s HexapodSession
/usr/bin/tmux set-option -t HexapodSession set-remain-on-exit on
/usr/bin/tmux new-window -d -n "RosCore" -t HexapodSession:1 -c '/home/pi/hexapod/ROS' 'sudo -u pi /home/pi/hexapod/Rpi/StartupScripts/HexapodRosCore.zsh'
sleep 10
/usr/bin/tmux new-window -d -n "RosWebControl" -t HexapodSession:2 -c '/home/pi/hexapod/ROS' 'sudo -u pi /home/pi/hexapod/Rpi/StartupScripts/HexapodRosWebControl.zsh'

exit 0
