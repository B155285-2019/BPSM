#!/bin/python3
dna_seq = open("input.txt").read().rstrip('\n')
out_file = open("cleaned_DNA.txt", "w")
dna_lines = dna_seq.split('\n')

for lines in dna_lines:
	out_file.write(lines[14:]+ '\n')
	print(len(lines[14:]))
