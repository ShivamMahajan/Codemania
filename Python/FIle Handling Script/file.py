# Open a file

def append():
	a = []
	user=raw_input("Enter user name :")
	a.append(user)
	fo = open('user.txt','r')
	for line in fo:
			for word in a:
				if word in line:
					print "User is already Exist"
					print "Enter a unique user name"
					append()
				else:
					fo = open("user.txt", "a")
					fo.write(user+" ,");
					fo.close()

def read():
	fo = open("user.txt", "r+")
	str=fo.read();
	print str
	fo.close()

def delete():
	if 'users' in open('user.txt','r').read():
		print "Ready to go"
		f = open('user.txt','r')
		a = []
		user=raw_input("Enter user to be deleted: ")+" ,"
		a.append(user)
		lst = []
		for line in f:
			for word in a:
				if word in line:
					line = line.replace(word,'')
				lst.append(line)
		f.close()
		f = open('user.txt','w')
		for line in lst:
			f.write(line)
		f.close()
	else:
		print " Oops ! Sorry"
def input():
	print("Make a choice :\n")
	print("Enter 1 to append :\n")
	print("Enter 2 to read\n")
	print("Enter 3 to delete\n")
	option=int(raw_input("Enter youc choice : "))
	if option==1:
		append()
	elif option==2:
		read()
	elif option==3:
		delete()
	else :
		print "Enter the correct Choice"
		input()

input()