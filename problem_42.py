import string

def calc_triangle(n):
	return n*(n+1)/2

def calc_number(word):
	result = 0
	for char in word:
		result += string.lowercase.index(char.lower())+1
	return result

# First we establish the longest word, and then compute the triangle 4
# numbers until that length * 26
words = open('words.txt','r').read().split("\",\"")
words[0] = words[0].split("\"")[1]
words[-1] = words[-1].split("\"")[0]
max_triangle_value = 26 * max([len(word) for word in words])

triangle_numbers = [1]
n = 2
while triangle_numbers[-1] < max_triangle_value:
	triangle_numbers.append(calc_triangle(n))
	n += 1

no_triangles = 0
for word in words:
	if calc_number(word) in triangle_numbers:
		no_triangles += 1
print no_triangles