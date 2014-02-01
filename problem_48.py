import math

def keep_last_10_digits(val):
	return long(str(val)[-10:])

total = 0L
for i in xrange(1,1000+1):
	temp = 1L
	for j in xrange(1,i+1):
		temp = keep_last_10_digits(temp*i)
	total = keep_last_10_digits(temp+total)
print total