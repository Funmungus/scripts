#!/bin/bash

if [[ $# -lt 1 ]]; then
	printf "1d20 = %d\n" $((RANDOM % 20 + 1))
	exit 0
fi
if [[ $# -lt 2 ]]; then
	printf "1d%d = %d\n" $1 $((RANDOM % $1 + 1))
	exit 0
fi
die=$(echo $2 | egrep '^[a-zA-Z]')
if [[ -z "$die" ]]; then
	die=$2
else
	die=$(echo $2 | sed 's/^[a-zA-Z]*//')
fi
total=0
count=$1
echo "${count}d${die}:"
while [[ $count -ne 0 ]]; do
	current=$((RANDOM % $die + 1))
	calculated=$((current ${*:3}))
	printf "d%d ${*:3} = %d\n" $die $calculated
	total=$((total + calculated))
	count=$((count - 1))
done
echo total = $total
