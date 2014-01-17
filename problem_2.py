prev = 1
current = 2
answer = 0
while current <= 4000000:
	# Every third iteration has num_2 even
	answer += current
	for i in range(0,3):
		current += prev
		prev = current - prev
print answer