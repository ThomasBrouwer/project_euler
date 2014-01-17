def check_palindrome(val):
	string = str(val)
	for i in range(0,len(string)/2+1):
		if string[i] != string[(-1-i)]:
			return False
	return True

highest = 0
for v1 in xrange(100,1000):
	for v2 in xrange(100,1000):
		if v1*v2 > highest and check_palindrome(v1*v2):
			highest = v1*v2
print highest