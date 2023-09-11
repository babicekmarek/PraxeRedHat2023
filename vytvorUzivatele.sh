#!/bin/bash

for i in $(seq 1 10)

do
	id alice$i
	if [[ $? ]]; then
		echo "uzivatel vytvarim"
		sudo useradd "alice$i"
		sudo passwd alice$i	
	else
		echo "uzivatel neexistuje"
	fi
done
