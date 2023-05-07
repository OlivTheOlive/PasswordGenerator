import string
import random
from PositiveNumberConstructor import PositiveNumber


while True:
    tempLength=input("Enter length wanted for password:  ")
    if not tempLength.isdecimal():
        print("A positive number pls!")
    else:
        length= int(tempLength)
        break


upperCase=input("Uppercase Characters? (y/n):  ")
number=input("Any numbers? (y/n)")
special=input("Any special Characters? (y/n):  ")

lowerCase_char = string.ascii_lowercase

if upperCase == "y":
    upperCase_char = string.ascii_uppercase
    while True:
        num_upperCase = input("How many uppercase characters would you like? ")
        my_instance= PositiveNumber(num_upperCase)
        if num_upperCase > length:
            print("Error: Number of uppercase characters cannot be greater than password length.")
        else:
            break
else: 
    upperCase_char = 0
    num_upperCase = 0

if number == "y":
    number_char = string.digits
    lengthII = length-num_upperCase
    while True:
        num_number= input("How many numbers would you like? ")
        my_instance= PositiveNumber(num_number)
        if num_number > lengthII:
            print("Error: Number of numbers to great. Available space is :"+str(lengthII))
        else:
            break
else:
    number_char = 0
    num_number = 0

if special == "y":
    special_char = string.punctuation
    lengthIII = lengthII - num_number
    while True:
        num_special= input("How many special characters would you like? ")
        my_instance= PositiveNumber(num_special)
        if num_special < lengthIII:
            print("Error: Number of special Chars to great. Available space is :"+str(lengthIII))
        else:
            break
else:
    number_char = 0
    num_special = 0

num_lowerCase= length-num_upperCase-num_number-num_special

password_char = []
for i in range(num_lowerCase):
    password_char.extend(random.choice(lowerCase_char))
for i in range(int(num_upperCase)):
    password_char.extend(random.choice(upperCase_char))
for i in range(int(num_number)):
    password_char.extend(random.choice(str(number_char)))
for i in range(int(num_special)):
    password_char.extend(random.choice(special_char))

random.shuffle(password_char)
password = ''.join(password_char)

# print the password
print("Your password is:", password)
