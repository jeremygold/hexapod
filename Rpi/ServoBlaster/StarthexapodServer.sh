#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# user/servod --p1pins="7,8,10,11,12,13,15,16,18,19,21,22"
user/servod --p1pins="15,16,18,19,21,22,23,24,26,29,31,32,33,35,36,37,38,40"

