# Q1 
x = 65 
y = 53 
if x % 2 != 0 :
   z = not y
else:
    print(x)
    
print(z) 

# answer (False)

# Q1  2)

numbers = [1,2,3,4,5]
print(type(numbers))

def getNumbers():
    return type([1,2,3,4,5])

print(getNumbers())    

#output :    

#<class 'list'>
#<class 'list'>

#Q2 1)

def getNumbersFromFunc():
    x = y = z = 10
    return x , y , z 
    
print(getNumbersFromFunc()) 


#Another Answer

def getNumbersFromFunc():
    x = y = z = 10
    return {'x': x ,'y': y ,'z': z} 
    
print(getNumbersFromFunc())   


#Q2  2)

def sum(x):
    def add(y):
        return x+y
    return add
 
print(sum(12)(5))


#Q3 ) 

# 1
number = input("Enter a number") 

if number == number[::-1]: 

    print("it is a palindrome!") 

else: 

    print("it is not a palindrome!") 


# 2
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []
for numbers in list1:
    if numbers % 3 == 0:
        print(numbers)
        list3.append(numbers)
        print(list3)
for Numbers in list2:
    if Numbers % 2 == 0:
        print(Numbers)
        list3.append(Numbers)
        print(list3)
        


# 3


import math as m


def exponent(base, exp):
    value = m.pow(base , exp)
    print(int(value)) 
    
    
exponent(2.5 , 5)   



# 4 

Mul = int(input("please Enter a number"))

def Multiplication(x):
    for i in range(1,100):
        print(x, "*", i, "=", (x * i))
        

print(Multiplication(Mul))



# 5 

import numpy as np

arr = np.array([15, 25, 35, 45, 55, 65, 75])

for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end = '  ')


# 6

lower_range = int(input("Enter lower range number :"))
upper_range = int(input("Enter higher range number:"))
print("Prime numbers between", lower_range, "and", upper_range, "are:")
for numbers in range(lower_range, upper_range + 1):
   if numbers > 1:
       for i in range(2, numbers):
           if (numbers % i) == 0:
               break
       else:
           print(numbers)



# 7 

for i in range(1,50):
    if i % 3 == 0 and i%5==0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 :
        print("Fizz")
    else:
        print("Not Divisable by any")



# 8 

tup1 = (1,2,3,4,5)
tup2 = tup1

for i in tup1:
    if i not in tup2:
        print("False")
        break
    else:
        print("True")
        break