def numbers_without(numbers,without):
	return list(set(numbers) - set(without))

# Given a multiple and d2,d3, it gives values d1 s.t. d1d2d3 % multiple == 0
def find_digit_for_multiples_of(multiple,d2,d3):
	results = []
	for d1 in numbers_without(range(0,10),[d2,d3]):
		if long(str(d1)+str(d2)+str(d3)) % multiple == 0:
			results.append(d1)
	return results

pandigitals_with_p = []
for d10 in xrange(0,10):
	for d9 in numbers_without(range(0,10),[d10]):
		for d8 in numbers_without(find_digit_for_multiples_of(17,d9,d10),[d9,d10]):
			for d7 in numbers_without(find_digit_for_multiples_of(13,d8,d9),[d8,d9,d10]):
				for d6 in numbers_without(find_digit_for_multiples_of(11,d7,d8),[d7,d8,d9,d10]):
					for d5 in numbers_without(find_digit_for_multiples_of(7,d6,d7),[d6,d7,d8,d9,d10]):
						for d4 in numbers_without(find_digit_for_multiples_of(5,d5,d6),[d5,d6,d7,d8,d9,d10]):
							for d3 in numbers_without(find_digit_for_multiples_of(3,d4,d5),[d4,d5,d6,d7,d8,d9,d10]):
								for d2 in numbers_without(find_digit_for_multiples_of(2,d3,d4),[d3,d4,d5,d6,d7,d8,d9,d10]):
									for d1 in numbers_without(range(0,10),[d2,d3,d4,d5,d6,d7,d8,d9,d10]):
										pandigitals_with_p.append(long(str(d1)+str(d2)+str(d3)+str(d4)+str(d5)+str(d6)+str(d7)+str(d8)+str(d9)+str(d10)))
print sum(pandigitals_with_p)