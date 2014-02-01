import math

def is_prime(n):
	for i in xrange(2,long(math.sqrt(n))+1):
		if n % i == 0:
			return False
	return True

def find_primes(max):
	primes = []
	for i in range(2,max+1):
		if is_prime(i):
			primes.append(i)
	return primes

def no_distinct_prime_factors(n,primes):
	no_prime_factors = 0
	for prime in primes:
		if n % prime == 0:
			no_prime_factors += 1
			while n % prime == 0:
				n /= prime
		if n == 1:
			break

	if n != 1:
		print "Need more primes!"
	return no_prime_factors


max_val = 1000000
primes = find_primes(max_val)

no_distinct_factors = 4
no_consecutives = 4
no_seen = 0
first_result = None
for n in xrange(1,max_val+1):
	if is_prime(n):
		no_seen = 0
	elif no_distinct_prime_factors(n,primes) == no_distinct_factors:
		no_seen += 1
		if no_seen == no_consecutives:
			first_result = n - (no_consecutives - 1)
			break
	else:
		no_seen = 0

print first_result