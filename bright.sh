#!/bin/bash

#run as root to change file permissions, then feel free to run as normal user
# ./bright [ + | - | level]
#    where 0 < level <= 100
#
#cf https://wiki.archlinux.org/title/Backlight#ACPI

if [ $EUID == 0 ]; then
	chmod 666 /sys/class/backlight/**/brightness
	chmod 444 /sys/class/backlight/**/max_brightness
fi

max=$(</sys/class/backlight/**/max_brightness)
current=$(</sys/class/backlight/**/brightness)
tenth=$(echo "scale=0;$max/10" | bc -l)

if [ $# == 0 ]; then
	echo "scale=0;$current*100/$max" | bc -l
	exit
elif [ $# == 1 ]; then
	if [ $1 == "+" ]; then
		if [ $(echo "$max-$current" | bc -l) -lt $tenth ]; then
			echo $max > /sys/class/backlight/**/brightness
		else
			echo $(echo "scale=0;$current+$tenth" | bc -l) > /sys/class/backlight/**/brightness
		fi
	elif [ $1 == "-" ]; then
		if [ $current -lt $(echo "scale=0;2*$tenth" | bc -l) ]; then
			echo $tenth > /sys/class/backlight/**/brightness
		else
			echo $(echo "scale=0;$current-$tenth" | bc -l) > /sys/class/backlight/**/brightness
		fi
	elif [ $1 -gt 0 ]; then
		echo $(echo "scale=0;$1*$max/100" | bc -l) > /sys/class/backlight/**/brightness
	fi
fi

