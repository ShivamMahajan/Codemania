list("hello") <------------->   ['h', 'e', 'l', 'l', 'o']      (list casting of string)
list1=['s','h','i','v','a','m']<-----------> "".join(list1) <------->'shivam'     (string casting of list)

Keywords : list() ,tuple()
list=[]
list1=list1()
len(list)
max(list)
min(list)
sum(list)
random.shuffle(list1)   import random

Indexing and Slicing

print(list1[0]) -------First index
print(list1[-1])------Last index
print(list1[:2]) ------before this -------0,1
print(list1[:-2]) ----------after this--------------- -3,-4,-5.......
print(list1[4:6]) --------------  4,5
print(list1[-4:-1])--------- -4,-3,
It can also be used to reverse a list using [::-1]
[::3] it means 'nothing for the first argument, nothing for the second, and jump by three'. It gets every third item of the sequence sliced
list[1::2]  1,3,5....  each +2

names2 = names1 When assigning names1 to names2, we create a second reference to the same list. Changes to names2 affect names1.

names3 = names1[:]  When assigning the slice of all elements in names1 to names3, we are creating a full copy of names1 which can be modified independently. 

list1 = [1, 3, 2], list1 * 2 =[1, 3, 2, 1, 3, 2]

list1 < list2

Elements are compared one by one.

list1.append(5)  To add a new element to a list list1.append(5) -------Used to add only one elemt at a time

list1.insert(2, 5)   To insert 5 to the third position in list1  (position(index+1),value) -----------don't replace

 list1.remove(“hello”) To remove string “hello” from list1, 

list1.index(5)  --To find out the index position of element in the list1

list1.count(5) ---------To find the occurenece (no of times) of the element in the list 

 list1.reverse()  ------To revers the list

 listExample.extend([34, 5])  ---used to add multiple elements (list of elements at a time)

 list.pop(1) ---removes the element at the position specified in the parameter. (remove the elmenta at index 1 from the list)

 pop() by default will remove the last element.

 "Welcome to Python".split()  <----------> [“Welcome”, “to”, “Python”] 
 		split() function returns the elements in a list. 
 		sting into the list (collectionof elements)

List are immutable

list1 + list2   <--------------------> List concatenation ________New list
	




							Strings
+ operator is concatenation operator. 
"abcd"[2:] cd : Slice operation is performed on string. 




    global a (global variable)
.......................................................................................................................................................
-------------------------------------------------------------------------------------------------------------------------------------------------------
Class is a user defined datatype. 
By default Python shell throws a NoneType object back. 

slicing:

[1:5] 1,2,3,4
[1:]12,3..............
[:3] 0,1,2
[-1] last element
[:-1] -2,-3,-4,-5.......upto the first element


round(...)
    round(number[, ndigits]) -> floating point number
    
    Round a number to a given precision in decimal digits (default 0 digits).
    This always returns a floating point number.  Precision may be negative.

id(...)
    id(object) -> integer
    
    Return the identity of an object.  This is guaranteed to be unique among
    simultaneously existing objects.  (Hint: it's the object's memory address.)

The return type of function id a integer value that is unique.


 x = 13 // 2 (// is integer operation return the quotient)

 x = int(13 / 2)int(..) is a type cast operator.



 Type of Errors :

a) SyntaxError
b) NameError
c) ValueError
d) TypeError


trunc()   :
Syntax   :   math.trunc(x)
This function returns the Real value of x truncated to an Integral 

power operator is x**y

floor division //

the order of precedence in python? (PEDMAS)
i) Parentheses
ii) Exponential
iii) Division
iv) Multiplication
v) Addition
vi) Subtraction

 22 % 3Modulus operator gives remainderSo, 22%3 gives 1 remainder

 You can’t perform mathematical operation on string even if string looks like integers.

 Operators with the same precedence are evaluated in  Left to Right manner?

 regular expressiona : sequence of symbols and characters expressing a string or pattern to be searched for within a longer piece of text.

   re module in Python supports regular expressions 
   re is a part of the standard library and can be imported using: import re.

   
   
   re.compile(str)  creates a pattern object?
   It converts a given string into a pattern object.


    re.match matches a pattern at the start of the string It will look for the pattern at the beginning and return None if it isn’t found

    re.search matches a pattern at any position in the string It will look for the pattern at any position in the string.



    import re
    sentence = 'we are humans'
	matched = re.match(r'(.*) (.*?) (.*)', sentence) / 'How are'
	print(matched.groups())  //Returns tuples (‘we’, ‘are’, ‘humans’) returns all the subgroups that have been matched.
	print(matched.group()) //‘we are humans’ This function returns the entire match.
	print(matched.group(2)) // ‘humans’ This function returns the particular subgroup.


sentence = 'horses are fast'
regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
matched = re.search(regex, sentence)
print(matched.groupdict())

a) {‘animal’: ‘horses’, ‘verb’: ‘are’, ‘adjective’: ‘fast’}
This function returns a dictionary that contains all the mathches.

print(matched.groups())

This function returns all the subgroups that have been matched.
 
print(matched.group(2))
 ‘are’   This function returns the particular subgroup.

 This set of Python Multiple Choice Questions & Answers (MCQs) focuses on “Regular Expressions”.


 Number System 
a) x = 0b101    0b represent binary form
b) x = 0x4f5    0x represent hexadecimal
c) x = 19023    Decimal
d) x = 03964Numbers starting with a 0 are octal numbers


cmp(3, 1)? 
cmp(x, y) returns 1 if x > y, 0 if x == y and -1 if x < y.

 ^ is the Binary XOR operator.

 round(0.5 ) 1.0
 round (-0.5_) -1.0

print r"\nhello"

\nhelloWhen prefixed with the letter ‘r’ or ‘R’ a string literal becomes a raw string and the escape sequences such as \n are not converted. 

:+ is used to concatenate and * is used to multiply strings.

print 'new' 'line'

String literals seperated by white space are allowed. They are concatenated.

\x is an escape sequence that means the following 2 digits are a hexadicmal number encoding a character.
\b 
\0

Jumping index

syntax   [::integer literal]
[::-2]
-1(0) -2 -4
[::2]
0 2 4.......

 s3 = s1.__add__(s2)__add__ is another method that can be used for concatenation.
 example="helloworld"

>>>example[::-1].startswith("d")

TrueStarts with checks if the given string starts with the parameter that is passed.

    >>>example = "helle"

    >>>example.rfind("e")

b) 4returns highest index.

example.find("e")

c) 1returns lowest index .

example.count(l)occurs twice in hello. 

max("what are you")

Explanation:Max returns the character with the highest ascii value.





n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


The first line contains an integer, NN, denoting the size of the array.
The second line contains NN space-separated integers representing the array's elements. 

input()




n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)


The first line contains a single integer, NN. The next NN lines denote the matrix's rows, with each line containing NN space-separated integers describing the columns.

"

Decorators


Decorator is way to dynamically add some new behavior to some objects.
We achieve the same in Python by using closures.
In the example we will create a simple example which will print some statement before and after the execution of a function.

def my_decorator(func):
  def wrapper(*args, **kwargs):
    print("Before call")
    result = func(*args, **kwargs)
    print("After call")
    return result
  return wrapper

@my_decorator
def add(a, b):
  "Our add function"
  print a + b

add(1,3)

Closures

Closures are nothing but functions that are returned by another function.
We use closures to remove code duplication. 
In the following example we create a simple closure for adding numbers.
adder is a closure which adds a given number to a pre-defined one.
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


Generators are used to create iterators,