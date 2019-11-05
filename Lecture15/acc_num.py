#!/user/bin/python3

import re

accession = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
for value in accession:
	if re.search('5', value):
		print('5 is found in ', value)
	if re.search('[de]', value):
		print('The letter d or e found in', value)
	if re.search('de', value):
		print('The letters d and e in that order found in', value)
	if re.search('d.e', value):
		print('The letters d and e with a single letter betweeen them found in ', value)
	if re.search('[de].*[ed]', value):
		print('Both letters d and e in any order found in ', value)
	if re.search('^[xy]', value):
		print('Start with x or y in ', value)
	if re.search('^[xy]', value) and re.search('e$', value):	
		print('Start with x or y and end with e in', value)
	if re.search('\d{3}', value):
		print('Contain three or more numbers in ', value)
	if re.search('[arp]d$', value):
		print('end with d followed by either a,r or p in ', value)
