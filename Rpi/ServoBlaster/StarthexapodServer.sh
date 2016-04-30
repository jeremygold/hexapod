#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

user/servod --p1pins="7,8,10,11,12,13,15,16,18,19,21,22"

