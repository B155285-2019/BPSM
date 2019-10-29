#!/usr/bin/python3

def percentage_pr(seq, res):
	res = res.upper()
	res_count = seq.upper().count(res)
	per = res_count/len(seq) * 100
	return round(per, 2)

assert round(percentage_pr("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
#print((percentage_pr("MSRSLLLRFLLFLLLLPPLP", "M")))
#print((percentage_pr("MSRSLLLRFLLFLLLLPPLP", "r"))) 
assert round(percentage_pr("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)

assert round(percentage_pr("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(percentage_pr("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)

