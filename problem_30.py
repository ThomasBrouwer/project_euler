import math

values = []
for i in range(2,1000000+1):
	digits = str(i)
	sum_fourth_powers = sum([math.pow(long(d),5) for d in digits])
	if i == sum_fourth_powers:
		values.append(i)

print values,sum(values)