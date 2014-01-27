import math

def is_prime(n):
	for i in xrange(2,long(math.sqrt(n))+1):
		if n % i == 0:
			return False
	return True

def all_primes_with_number_digits(n): 
	primes = []
	for i in xrange(long(math.pow(10,n-1)),long(math.pow(10,n))):
		if is_prime(i):
			primes.append(i)
	return primes

def rotate(string,n):
	return string[n:]+string[0:n]

def rotations(number):
	number = str(number)
	rotations = []
	for i in xrange(1,len(number)):
		rotations.append(long(rotate(number,i)))
	return rotations

def is_circular(prime):
	is_circular = True
	for rotation in rotations(prime):
		if not is_prime(rotation):
			return False
	return True

circular_primes = []
for no_digits in range(1,6+1):
	primes = all_primes_with_number_digits(no_digits)
	for prime in primes:
		if is_circular(prime):
			circular_primes.append(prime)

print len(circular_primes)-1 # includes 1