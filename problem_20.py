def calc_factorial(n):
	total = 1
	while n > 1:
		total *= n
		n -= 1
	return total

factorial_100 = long(calc_factorial(100))
sum_digits = sum([long(digit) for digit in str(factorial_100)])
print sum_digits