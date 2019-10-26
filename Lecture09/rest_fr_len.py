
dna_seq = ("ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT")
motif = ("GAATTC")
pos = dna_seq.find(motif)
number_met = dna_seq.count(motif)
dna_len = len(dna_seq)
sec_fr_len = dna_len - (pos + 1 )
print ("The motif starts index number ", pos)
print ("The number of motif we have in our sequence is ", number_met)
print ("Our DNA sequence length is ", dna_len)
print ("Second fragment length ", sec_fr_len)
