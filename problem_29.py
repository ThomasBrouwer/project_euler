import math

values = []
for a in range(2,100+1):
	for b in range(2,100+1):
		values.append(math.pow(a,b))

print len(set(values))