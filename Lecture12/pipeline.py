#!/bin/python3

data_table = open("data.csv").read().rstrip('\n')

data_lines = data_table.split('\n')
for lines in data_lines:
	data_seq = lines.split(',')
#	print(data_seq[2])
	gene_seq = data_seq[1]
	gene_seq_len = len(gene_seq)
	if len(data_seq[1]) > 90 and len(data_seq[1]) < 110:
		print("The gene between 90 and 110 bases long is", data_seq[2])	
	if (data_seq[1].count('a') + data_seq[1].count('t')/len(data_seq[1])) < 0.5 and int(data_seq[3]) > 200:
		print(data_seq[2])
	#if data_seq[2] =~ m/^k/
#print(data_seq)

