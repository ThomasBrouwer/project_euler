# Helper methods
def check_prime(primes, number):
	for p in primes:
		if number % p == 0:
			return False
	return True

def generate_masks(n_digits):
	''' 1 means we can replace the digit, 0 means keep. 
		The first digit should always be a 0. '''
	if n_digits == 1:
		return [[0]]
	masks_minus_one = generate_masks(n_digits-1)
	masks = []
	for mask in masks_minus_one:
		masks.append(mask+[0]), masks.append(mask+[1])
	return masks

def generate_replacements(n_digits, number, mask):
	# If n_digits > len(number), add 0's at the start
	number_as_list = [v for v in str(number)]
	replacements = []
	for i in range(0,9+1):
		replacement = int(
			''.join([v if m == 0 else str(i) for (v,m) in zip(number_as_list, mask)])
		)
		replacements.append(replacement)
	return replacements


# Variables - skip first digit
primes_so_far = [2,3,5,7]
largest_number, smallest_prime = 1, 2
max_digits = 7


# For every number of digits (2, 3, ...) we do the following:
for n_digits in range(2,max_digits+1):
	print "Trying %s digits." % n_digits

	# First generate all new primes with this number of digits (using the primes so far).
	print "Finding primes."
	new_primes = []
	for number in range(10**(n_digits-1), 10**n_digits):
		if n_digits >= 5 and number % 10**4 == 0:
			print "Still generating primes (%s)." % number
		if check_prime(primes=primes_so_far, number=number):
			new_primes.append(number), primes_so_far.append(number)

	primes_set = set(primes_so_far) # O(1) amortised set membership 

	# Generate all possible masks of digit replacements.
	print "Generating masks."
	masks = generate_masks(n_digits=n_digits)
	masks = masks[1:] # Remove the first mask [0,0,..,0] 

	# Then for each prime and mask, generate all replaced digits and see whether they
	# are also primes. Count the number. 
	print "Generating replaced digits and counting primes."
	for prime in new_primes:
		for mask in masks:
			replacements = generate_replacements(n_digits=n_digits, number=prime, mask=mask)
			
			# Select the replacements that are prime
			primes_in_replacements = [r for r in replacements if r in primes_set]
			number_of_primes = len(primes_in_replacements)
			lowest_prime = min(primes_in_replacements) if len(primes_in_replacements) > 1 else None

			# Check whether we've improved the best find so far
			if number_of_primes > largest_number:
				largest_number = number_of_primes
				smallest_prime = lowest_prime
				print "Found a new best! %s." % (primes_in_replacements)
			elif number_of_primes == largest_number:
				print "Found another with %s digits: %s." % (largest_number, primes_in_replacements)
				smallest_prime = min(smallest_prime, lowest_prime)

	# Stop when we find an eight prime value family.
	if number_of_primes == 8:
		print "Found an eight prime value family. Smallest prime is %s." % smallest_prime

	# Otherwise, try again with more digits
	print "Best prime value family so far: %s digits, smallest prime is %s." % (largest_number, smallest_prime)
