
dna_seq = ("ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT")
compl_seq = dna_seq.replace("A", "t")
compl_seq2 = compl_seq.replace("C", "g")
compl_seq3 = compl_seq2.replace("T", "a")
compl_seq4 = compl_seq3.replace("G", "c")

print ("The original sequence is ", dna_seq)
print ("The complement sequence is ", compl_seq4.upper())
