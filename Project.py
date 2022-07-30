
## Question 1 
"""

# Function to check the Vowel
def isitVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']
 
def count_vowels(word):

    counter = 0
    for i in range(len(word)):
 
        # Check for vowel
        if isitVowel(word[i]):
            counter += 1
    return counter
 
word = input('Enter the word')

 
# number of Vowels
print(count_vowels(word))
 

"""


## Question 2
"""
def sum_number(number):
        return number * (number + 1) / 2

number = int(input("Enter the number"))

print("The Sum of Natural Numbers",sum_number(number))

"""


## Question 3

"""

def fibonacci_series(inp):

    if inp <= 1:
       return inp
    else:
       return(fibonacci_series(inp-1) + fibonacci_series(inp-2))


inp = int(input("Enter the number of fibo series you want :"))

if inp <= 0:
    print("Please enter positive integar")
else:
    for i in range(inp):
        print("The series : " , fibonacci_series(i))

"""




## Question 4



"""
sample_dict = {'a':100 , 'b':200 , 'c':300}
value = 200

# the loop will iterate through the the dictionary and print start from 
# the A printing not in the dictionary for the value the b's value is equal so it prints 
for i in sample_dict:
    if sample_dict.get(i) == value:
        print(f"{value}, is in the dictionary")
    else:
        print("Not in the dictionary")

"""      


## Question 5
"""
class Circle:

    def __init__(self,radius,color):
        self.radius = radius
        self.color  = color

    def area(self):
        return 3.14 * pow(self.radius,2)

    def color(self):
        return self.color     

rad = int(input("Enter radius"))
col =  input("Enter the color")

ans = Circle(rad,col)

print("Area of the circle : " , ans.area())
print("color of the circle : " , ans.color())


class cyclinder(Circle):

    def __init__(self):
"""






## Question 6
"""
##import random
##from re import S 
##import string

passgen = int(input("Enter password length you want !"))


#It gets passwordlength from the user and get 0.3 of the length to be digits
Upper = random.choices(string.ascii_uppercase, k=round(passgen*0.4))

#It get 0.6 of the length of password to be letters
Lower = random.choices(string.ascii_lowercase, k=round(passgen*0.3))

#It get 0.1 of the length to be character
numbers = random.randrange(1,10) 


# Pick randoms from letters + digits + characters
sample = random.sample(Upper + Lower + round(numbers*0.3), passgen)

#Joins them together
result = "" .join(sample)
print(result)
"""





