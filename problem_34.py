def factorial(n):
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result

def sum_factorial_of_digits(n):
	digits = str(n)
	return sum([factorial(long(char)) for char in digits])

curious_numbers = []
for i in xrange(3,factorial(9)*9):
	if i == sum_factorial_of_digits(i):
		curious_numbers.append(i)
print sum(curious_numbers)