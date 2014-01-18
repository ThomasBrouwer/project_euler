def is_abundant(val):
	dividers = []
	for i in range(1,val/2 + 1):
		if val % i == 0:
			dividers.append(i)
	if sum(dividers) > val:
		return True
	else:
		return False

# We keep a list of booleans, one for each value from 1 to 
# 28122. We keep a list of all abundant numbers so far, and
# when we encounter a new one, try each combination with 
# another abundant number already found and mark that number
# as True. Then when we see a value that is marked as False,
# we add it to the non-sum-of-two-abundant-numbers list.
is_sum_two_abundant_numbers = [False] # So the ith value is at index i
for i in range(1,28122+1):
	is_sum_two_abundant_numbers.append(False)

abundant_numbers = []
not_sum_two_abundant_numbers = []

for i in range(1,28122+1):
	if is_sum_two_abundant_numbers[i] == False:
		not_sum_two_abundant_numbers.append(i)

	if is_abundant(i):
		if (i+i) <= 28122:
			is_sum_two_abundant_numbers[i+i] = True
		for abundant_number in abundant_numbers:
			if (i+abundant_number) <= 28122:
				is_sum_two_abundant_numbers[i+abundant_number] = True
		abundant_numbers.append(i)

print sum(not_sum_two_abundant_numbers)