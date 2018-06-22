def digital_sum(v):
	return sum([int(d) for d in str(v)])

max_digital_sum = 0
for a in range(1, 100+1):
	for b in range(1, 100+1):
		d_sum = digital_sum(a**b)
		max_digital_sum = max(d_sum, max_digital_sum)
print max_digital_sum