def add_number(num):
	print num
	def adder(number):
		'adder is a closure'
		print number
		print num+number
		return num + number
	return adder
a_11 = add_number(10)
a_11(21)
a_11(4)