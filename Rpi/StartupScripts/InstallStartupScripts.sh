#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Install and run servoblaster init script
cp servoblaster /etc/init.d/
chmod 755 /etc/init.d/servoblaster
/etc/init.d/servoblaster start

# Update to run by default
update-rc.d servoblaster defaults
