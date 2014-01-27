def check_curious(numerator,denominator):
	str_num = str(numerator)
	str_den = str(denominator)
	if str_num[1] == '0' and str_num[1] == '0':
		return False
	else:
		for char in set(str_num):
			if char in set(str_den):
				char_removed_num = list(str_num)
				char_removed_num.pop(str_num.index(char))
				char_removed_den = list(str_den)
				char_removed_den.pop(str_den.index(char))
				if long(char_removed_num[0]) != 0 and long(char_removed_den[0]) != 0 and \
				float(numerator)/float(denominator) == float(char_removed_num[0])/float(char_removed_den[0]):
					return True
		return False

def multiply_fractions(fractions):
	numerator = 1
	denominator = 1
	for num,den in fractions:
		numerator *= num
		denominator *= den
	return (numerator,denominator)

def find_lowest_common_terms(numerator,denominator):
	i = 2
	while True:
		if i > numerator or i > denominator:
			break
		if numerator % i == 0 and denominator % i == 0:
			numerator /= i
			denominator /= i
			i = 2
		else:
			i += 1
	return (numerator,denominator)

curious_fractions = []
for denominator in xrange(10,99):
	for numerator in xrange(10,denominator):
		if check_curious(numerator,denominator):
			curious_fractions.append((numerator,denominator))

mult_fractions = multiply_fractions(curious_fractions)
mult_fractions = find_lowest_common_terms(mult_fractions[0],mult_fractions[1])
print mult_fractions[1]