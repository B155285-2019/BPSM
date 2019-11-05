#!/user/bin/python3

import re
seq = open('long_dna.txt').read().rstrip().upper()
print('The long DNA seq length is ', len(seq))

bpsmI = 'ANT*AAT'
bpsmII = 'GCR[AG]W[AT]*TG'

fragments = re.search('A.TAAT', seq)
seq_cut = re.search('GC[AG][AT]TG', seq)
frag_list = []
if fragments:
	frag1 = seq[0:fragments.start()+3]
	frag2 = seq[fragments.end()-3:]
	print('The length of the first fragment is ', len(frag1))
	print('The length f the second fragment is ', len(frag2))
	frag_list = (frag1, frag2)
for fra in frag_list:
	sec_cut = re.search('GC[AG][AT]TG', fra)
	if sec_cut:
		print('Fragments lengths is ', len(fra[0:sec_cut.start()+4]))
		print('Second fragment length is ', len(fra[sec_cut.end()-2:]))
