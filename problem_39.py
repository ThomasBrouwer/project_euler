import math

def right_angled(a,b,c):
	return a*a + b*b == c*c


highest_number_solutions = 0
best_p = None
for p in xrange(1,1000):
	number_solutions = 0
	for a in xrange(1,long(float(p)/3)+1):
		for b in xrange(a,long(float(p-a)/2)+1):
			c = p - a - b
			#print p,a,b,c
			if right_angled(a,b,c):
				number_solutions += 1
	if number_solutions > highest_number_solutions:
		best_p = p
		highest_number_solutions = number_solutions
print best_p