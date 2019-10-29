#!/usr/bin/python3

def base_counter(seq,thresh):
	seq = seq.upper()
	uncertain = ""
	for base in seq:
		if base not in ['A','T','G','C']:
			uncertain += base		
	proprtn = len(uncertain)/len(seq)*100	
#	print(proprtn)
	if proprtn > thresh:
		return True
	else:
		return False

print(base_counter('ACTttttttttttttttGXXXXGGGGTggggggggggTTACGACGANNNNNNNNNN', 30))
