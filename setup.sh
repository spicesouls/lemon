#!/bin/bash
YELLOW='\033[0;33m'
RED='\033[0;31m'
GREEN='\033[1;32m'
RESET='\033[0m'
echo -e " .=======================================."
echo -e " |              $YELLOW  SETUP $RESET                 |"
echo -e " '======================================='"
echo ""

if which apt > /dev/null; then
        echo -e "Checking For apt..............[$GREEN Installed $RESET]"
else
        echo -e "Checking For apt..........[$RED Not Installed $RESET]"
fi

if which python3 > /dev/null; then
        echo -e "Checking For Python 3.........[$GREEN Installed $RESET]"
else
        echo -e "Checking For Python 3.....[$RED Not Installed $RESET]"
	apt install python3
fi

if which pip > /dev/null; then
        echo -e "Checking For Pip..............[$GREEN Installed $RESET]"
else
        echo -e "Checking For Pip..........[$RED Not Installed $RESET]"
	apt install python3-pip
fi

if which msfvenom > /dev/null; then
	echo -e "Checking For MSF Venom........[$GREEN Installed $RESET]"
else
	echo -e "Checking For MSF Venom....[$RED Not Installed $RESET]"
fi

if which msfconsole > /dev/null; then
        echo -e "Checking For MSF Console......[$GREEN Installed $RESET]"
else
        echo -e "Checking For MSF Console..[$RED Not Installed $RESET]"
fi

echo ""
echo ""
echo -e "[$YELLOW+$RESET] Installing Python Modules"

pip install colorama
pip install requests

echo ""
echo ""
echo -e "[$YELLOW+$RESET] Finished!"
echo "(Make sure you have the scripts listed above all installed, otherwise Lemon can not function properly.)"
