import math

def is_prime(n):
	for i in xrange(2,long(math.sqrt(n))):
		if n % i == 0:
			return False
	return True

def is_pandigital(num):
	return sorted(str(num)) == [str(val) for val in range(1,len(str(num))+1)]

# At most 9-digit pandigital, so look for that
highest_pandigital = 0
for no_digits in xrange(1,7+1):
	for i in reversed(xrange(long(math.pow(10,no_digits-1)),long(math.pow(10,no_digits)))):
		if is_prime(i) and is_pandigital(i):
			highest_pandigital = i
			break # We check in reversed order, so once we find a number,
				  # it must be the highest with that no. of digits
print highest_pandigital