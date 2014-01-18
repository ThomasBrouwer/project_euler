primes = []
no_primes = 0
i = 1
while True:
	i += 1
	i_is_prime = True
	for prime in primes:
		if i % prime == 0:
			i_is_prime = False
			break
	if i_is_prime:
		primes.append(i)
		no_primes += 1
		if no_primes == 10001:
			break
print primes[-1]