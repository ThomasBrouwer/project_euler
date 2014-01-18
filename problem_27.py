import math

def is_prime(val):
	for i in range(2,int(math.sqrt(val))):
		if val % i == 0:
			return False
	return True

def calc_value(a,b,n):
	return n*n+a*n+b

best_a = 0
best_b = 0
longest_sequence_of_primes = 0
for a in xrange(-999,1000):
	for b in xrange(-999,1000):
		n = 0
		while True:
			value = calc_value(a,b,n)
			if value < 0 or not is_prime(value):
				if n+1 > longest_sequence_of_primes:
					longest_sequence_of_primes = n+1
					best_a = a
					best_b = b
				break
			n += 1

print best_a*best_b