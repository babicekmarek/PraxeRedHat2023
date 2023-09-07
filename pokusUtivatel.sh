#!/bin/bash
if [ $1 == "" ]; then
	exit 1
fi
rpm -q $1

if [ $1 != 0 ]; then 
	sudo dnf install -y $1

read -p "Do you want to erase? (yes/no) " yn
       case $yn in
	       yes ) echo ok, erasing...;;
               no ) echo exiting...;;
               * ) echo invalid response;
                        exit 1;;
        esac

else
	sudo dnf erase -y $1
fi
exit 0


