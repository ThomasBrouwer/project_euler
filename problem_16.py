import math
result = long(math.pow(2,1000))
total = 0
while result > 0:
	total += result % 10
	result /= 10

print total