#!/usr/bin/python3

def percentage_pr(seq, res=['A','I','L','G','P','M','F','W','Y','V']):
	total = 0
	for amino in res:
		amino = amino.upper()
		res_count = seq.upper().count(amino)
		per = res_count/len(seq) * 100
		total += per
	return round(total, 2)




assert round(percentage_pr("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
#print((percentage_pr("MSRSLLLRFLLFLLLLPPLP", "M")))
#print((percentage_pr("MSRSLLLRFLLFLLLLPPLP", "r"))) 
assert round(percentage_pr("MSRSLLLRFLLFLLLLPPLP", ["F", "S", "L"])) == 70
assert round(percentage_pr("MSRSLLLRFLLFLLLLPPLP")) == 65
#assert round(percentage_pr("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)

