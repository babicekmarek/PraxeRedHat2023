#!/bin/bash
# tisk uzivatel bash jmeno
#

var="/etc/passwd"
while read -r line; do
	user=$(echo "$line" |cut -d':' -f1)
	name=$(echo "$line" |cut -d':' -f5)
	bash=$(echo "$line" |cut -d':' -f7)
	echo "$user $bash $name"
done < $var
exit 0
