def pyramid(rows):
	rows=rows
	for i in range(rows):
		print ' '*(rows-i-1) + '*'*(2*i+1)

pyramid(8)
