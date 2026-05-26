num = input("Enter the number :")
num = int(num)

if num%2==0:
    print("The number is even")
else:
    print("The number is odd")


indian = ["samosa","daal","naan"]
chinese = ["egg role","pot sticker","fried rice"]
italian = ["pizza","pasta","risotto"]
dish = input("Enter a dish name : ")
if dish in indian:
    print("The dish is in the indian list")
elif dish in chinese:
    print("The dish is in the chinese list")
elif dish in italian:
    print("The dish is in the italian list")
else:
    print("I am not getting which cuisine is this")

fruit_basket = ['apple', 'banana', 'orange', 'mango', 'kiwi']

    # iterating over the index of elements in the list
for i, fruit in enumerate(fruit_basket):
    print(i, ":", fruit)

age = int(input("Enter your age :"))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible enough to vote")

num = int(input("Enter the number :"))
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is negative")
else:
    print("Number is zero")

#Login system:
username=input("Enter your username :")
password=input("Enter your password :")

if username=="admin" and password=="1234":
    print("Login Successful")
else:
    print("Invalid credentials")

#ATM withdrawal:
Balance=5000

amount=int(input("Enter the amount :"))
if amount>Balance:
    print("Insufficient balance")
else:
    print("Transaction successful")


#Discount
amount=int(input("Enter the amount :"))
if amount>5000:
    discount=amount*0.20
elif amount>2000:
    discount=amount*0.10
else:
    discount=0

final_amount=amount-discount

print("Discount",discount)
print("Final Amount",final_amount)
print("No discount",discount)

#Grading System
marks=int(input("Enter your marks :"))

if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Fail")

#Find Largest of 3 Numbers:
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
c = int(input("Enter third number :"))

if a > b and a > c:
     print("Largest number is :",a)
elif b > c:
    print("Largest number is :",b)
else:
    print("Largest number is :",c)

#Salary Bonus System:
salary = int(input("Enter your salary :"))
experience = int(input("Enter your experience :"))

if experience > 10:
    bonus = salary*0.20
elif experience > 5:
    bonus = salary*0.10
else:
    bonus = salary*0.05

print("Bonus:",bonus)

#Hospital Emergency Priority
age=int(input("Enter your age :"))
emergency=(input("emergency case? yes or no :"))
if age>60 or emergency=="yes":
    print("Immediate treatment")
else:
    print("Wait in queue")

#Smart Traffic Signal System
signal=input("Enter your signal :")
if signal=="Red":
    print("Stop")
elif signal=="Yellow":
    print("Ready")
elif signal=="Green":
    print("Go")
else:
    print("Invalid signal")


age=int(input("Enter your age :"))
if age<13:
     print("Kids section")
elif age<=59:
    print("Regular section")
else:
    print("Senior citizen section")
#-----------------------------
food=input("Enter the food item").lower()

if food=="pizza":
    price=200
elif food=="burger":
    price=120
elif food=="pasta:":
    price=100
else:
    price=0
    print("Item not be available")

if price>0:
    print("Total bill",price)
#------------------------------------------
temp=int(input("Enter your temp :"))
if temp>35:
      print("Hot")
elif temp<=20:
      print("Normal")
else:
    print("Cold")
#----------------------------------------
salary=int(input("Enter your salary :"))
age=int(input("Enter your age :"))

if salary>=30000 and age>=21:
    print("Loan approved")
else:
    print("Loan Rejected")
#--------------------------------
password=input("Enter your password :")
if password=="python123":
    print("Login Successful")
else:
    print("Wrong password")

x=10 #global variable
def change():
    global x
    x=20 #local varible
    print(x)

change()
print(x)

boy_name=input("Enter your boy name: ")
boy_age=int(input("Enter your age : "))
girl_name=input("Enter your girl name: ")
girl_age=int(input("Enter your age : "))
Age_Diff=abs(boy_age-girl_age)
#print(boy_name,"Loves",girl_name, "Age diff is :",Age_Diff)
#print(boy_name  + " Loves " +  girl_name + ". Age diff is " + str(Age_Diff))
print(f"{boy_name} Loves {girl_name} .The Age diff is {Age_Diff}")

message="Hi Megha, how are you?"

print(message.strip())

print(message.replace("Megha","Manju"))


#Repition-both are same
greet="Heelo " *4
print(greet)

#OR
greet="Heelo "
print(greet*4)

#String Methods
#-->Upper()
message="Hi Megha am "
print(message.upper())
#-->strip()
print(message.strip()*3)

#replace()
megha="She is a princess"
print(megha.replace("princess","Queen"))

#quotes confusion
name1='Hi, My name is "megha"'
name2="Hi ,my name is 'megha'"
print(name1)
print(name2)

#multiline comment
line=('''Hi , i am megha,
      nd i am working corporate employee and
      am earnign and learning so much..''')
print(line)

#length
print(len(line))

#index
name="Megha Rani"
print(name[6]) #index=position-1, position=index+1

#string slicing
name="Manjunath"
print(name[0:5])
print(name[2:])
print(name[:8])
#if we want to access it from the end:
print(name[-2])
#if we want to skip middle liek tht -[start,end, skip]
print(name[::1])

#escape sequence
m1="hello , \nhow are you, \nwhat u dng"
m2="hello\thow are you, what u dng"
m3="hello\\how are you, what u dng"

print(m1)
print(m2)
print(m3)



































