def find_next_prime(values,start,length):
	for v in range(start,length):
		if values[v] != 0:
			return v
	return -1

# We mark values by 0 if they are marked off
max_value = 2000000
primes = [1] # little hack
values = range(0,max_value+1)
values[1] = 0
# Use sieve of Eratosthenes
while True:
	next_prime = find_next_prime(values,primes[-1]+1,max_value)
	if next_prime == -1:
		break
	primes.append(next_prime)

	print next_prime

	i = next_prime
	while i <= max_value:
		values[i] = 0
		i += next_prime
print sum(primes)-1