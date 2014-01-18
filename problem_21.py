from sets import Set

def find_sum_proper_divisors(n):
	divisors = []
	for i in range(1,n/2+1):
		if n % i == 0:
			divisors.append(i)
	return sum(divisors)

amicable_numbers = Set([])
for n in range(1,10000):
	d_n = find_sum_proper_divisors(n)
	if n != d_n and d_n < 10000 and find_sum_proper_divisors(d_n) == n:
		amicable_numbers.add(n)
		amicable_numbers.add(d_n)
print sum(amicable_numbers)