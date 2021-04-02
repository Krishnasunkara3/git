
#Finding the square of the number using functions
number = int(input("enter the number:"))            #taking input from the user
def func(num):                                      #defining functiom
    square = num*num                                #logic
    return square                                   #returning the output
result = func(number)                               #function calling     
print(f'The square of the number is:{result}')      #printing the output


#Doubling the data in the list using using functions
range1 = int(input('enter the range:'))             #Taking range from the user
list1 = []                                          #declaring the list to be passed into the function
for i in range(range1):
    list1.append(int(input('enter the value')))     #adding values to the list

def func1(list2):                                   #declaring function
    for val in range(range1):
        list2[val] = list2[val]+list2[val]          #logic part
    return list2                                   #returning the output

result1 = func1(list1)                               #function calling
print(f'Doubled values of given list are: {result1}')       #printing the output


#finding the even numbers in the list using functions
range2 = int(input('enter the range:'))             #Taking range from the user
list3 =[]                                           #declaring the list to be passed into the function
for i in range(range2):
    list3.append(int(input('enter the value')))      #adding values to the list

def func2(list4):                                    #declaring function
    list5 =[]
    for val in list4:
        if val%2==0:                                 #logic part
            list5.append(val)
    return list5                                     #returning the output

result2 = func2(list3)                               #function calling
print(f'even numbers are:{result2}')                 #printing the output    


#finding sum of all the values in the list using functions
range3 = int(input('enter the range:'))             #Taking range from the user
list6 = []                                          #declaring the list to be passed into the function
for i in range(range3):
    list6.append(int(input('enter the value:')))    #adding values to the list

def func3(list7):                                   #function declaration
    sum = 0
    for val in list7:
        sum = sum+val                               #logic part
    return sum                                      #returning output

result3 = func3(list6)                              #function calling
print(f'sum of all the values in a list is:{result3}') #printing output   


