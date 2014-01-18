number_to_spoken = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}

def len_number(number):
	word = ""
	if number >= 100:
		decimal = number / 100
		number %= 100
		word += number_to_spoken[decimal] + number_to_spoken[100]
		if number > 0:
			word += "and"

	if number >= 20:
		decimal = number / 10
		number %= 10
		word += number_to_spoken[decimal*10]
		if number > 0:
			word += number_to_spoken[number]
	elif number > 0:
		word += number_to_spoken[number]

	print word
	return len(word)

result = 0
for i in range(1,999+1):
	result += len_number(i)
result += len("one") + len("thousand")
print result