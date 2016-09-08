# Open a file

def append(file_name):
	fo = open(file_name,'r')
	for line in fo:
		for word in line.split():
			# print re.match('', line)
			if '=' in word:
				word=word.split("=")[0]
				print word
				f1 = open("subtag.xml", "a")
				f1.write(word+" \n");
	f1.close()     
	fo.close()
	lines = open('subtag.xml', 'r').readlines()
	lines_set = set(lines)
	out  = open('subtag.xml', 'w')
	for line in lines_set:
	    out.write(line)
n=raw_input("Enter the file Path : ")
append(n)


