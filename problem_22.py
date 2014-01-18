letter_to_value = {
	'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 
	'I':9, 'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16, 
	'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,
	'Y':25,'Z':26
}

names = open('names.txt','r').read().split("\",\"")
names[0] = names[0].split("\"")[1]
names[-1] = names[-1].split("\"")[0]
names.sort()

total_score = 0
for i,name in enumerate(names):
	word_score = sum([letter_to_value[char] for char in name])
	index_score = i+1
	total_score += word_score*index_score
print total_score