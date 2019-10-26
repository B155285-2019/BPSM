#!/bin/python3
my_file = open("genomic_dna2.txt")
dna_seq = my_file.read()

exon_file = open("exons.txt")
exons_info = exon_file.read()

out_file = open("concat_exons.txt", "w")

dna_seq1 = dna_seq.rstrip('\n')
exons_info = exons_info.rstrip('\n')
exons_lines = exons_info.split('\n')

concat_exons = ''
for lines in exons_lines:
	st_end = lines.split(',')
	concat_exons += dna_seq1[int(st_end[0]):int(st_end[1])]
	#print(dna_seq1[int(st_end[0]):int(st_end[1])])
out_file.write(concat_exons)
