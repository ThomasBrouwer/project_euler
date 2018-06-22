# If fraction n is a/b, then fraction (n+1) is (a+2*b)/(a+b)
larger_numerator = 0
expansions = 1000
fraction_n = (3, 2)
for e in range(1,1000+1):
	a, b = fraction_n
	fraction_n = ((a+2*b), (a+b))
	if len(str(fraction_n[0])) > len(str(fraction_n[1])):
		larger_numerator += 1
print larger_numerator