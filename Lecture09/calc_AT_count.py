
dna_seq=("ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT")
count_T = dna_seq.count("T")
count_A = dna_seq.count("A")
dna_len = len(dna_seq)
AT_count = (count_T + count_A)/dna_len
print ("T count is ", count_T, " and A count is ", count_A)
print ("AT count is ", AT_count)

