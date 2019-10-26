#!/bin/bash

set IFS=$'\t'

count=0 
while read  a b c d e f g
do 
	count=$((count+1))
	echo -e "$count\t$a\t$c\t$g"
done < example_people_data.tsv 
