num = 1
for i in range(2,20+1):
	# If it is not divisible, need to multiply num by the 
	# result of the largest number we have already seen that
	# evenly divides i
	if num % i != 0:
		for j in reversed(range(1,i)):
			if i % j == 0:
				multiply_by = i / j
				break
		num *= multiply_by
print num