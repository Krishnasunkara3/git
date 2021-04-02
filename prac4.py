import re 
#Regular expressions is also known as re
#To check for the pattern matching we go for the regular expressions i.e
#to check wheather the data is available or not,how many times data occoured and to extract the required data.
#to understand regular expressions we require some functions and those functions belong to re module  

#match function
#it compares the pattern at the first index position only.
s = re.match("hi","hi how are you")
print(s)
print(s.group())       #To get the matched pattern
print(s.start())        #To get the starting index
print(s.end())          #To get the ending index

s1 = re.match("hey","you hey its ok")
print(s1)       #None

#search function:
#searches the pattern in entire string untill first occourance.
s2 = re.search("hi","hey, hi how are you")
print(s2)
print(s2.group())       #To get the matched pattern
print(s2.start())        #To get the starting index
print(s2.end())          #To get the ending index

s3 = re.search("hey","i am fine")
print(s3)       #None

s4 = re.search("hi","hey, hi how are you hi")
print(s4)       #it returns only first occourance

#findall function searches the pattern in the string and returns all occourances
s5 = re.findall("hi","hey, hi how are you hi")
print(s5)    #by default it returns the output in list format 
print(tuple(s5))        #typecasted to tuple format
print(set(s5))          #returns output in set format-it prints duplicates for only one time.

#Data in regular expressions
# *: zero or more
# +: one or more
# ?: zero or one
# []: data representation
# [a-z]: all chars from a to z
# [a-f]: characters between a to f
# [abc]: only these three characters
# [^abc]: not abc and remaining all

#data representing by * using match function
result = re.match(r'[a-z]*','ratan hi how are you')
print(result.group())

result = re.match(r'[a-z]+','ratan hi how are you')
print(result.group())

result = re.match(r'[a-z]?','ran hi how are you')
print(result.group())


result = re.match(r'[a-z]*an','ratan hi how are you')
print(result.group())

result = re.match(r'[a-z]+an','ratan hi how are you')
print(result.group())

result = re.match(r'[a-z]?an','ran hi how are you')
print(result.group())

#search method
result = re.search(r'[a-z]*soft','ratan hi how are you and how is durgabcsoft')
print(result.group())

result = re.search(r'[abc]+soft','ratan hi how are you and how is durgabcsoft')
print(result.group())

result = re.search(r'[abc]?soft','ratan hi how are you and how is durgabcsoft')
print(result.group())


