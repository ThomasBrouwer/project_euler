# Helpers
def check_palindrome(v):
	return str(v) == str(v)[::-1]

def reverse_number(v):
	return int(str(v)[::-1])

def is_lychrels(v, max_iterations):
	for i in range(max_iterations):
		v = v + reverse_number(v)
		if check_palindrome(v):
			return False
	return True

# Find Lychrels numbers
max_number = 10000
max_iterations = 50
lychrels = 0
for v in range(max_number+1):
	if is_lychrels(v, max_iterations):
		lychrels += 1
print lychrels