import math

def is_prime(n):
	for i in xrange(2,long(math.sqrt(n))+1):
		if n % i == 0:
			return False
	return True

n = 3
while True:
	if not is_prime(n):
		found_numbers = False
		i = 1
		while 2*i*i < n:
			remainder = n - 2*i*i
			if is_prime(remainder):
				found_numbers = True
				break
			i += 1
		if not found_numbers:
			break
	n += 2
print n