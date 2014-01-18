def no_digits(val):
	return len(str(val))

prev_value = long(1)
current_value = long(1)
i = 2

while True:
	current_value += prev_value
	prev_value = current_value - prev_value
	i += 1

	if no_digits(current_value) >= 1000:
		break

print i