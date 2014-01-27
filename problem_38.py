import math

# Max n is 9
highest_pandigital = 0
for n in range(2,9+1):
	max_number = long(math.pow(10,int(9.0/n)))
	for number in xrange(1,max_number):
		concatenation = ""
		for i in range(1,n+1):
			concatenation += str(i*number)
		if len(concatenation) == 9:
			one_to_nine = ['1','2','3','4','5','6','7','8','9']
			if concatenation == one_to_nine:
				print concatenation 
			if long(concatenation) > highest_pandigital and sorted(concatenation) == one_to_nine:
				highest_pandigital = long(concatenation)
print highest_pandigital			