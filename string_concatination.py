#Concatinition
#1.

first_name="Megha"
middle_name="SV"
last_name="Rani"
full_name=first_name +" "+ middle_name+" " + last_name
print(full_name)

#1.
name="Megha"
city="Mysore"
print(name +" "+ city)

#2.
food="pizza"
print("I love " +food)

#3
name="Megha"
age=27
print("My name is"+" "+name+" "+"and i am"+" "+str(age)+" "+"years old")
#or
print(f"My name is {name} and i am {age} years old")

#4
"""name=input("Enter your name : ")
print("Hello"+" "+name)"""

#5
company="Google"
role="AI engineer"
print("I want to work at "+company+ " as a "+ role)
#or
print(f"I want to work at {company} as a {role}")

#6
movie = input("Enter movie name: ")
rating = input("Enter rating: ")
print("Movie:"+" "+movie+" "+"and Rating:"+" "+rating)
#or
print(f"Movie: {movie} and Rating: {rating}")

#7
name = input("Enter name: ")
skill = input("Enter skill: ")
experience = input("Enter years of experience: ")
print(f"{name} has {experience} years of experience in {skill}")
#or
print(name + " has " +experience + " years of experience in " + skill)

8-"""What is string concatenation in Python?
String concatenation means joining two or more strings together using the + operator."""

print("Hello" + "World")

"""10-What is the difference between:
print("10" + "20")
--> this will print 1020,Because "10" and "20" are strings, so Python concatenates them.
and
print(10 + 20)
--> Because 10 and 20 are integers, so Python performs mathematical addition."""

"""11-Why do we use str() in concatenation?
We use str() to convert other data types into strings during concatenation.
Example:
age = 27
print("Age is " + str(age))
age is an integer, so Python cannot directly concatenate it with a string.
str(age) converts integer into string."""

#Write a Python program that takes:
"""name
city
from user input and prints:
Megha lives in Mysore"""

name= input("Enter your name: ")
city= input("Enter your city: ")
print(f"{name} lives in {city}")


#Assignments - 1
name=input("Enter your name:")
age=input("Enter your age:")
print(f"Hello, {name}! You are {age} years old")
print("Hello "+ name + "! you are " + age + " years old")
#Output: Hello, Alice! You are 25 years old.

#Assignment - 2
"""sent=input(" Enter a sentence: ")
print(sent.upper())
print(sent.lower())
print(sent.replace(" ","__"))
print((sent.strip() + " ") *3)"""

input=input("Enter a string: ")
text_Without_spaces=input.replace(" ","")
count=int(len(text_Without_spaces))
print("Number of characters excluding spaces : ",count)


#Assignment - 3
input=input("Enter a string: ")
print("number of characters excluding spaces : ",len(input.replace(" ","")))





