import math

def P(n):
	return n*(3*n-1)/2

def check_pentagonal(val):
	# Simple arithmatic shows that n = (1 + sqrt(1+24*val))/6
	# (negative solution left out). If it is a solution, n will
	# be integer.
	n = int((1+math.sqrt(1+24*val))/6)
	if val == P(n):
		return True
	else:
		return False

def find_lowest_D():
	# Simple arithmatic shows that P[n] - P[n-i] = i*(3n-(1+3i)/2) = 3*n*i-(1+3*i*i)/2
	# We just need to find the right n and i
	# We can stop once the difference between two consecutive pentagonals is greater than lowest_D,
	# because that is the lowest D possible for any number from then on
	lowest_D = None
	n = 0
	while True:
		n += 1
		# P(n)-P(n-1) = 3n-2 by arithmatic
		if lowest_D and 3*n - 2 >= lowest_D:
			break

		for i in reversed(xrange(1,n)):
			# We can stop this loop once the distance between P(n) and P(n-i) (i.e. D) is greater than lowest_D
			D = 3*n*i - (i+3*i*i)/2
			if lowest_D and D > lowest_D:
				break
			if check_pentagonal(D):
				Pj = P(n)
				Pk = P(n-i)
				if check_pentagonal(Pj+Pk):
					lowest_D = D
	return lowest_D

print find_lowest_D()