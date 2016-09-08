squares = [1, 4,9, 3,16, 25]
cubes=[1,8,27,64,125]
test=['a','b','c','d','e']
# squares.extend(cubes)
# squares=squares+cubes

# squares.insert(10,0)

# squares.remove(1)

# squares.pop()

# squares.clear()

# print squares.count(1)

# squares.sort(reverse=True)

# print sorted(squares)

# squares.reverse()
# print reversed(squares)

# print squares.copy()
# print squares

# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# print queue
# queue.append("Terry")
# print queue.popleft()
# print queue

# print zip(squares,cubes)
# print zip(squares,cubes,test)

# del squares[]
# print squares

# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# print data[0]
# def ttt(m):
# 	 print m
# 	 v = m[0][0]
# 	 print v
# 	 for row in m:
# 	 	print row
# 	 	for element in row:
# 	 		if v < element: 
# 	 			v = element
# 	 return v

# print(ttt(data[0]))
# data = [[[1, 2], [3, 4]], ]
# data[1][0][0]
# [, [7, 8]]
# [5, 6]


def addItem(listParam):
	listParam.pop()
	listParam += [1]

 

mylist = [1, 2, 3, 4]

addItem(mylist)

print len(mylist)
print mylist