import math
def no_divisors(val):
	divisors = []
	for i in range(1,int(math.sqrt(val))+1):
		if val % i == 0:
			divisors.append(i)
			divisors.append(val/i)
	return len(divisors)

val = 1
i = 1
while True:
	if no_divisors(val) > 500:
		break
	else:
		i += 1
		val += i
print val