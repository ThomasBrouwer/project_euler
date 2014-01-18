def number_permutations(no_values):
	result = 1
	while no_values > 1:
		result *= no_values
		no_values -= 1
	return result

millionth_permutation = []
permutations_left = 1000000-1 #0th is 123456789
values_left = [0,1,2,3,4,5,6,7,8,9]
while values_left:
	for value in values_left:
		no_permutations = number_permutations(len(values_left)-1)
		if no_permutations > permutations_left:
			values_left.remove(value)
			millionth_permutation.append(value)
			break
		else:
			permutations_left -= no_permutations

print "".join([str(val) for val in millionth_permutation])