import math

def is_prime(n):
	if n == 0 or n == 1:
		return False
	for i in xrange(2,long(math.sqrt(n))+1):
		if n % i == 0:
			return False
	return True

def truncations_left(n):
	string = str(n)
	truncations = []
	for i in xrange(1,len(string)):
		truncations.append(long(string[i:]))
	return truncations

def truncations_right(n):
	string = str(n)
	truncations = []
	for i in xrange(1,len(string)):
		truncations.append(long(string[:i]))
	return truncations

def is_truncatable(n):
	for val in truncations_left(n):
		if not is_prime(val):
			return False
	for val in truncations_right(n):
		if not is_prime(val):
			return False
	return True

truncatable_primes = []
number_truncatable_primes = 0
n = 10
while number_truncatable_primes != 11:
	if is_prime(n):
		if is_truncatable(n):
			truncatable_primes.append(n)
			number_truncatable_primes += 1
	n += 1
print sum(truncatable_primes)