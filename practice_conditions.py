#1.Check Positive, Negative, or Zero
num=int(input("enter the number"))

if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#2.even or odd
number=int(input("Enter the number : "))

if number%2==0:
    print("number is even")
else:
    print("number is odd")

#3.Divisible by 5
num=int(input("Enter the number : "  ))

if num%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")

#4.largest of two numbers-print lagrest number:
a=10
b=20

if a > b :
    print("a is largest")
else:
    print("b is largest")

#5.Voting Eligibility
replaceage=int(input("Enter the age : "))
if replaceage>=18:
       print("ELigible for vote")
else:
       print("Not eligible for vote")


#6.password checker:
correct_password=input("Enter the password : ")
if correct_password=="python123":
    print("Access granted")
else:
    print("Wrong password")

#7.Student Grade System

student_marks=int(input("Enter the marks : "))

if student_marks>=90:
    print('Student Grade is "A" ')
elif student_marks>=75:
    print('Student Grade is "B" ')
elif student_marks>=50:
    print('Student Grade is "C" ')
else:
    print("Student is Failed")

#8.ATM withdrawl

Balance=5000
amount=int(input("Enter your amount : "))

if amount>Balance:
    print("Insufficient balance")
else:
    print("Withdrawal successful")

#Biggest of Three Numbers

a=10
b=50
c=30

if a > b and a > c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
else:
    print("c is largest")

#Simple Login System 
correct_username="megha"
correct_password="python124"

username=input("Enter your username : ")
password=input("Enter your password")

if correct_username==username and correct_password==password:
    print("Login Successful")
elif correct_username==username and correct_password!=password:
    print("Wrong password")
else:
    print("User not Found")

#Write a program to check if someone is eligible for a bus pass. If they are below 5 years, the bus pass is free. 
# If they are 60 years or older, they get a senior citizen discount. Otherwise, they pay the full price.

age=int(input("Enter your age : "))

if age<=5:
    print("The buss pass is free")
elif age>=60:
    print("you will get a senior citizen discount")
else:
    print("You should pay full price")

#
time=int(input("Enter the time in 24 hrs format : "))

if time==8:
    print("Its time for BF")
elif time==13:
    print("It's time for Lunch")
elif time==20:
    print("It's dinner time")
else:
    print("it's not a meal time")

#
age=int(input("Enter you age : "))
if age<18:
   print("You ll get a student membership")
elif age>=60:
    print("You get a senior citizenship membership")
else:
    print("you get regular membership")


balance=6000
correct_pin="python123"

amount=int(input("enter you amount : "))
pin=input("Enter your pin : ")

if pin==correct_pin:
    if amount<=balance:
        print("Withdrawal successful")
    else:
        print("Insufficient balace")
else:
    print("Incorrect pin")

#movie ticket
has_id=input("Do you have any ID proof? (yes/no)")

if has_id=="yes":
    age=int(input("Entre your age"))
    if age>=18:
        print("you will get movie ticket")
    else:
        print("you will not get movie ticker")
else:
    print("user dont have ID proof")

 #Train ticket   
user_has_adhar=input("Do you have your adhar card? (yes/no) : ") 

if user_has_adhar=="yes":
    age=int(input("Enter your age : "))
    if age >= 18:
        print("Your ticker is booked")
    else:
        print("You are underage")
else:
    print("Sorry!, we need your adhar card to book the tickets")

#Online Course Access
email_verified=input("Do your email verification (yes/no): ")

if email_verified=="yes":
    payment_completed=input("is your payment completed? ,please type yes or no") 
    if payment_completed=="yes":
        print("Course unlocked")
    else:
        print("payment pending ")
else:
    print("verify email first")

#Gym Membership
medical_certificate_available=input("Is your medical certificate available? (yes or no)")

if medical_certificate_available=="yes":
    age=int(input("Enter your age"))
    if age>=16:
        print("Membership approved")
    else:
        print("Sorry!, you are underage")
else:
    print("We need your Medical ceritificate for the membership")
    

#ATM machine
atm_pin = "123456"
balance = 5000

ATM = input("Insert your ATM card:(inserted or not) inserted : ")

if ATM=="inserted":
    pin=input("Enter your Pin : ")
    if pin==atm_pin:
        amount=int(input("Enter your amount : "))
        if amount<=balance:
            print("Processing......")
            print("cash withdrawn successfully")
            print("Remaining balance : " ,balance-amount)
        else:
            print("insufficient balance")
    else:
        print("Incorrect pin")
else:
    print("ATM card not inserted")


         









 
