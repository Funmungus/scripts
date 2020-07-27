#!/bin/bash

if [[ $# -lt 1 ]]; then exit -1; fi

sed -n $((RANDOM % $(wc -l "$1" | awk '{print $1}') + 1))p "$1"
