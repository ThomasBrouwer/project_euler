primes = []
val = 600851475143
while True:
	# Keep finding a prime (first divider) and dividing val
	# by that until the only divider is val itself.
	# That value is the largest prime.
	prev = val
	for i in xrange(2,val):
		if val % i == 0:
			val /= i
			break
	if prev == val:
		break
print val