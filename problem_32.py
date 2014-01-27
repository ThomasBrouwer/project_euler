import math

def equal_sets(set1,set2):
	if len(set1) != len(set2):
		return False
	equal = True
	for val in set1:
		if val not in set2:
			equal = False
			break
	return equal

def check_pandigital(multiplicand,multiplier,product):
	string = str(multiplicand)+str(multiplier)+str(product)
	if len(string) != 9:
		return False
	letters = set(string)
	return equal_sets(letters,set(['1','2','3','4','5','6','7','8','9']))

# At most the first 5 numbers are before the =
products = []
for multiplicand in xrange(1,9999+1):
	no_digits_multiplicand = int(math.log(multiplicand,10))+1
	no_digits_multiplier = 5 - no_digits_multiplicand
	for multiplier in xrange(1,int(math.pow(10,no_digits_multiplier))):
		if check_pandigital(multiplicand,multiplier,multiplicand*multiplier):
			products.append(multiplicand*multiplier)

print sum(set(products))