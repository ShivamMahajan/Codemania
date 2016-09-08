# Open a file

def append():
	fo = open("employee.txt",'r')
	foo=open("employee2.txt",'r')
	list_employee=[]
	list2_employee=[]
	for line2 in fo:
		list_employee.append(line2)
	print len(list_employee)
	set1=set(list_employee)
	
	for line in foo:
		list2_employee.append(line)
		
	print len(list2_employee)
	set2=set(list2_employee)

	print len(list2_employee)-len(list_employee)
	print set2 - set1
	print len(set2 - set1)
	
	
	for line in foo:
		if line not in list_employee:
			# print line
		# line2=line.split("(")[0]
		# line=line.strip()
		# f1 = open("user.txt", "a")
		# f1.write(line+"\n");

			# if line!=line2:
			f1 = open("user.txt", "a")
			f1.write(line);
			f1.close()     
	fo.close()
	foo.close()
	# lines = open('subtag.xml', 'r').readlines()
	# lines_set = set(lines)
	# out  = open('subtag.xml', 'w')
	# for line in lines_set:
	#     out.write(line)
# n=raw_input("Enter the file Path : ")
append()


