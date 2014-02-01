import math
from collections import deque

def is_prime(n):
	for i in xrange(2,long(math.sqrt(n))+1):
		if n % i == 0:
			return False
	return True

def find_no_consecutive_terms(value,primes,best_so_far):
	selected_primes = deque([])
	sum_selection = 0
	length_selected = 0
	for prime in primes:
		selected_primes.append(prime)
		sum_selection += prime
		length_selected += 1

		# If the selection is greater than value, and we already have less
		# consecutive primes than the best so far, we can stop
		if sum_selection > value and length_selected < best_so_far:
			return -1

		while sum_selection > value:
			removed_prime = selected_primes.popleft()
			sum_selection -= removed_prime
			length_selected -= 1

		if sum_selection == value:
			return len(selected_primes)

	return -1


max_prime = 1000000

longest_sum_prime = 0
no_terms_longest_sum_prime = 0
primes = []

for val in xrange(2,max_prime+1):
	if is_prime(val):
		no_prime_terms = find_no_consecutive_terms(val,primes,no_terms_longest_sum_prime)

		if no_prime_terms > no_terms_longest_sum_prime:
			no_terms_longest_sum_prime = no_prime_terms
			longest_sum_prime = val

		primes.append(val)

print no_terms_longest_sum_prime,longest_sum_prime