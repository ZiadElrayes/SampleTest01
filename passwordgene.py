import random
from re import S 
import string

passgen = int(input("Enter password length you want !"))


#It gets passwordlength from the user and get 0.3 of the length to be digits
digits = random.choices(string.digits, k=round(passgen*0.3))

#It get 0.6 of the length of password to be letters
letters = random.choices(string.ascii_letters, k=round(passgen*0.6))

#It get 0.1 of the length to be character
charas = random.choices(string.punctuation,k=round(passgen*0.1))

# Pick randoms from letters + digits + characters
sample = random.sample(digits + letters + charas, passgen)

#Joins them together
result = "" .join(sample)
print(result)

