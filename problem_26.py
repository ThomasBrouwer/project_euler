from decimal import *
precision = 3000
getcontext().prec = precision

def find_length_recurring_cycle(val):
	# We try sequence lengths, and verify whether it is correct.
	# If not, we try the next length. If it is, we return it.
	value = Decimal(1)/Decimal(val)
	if len(str(value)) >= precision+2:
		for try_length in xrange(1,precision):
			sequence = str(value)[2 : 2+try_length]
			for i in xrange(1,precision/try_length):
				next_sequence = str(value)[2+i*try_length : 2+(i+1)*try_length]
				if sequence != next_sequence:
					break
				# If this is the last iteration, it means this
				# was the correct sequence
				if i == precision/try_length-1:
					return try_length
	else:
		# Not a recurring cycle
		return 0

longest_sequence = 0
value = 0
for val in range(1,1000):
	sequence_length = find_length_recurring_cycle(val)
	if sequence_length > longest_sequence:
		longest_sequence = sequence_length
		value = val

print value