def check_palindrome_decimal(n):
	string = str(n)
	for index in range(0,len(string)/2):
		if string[index] != string[-1-index]:
			return False
	return True

def check_palindrome_binary(n):
	binary = bin(n)[2:] # get rid of the '0b'
	for index in range(0,len(binary)/2):
		if binary[index] != binary[-1-index]:
			return False
	return True

palindromic_numbers = []
for n in xrange(1,1000000):
	if check_palindrome_binary(n) and check_palindrome_decimal(n):
		palindromic_numbers.append(n)
print sum(palindromic_numbers)