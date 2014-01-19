# In the first circle, 1 is on the diagonal
# In the second circle, every 2nd value is on the diagonal
# In the third circle, every 4th value is on the diagonal. etc
total = 1
i = 1
circle_no = 1 # 1 is the 0th circle
while circle_no <= 500:
	skipfactor = 2*circle_no
	for j in range(0,4):
		i += skipfactor
		total += i
	circle_no += 1

print total