def check_prime(primes, number):
	''' Return True if :number is a prime, using all lower prime values. '''
	for p in primes:
		if number % p == 0:
			return False
	return True

''' Methods for generating primes. '''
def generate_primes(upper):
	''' Check for each number in [0, upper] whether it is a prime by dividing
		it by the primes found so far. Return a list of primes. 
	'''
	primes = []
	for number in range(2,upper+1):
		if check_prime(primes=primes, number=number):
			primes.append(number)
	return primes

def load_primes(upper, fname='primes.txt'):
	''' Read in the precomputed primes from the file. '''
	primes = []
	fin = open(fname, 'r')
	for line in fin:
		new_primes = [int(v) for v in line.split('\t')]
		if new_primes[-1] >= upper:
			new_primes_filtered = [p for p in new_primes if p <= upper]
			primes += new_primes_filtered
			break
		else:
			primes += new_primes
	return primes
	