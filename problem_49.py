import itertools, math

def is_prime(n):
	for i in xrange(2,long(math.sqrt(n))+1):
		if n % i == 0:
			return False
	return True

def find_permutations(val):
	permutations = list(itertools.permutations(str(val)))
	permutation_values = [long("".join(tuple_perm)) for tuple_perm in permutations]
	unique_values = list(set(permutation_values))
	return unique_values

def max(a,b):
	return a if a >= b else b

def min(a,b):
	return a if a <= b else b

result = None
for val in xrange(1000,10000):
	if is_prime(val):
		permutations = find_permutations(val)
		permutations = [permutation for permutation in permutations if permutation > val]
		for permutation in permutations:
			difference = permutation - val
			next_val = permutation + difference
			if next_val in permutations and is_prime(permutation) and is_prime(next_val):
				result = (val,permutation,next_val)
print "".join([str(val) for val in result])