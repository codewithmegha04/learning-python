pro_price=float(input("Enter the product price : "))
quantity=int(input("Enter the quantity : "))

total_amnt = pro_price*quantity
gst=total_amnt*18/100

final_amnt=total_amnt+gst

print(f"Total amount : {total_amnt}")
print(f"GST : {gst}")
print(f"Final amount : {final_amnt}")

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
num3=int(input("Enter the third number : "))

large=max(num1,num2,num3)
total=num1+num2+num3
ave=total/3

print(f"Largest num : {large}")
print(f"Sum of numbers : {total}")
print(f"Average : {ave}")

num=int(input("Enter 3 digit number : "))

digit1=num%10
num=num//10

digit2=num%10
num=num//10

digit3=num%10

total=digit1+digit2+digit3
print(total)

name="Megha"
name="J"+name[0:]
print(name)


t="Megha"
print(t[::-1])

price = 49.99
tax = price * 0.18
total = price + tax

print(f"{'price':<15} :{price:>15}")
t=" Megha is genius "
print(t.find("rani"))
print(t.count("s"))
print(t.replace("Megha","Rani"))

print(t.strip().replace("Megha","RNI"))

age_input=input("Enter your age : ")

if age_input.isdigit():
    age=int(age_input)
    print(f"Your age is {age}")
else:
    print(f"Invalid inout. Please enter a number.")

text="Megha is the best coder"
word=text.split(",")
print("w",word)

data = ["OnePercentDev","Python","Bangalore","Developer"]
parts =" ".join(data)
print(parts) 

parts = ["2026", "03", "19"]
date = "-".join(parts)
print(date) 

numbers = []
for i in range(5):
    numbers.append(str(i))
result = ", ".join(numbers)
print(result)  

greeting = "ನಮಸ್ಕಾರ"  # Kannada
print(greeting)
print(len(greeting))