#!/usr/bin/python3

def kmer_count(seq, k, minfreq):
	if k > len(seq):
		return print("Sorry, your kmer length is longer than your DNA (" + str(len(seq)) +" bases).")
	if k < 2 or k > 50:
		return print("Sorry, inappropriate kmer length, only 2 to 50 accepted here.")
	seq = seq.upper()
	k_mer = []
	for base in range(len(seq)+1-k):
		slid = seq[base: base+k]
		if seq.count(slid) > minfreq:
			k_mer.append((slid)+": "+str(seq.count(slid)))
			
	print(list(set(k_mer)))
dna = "ATTTTGCATCATG"
print(dna.count("TT")) 
kmer_count("ttagatcctgaacgtgaacgcacggatttagatcctgaacgtgaacgcacggat",2,2)

#counting array issue

