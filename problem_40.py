def champernowne(max_num):
	result = '0.'
	for i in range(1,max_num+1):
		result += str(i)
	return result

result = champernowne(1000000)
print long(result[1+1]) * long(result[1+10]) * long(result[1+100]) \
	* long(result[1+1000]) * long(result[1+10000]) \
	* long(result[1+100000]) * long(result[1+1000000])