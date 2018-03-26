def func_multiples(begin,end):
	output_values=[]
	for j in range(begin,end+1):
		if j%7 == 0 and j%5 != 0:
			output_values.append(str(j))
	return ','.join(output_values)

print(func_multiples(3000,5300))
				
