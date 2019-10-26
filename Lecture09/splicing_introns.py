
dna_seq = ("ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT")
dna_len = len(dna_seq)
first_exon = dna_seq[0:63]
introns = dna_seq[63:90]
sec_exon = dna_seq[90:]
all_seq = first_exon + introns.lower() + sec_exon
exons= first_exon+sec_exon
exons_len = len(exons)
print ("First exon sequence is ", first_exon)
print ("Second exon sequence is ", sec_exon)
print ("Only exons sequence is ", first_exon+sec_exon)
print ("The percentage of the DNA sequence is ", (exons_len/dna_len)*100)
print ("DNA sequence with coding bases is ", all_seq)
