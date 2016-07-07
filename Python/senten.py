import re
sentence ='**Initially Planned Hours**: 18.0  6.0 \
	\
	Stage changed \
	\
   **Ending Date**: 2016-06-13 08:01:05 \
   \
   **Stage**: In-Progress  Completed\
\
   **Deadline**: 2015-10-29  2016-06-09\
\
Stage changed\
\
   **Stage**: TODO  In-Progress\
\
   **Starting Date**: 2015-10-28 14:21:24  2016-06-13 07:59:34\
\
Stage changed\
\
   **Stage**: Analysis  TODO\
\
Task Assigned\
\
   **Stage**: Analysis\
\
   **Assigned to**: Abhimanyu Singh\
\
   **Task Summary**: Swipe Implementation\
\
   **Reviewer**: Abhimanyu Singh\
\
   **Kanban State**: In Progress\
\
   **Project**: Training Activities\
\
Task created\
\
   **Stage**: Analysis\
\
   **Assigned to**: Abhimanyu Singh\
\
   **Task Summary**: Swipe Implementation\
\
   **Reviewer**: Abhimanyu Singh\
\
   **Kanban State**: In Progress\
\
   **Project**: Training Activities\
\
\
\
PPPPPPPPPPPPPPPPPP Stage changed\
\
   **Ending Date**: 2016-06-21 06:10:04\
\
   **Stage**: Completed\
\
   **Deadline**: 2015-10-28  2016-06-10\
\
Stage changed\
\
   **Stage**: TODO  In-Progress\
\
   **Starting Date**: 2015-10-28 14:19:02  2016-06-13 07:03:46\
\
Stage changed\
\
   **Stage**: Analysis  TODO\
\
Task Assigned\
\
   **Stage**: Analysis\
\
   **Assigned to**: Bhanu Prakash\
\
   **Task Summary**: google map\
\
   **Reviewer**: Bhanu Prakash\
\
   **Kanban State**: In Progress\
\
   **Project**: Training Activities',
str2="""
My name 

is 

Shivam

Mahajan
"""
print str2.strip()
print re.sub('\s+',' ',str2)

# print sentence.strip() 
# word_list=[]
# for line in sentence:
# 	for word in line.split():
# 		word=word.title()
# 		word_list.append(word)
# print word_list
# print sentence
#sentence = ' '.join(word_list)
# print sentence
# cap_list=[]
# for word in word_list:
# 	word=word.title()
# 	cap_list.append(word)
# print cap_list


