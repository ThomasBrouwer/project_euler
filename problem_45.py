import math

def triangle(n):
	return n*(n+1)/2

def pentagonal(n):
	return n*(3*n-1)/2

def check_pentagonal(Pn):
	n = (1.0/3.0 + math.sqrt(1.0/9.0 + 8.0/3.0*Pn))/2.0
	return pentagonal(long(n)) == Pn

def hexagonal(n):
	return n*(2*n-1)

def check_hexagonal(Hn):
	n = 0.25 + math.sqrt(1.0/16.0 + 0.5*Hn)
	return hexagonal(long(n)) == Hn

i = 286
while not check_pentagonal(triangle(i)) or not check_hexagonal(triangle(i)):
	i += 1
print triangle(i)