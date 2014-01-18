def collatz_length(val):
	length = 0
	while val != 1:
		if val % 2 == 0:
			val /= 2
		else:
			val = 3 * val + 1
		length += 1
	return length

max_chain = 0
starting_number = 0
for i in xrange(1,1000000):
	length = collatz_length(i)
	if length > max_chain:
		max_chain = length
		starting_number = i
		
print starting_number