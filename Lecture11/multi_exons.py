#!/bin/python3
dna_seq = open("genomic_dna2.txt").read().rstrip('\n')
exons_info = open("exons.txt").read().rstrip('\n')

out_file = open("concat_exons.txt", "w")
exons_lines = exons_info.split('\n')

concat_exons = ''
for lines in exons_lines:
	st_end = lines.split(',')
	concat_exons += dna_seq[(int(st_end[0])-1):int(st_end[1])]
	print(dna_seq[(int(st_end[0])-1):int(st_end[1])])
out_file.write(concat_exons)
