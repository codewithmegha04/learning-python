#while

is_failed=True
i=1

while is_failed and i<=100:
    print(f"try {i}")
    i=i+1
print("I did my best ")
#or
while is_failed:
    print(f"try {i}")
    i=i+1
    if i>100:
     break
#or what if we only want even numbers to print:
while is_failed:
    if i%2!=0:
       i=i+1
       continue
    print(f"try {i}")
    i=i+1
    if i>100:
     break

i=0

while i<=10:
    x=0
    while x<i:
     print("*",end="-")
     x +=1
    print("")
    i += 1

print("Megha")
print()
print("MAnju")

i=1

while i<5:
    print(i)
    i=i+1
else:
    print("i am running else block : ",i)

age=5

while age<=10:
    print(age)
    age += 1
    if age==8:
        break

i=1

while i<7:
    print(f"{i} is not equal to 5")
    i=i+1
    if i==2:
     print("printing i",i)
     continue
    print("printing i",i)
    i=i+2

#Print numbers from 1 to 10:

i=1
print("Numbers from 1 to 10: ")
while i <=10:
   print(i)
   i += 1


#nd=" " stops Python from going to the next line after printing.
i=2
print("Numbers from 1 to 10:", end="")
while i<=9:
   print(i,end=" ")
   i += 1

#Print numbers from 10 to 1
i=10

while i>=1:
   print(i)
   i -= 1

#Print even numbers from 1 to 20
num=1
while num<20:
    if num%2==0:
     print(num)
    num += 1

#or
num=2
while num<=20:
   print(num)
   num += 2

#Print odd numbers from 1 to 15
num=1
while num<=15:
   if num%2==1:#or num%2!=0
      print(num)
   num += 1
#or
num=1
while num<=15:
   print(num)
   num += 2

#Print multiplication table of a number
num=int(input("Enter number : "))
i=1

while i<=10:
   print(f"{num} x {i} = {num * i}")
   i += 1

#Find sum of numbers from 1 to 100
i=1
total=0

while i<=100:
    total=total+i
    i += 1
    print("Sum of numbers: ",total)

#Count how many digits are in a number
num=int(input("How many digits are in a number?"))

count=0

while num>0:
    num=num//10
    count += 1
print("num of digits",count)

#if i want the numbers to print 1,5,7,9
num=1
while num<=10:
    if num<=1:
        print(num)
        num +=4
    print(num)
    num += 2
#or--print 1 seperately
print(1)

num=5
while num<=10:
    print(num)
    num += 2

#or
num=1
while num<=10:
    print(num)
    if num==1:
        num +=4
    else:
        num +=2

num=int(input("Enter number"))
i=1
while i<=10:
    print(f"{num} x {i}={num*i}")
    i += 1

num=1
count=0 
while num<=10:
    print(num)
    count +=1 
    num += 1

print("Total Numbers = " , count)

num=1
total=0

while num<=10:
    total=total+num
    num += 1
print("Total",total)
#-----------------------
num=3

print("Even" if num%2==0 else "odd")

#Sum only EVEN numbers from 1 to 20
num=2
total=0

while num<=20:
    total=total+num
    num += 2
print(total)

num=1
total=0
while num<=20:
    total=total+num
    print("total",total)
    num += 1
print(total)

num=2
i=1

while i<=10:
    print(f"{num}*{i}={num*i}")
    i += 1

name=input("Enter your name pls : ")

while name == "":
    print("You did not enter your name yet..")
    name=input("Enter your name pls : ")
print(f"Hello, i am {name}")

age = int(input("Enter your age : "))
while age <= 0:
    print("Age can't be zero or negative")
    age = int(input("Enter your age : "))

print(f"You are {age} years old")



#to print from 
for i in range(10,-1,-1):
    print(i)
    

i=0

while i<7:
    print("#"*i)
    i += 1

for i in range(1,12):
    print("*"*i)


i=1

while i<=7:
    print("#",end="")
    j=1
    while j<=7:
        print("#",end="")
        j += 1
    i += 1
    print()

for i in range(7):
    print("#",end=" ")
    for j in range(7):
        print("#",end=" ")
    print()

#multiplication
i=int(input("Enter your num"))
j=1
while j<=10:
    print(f"{i}X{j}={i*j}")
    j += 1

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
        j += 1
#or
num=int(input("Enter number: "))

for j in range(1,11):
    print(f"{num}*{j}={num*j}")
    
frame=['Python', 'Numpy','Pandas','Django', 'Flask']

for i in frame:
    print(i)

bucket_full=False
water_level=0

while not bucket_full:
    water_level += 1
    print(f"puring water {water_level}")
    
    if water_level>5:
        bucket_full=True
#or
keep_pouring=True
water_level=0

while keep_pouring:
    water_level += 1
    print(f"poring {water_level}")

    if water_level>=5:
        keep_pouring = False
 

i=1
print("odd numbers are:")
while i<=20:
    if i%2==1:
        print(i)
    else:
        print(i)
    i +=2

#countdown timer
import time
 
countdown=5

print("countdown started....")
while countdown>=1:
    print(countdown,flush=True)
    time.sleep(1)
    countdown -= 1
print("It's Done !, stop your work")
#-------------------------------------------------
#to check password
secret_password="python123"
entered_password=input("Enter your password : ")

while entered_password != secret_password:
    print("Wrong password,Try again !")
    entered_password=input("Enter your password")
print("Access Granted")
#------------------------------------------------

#to add num
total_sum=0

for i in range(1,6):
    total_sum=total_sum+i
print("Total is : ",total_sum)


arrived=False

while not arrived:
    ask=input("Are we there yet? (yes/no)")

    if ask == "yes":
        print("Hurray!...")
        arrived=True
    else:
        print("hugg...okay")
#or
while True:
    ask=input("Are we there yet? (yes/no)")

    if ask == "yes":
        print("Hurray!...")
        break

for i in range(1,11):
    if i%2 == 0:
        print("Even",i)
#or
for i in range(2,11,2):
    print("Even",i)


secret_number=2

for i in range(1,4):
    guess = int(input("Guess the number : "))
    if guess == secret_number:
        print("You Win!")
        break
print("Game Over!")

for rows in range(1,6):
    for stars in range(1,rows+1):
        print("*",end=" ")
    print()
  
   
for rows in range(1,6):
    for stars in range(rows+1,7):
        print("*",end="")
    print()


num=int(input("Enter num : "))
count=0

while num!=0:
    num=num//10
    count += 1
print("Total",count)








    




    
    



    



    





