#!/bin/python3

import os

AJ_dna = open("no_h_AJ223353.fasta").read().rstrip("\n").upper()

Aj_ncod = AJ_dna[0:28]
Aj_coding = AJ_dna[28:409]
Aj_ncod2 = AJ_dna[409:]

Aj_ncod1_file = open("AJ223353_ncoding_region_1_length"+str(len(Aj_ncod))+".fasta", "w")
Aj_ncod1_file.write(">AJ223353 nocoding region 1 length"+str(len(Aj_ncod))+'\n')
Aj_ncod1_file.write(Aj_ncod)

AJ_cod = open("AJ223353_coding_region_length"+str(len(Aj_coding))+".fasta", "w")
AJ_cod.write(">AJ223353 coding region length"+str(len(Aj_coding))+"\n")
AJ_cod.write(Aj_coding)

AJ_ncod2_f = open("AJ223353_ncoding_region_2_length"+str(len(Aj_ncod2))+".fasta", "w")
AJ_ncod2_f.write(">AJ223353 noncoding region 2 length"+str(len(Aj_ncod2))+'\n')
AJ_ncod2_f.write(Aj_ncod2)

dna_seq = open("plain_genomic_seq.txt").read().rstrip("\n").upper()

coding_file = open("coding_plain.fasta", "w")
noncod_file = open("noncoding_plain.fasta", "w")

first_part = dna_seq[0:63]
noncoding = dna_seq[63:90]
sec_part = dna_seq[90:]

coding_dna= first_part+sec_part
for base in coding_dna:
	if base not in ["A","C","T","G"]:
		coding_part = coding_dna.replace(base, "")

ncod1_file = open("plain_ncoding_region_length"+str(len(noncoding))+".fasta", "w")
ncod1_file.write(">plain nocoding region length"+str(len(noncoding))+'\n')
ncod1_file.write(noncoding)

cod = open("plain_coding_length"+str(len(coding_part))+".fasta", "w")
cod.write(">plain coding region length"+str(len(coding_part))+"\n")
cod.write(coding_part)
