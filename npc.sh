#!/bin/bash

bdir=$(dirname "$0")
npcTraits=(abilities.txt abilities.txt appearances.txt talents.txt mannerisms.txt interactions.txt good_evil.txt law_chaos.txt neutral_other.txt bonds.txt flaws.txt)
prefices=("High ability" "Low ability" "Appearance" "Talent" "Mannerisms" "Interraction" "Good/Evil ideal" "Law/Chaos ideal". "Neutral/Other ideal" "Bond" "Flaw or secret") 

for i in ${!npcTraits[@]}; do
	echo "${prefices[$i]}: " $("${bdir}/rline.sh" "${bdir}/assets/${npcTraits[$i]}")
done
