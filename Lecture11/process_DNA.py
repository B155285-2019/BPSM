#!/bin/python3
my_file = open("input.txt")
dna_seq = my_file.read()

out_file = open("cleaned_DNA.txt", "w")
dna_seq1 = dna_seq.rstrip('\n')

dna_lines = dna_seq1.split('\n')

for lines in dna_lines:
	out_file.write(lines[15:]+ '\n')
	print(len(lines[15:]))


#adapter_dna = set.intersection(set(dna_lines[0]),set(dna_lines[1]))
#print(set(dna_lines[0]))	
#print(adapter_dna)
