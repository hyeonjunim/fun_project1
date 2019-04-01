#!/bin/bash

while true;
do
	read -p "Enter a new word: " Word
        if [ $Word == quit ]; then
                break
        elif [ $Word == list ]; then
                echo ${array_test[@]}
                break
        else
                array_test=(${array_test[@]} "$Word")
                echo ${#array_test[@]}
        fi
done
