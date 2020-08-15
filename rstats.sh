#!/usr/bin/env bash

stats=(STR DEX CON INT WIS CHA)

for i in ${stats[@]}; do
	echo "$i: " $((RANDOM % 17 + 4))
done
