"""exp=[1200,2000,3500,4000,4500]
total=0
for item in exp:
    total=item+total
print(total)
--------------------------------
exp=[1200,2000,3500,4000,4500]
total=0
for i in range(len(exp)):
    print('Month :',i+1, 'Expense :',exp[i])
    total=total+exp[i]
print('Total :',total)
---------------------------------
key_location="chair"
location=["garage","living room","chair","closet"]
for item in location:
    if item==key_location:
        print("Item found in ",item)
        break
    else:
        print("Item not found in",item)

for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)"""


#multiplication in for loop
"""for i in range(2,6):
    for l in range(1,11):
    
     print(f"{i}*{l}={i*l}")
print("The tables from 2 to 5 is :")"""

"""name = ["Megha", "Manju", "chandrakala", "Veerupakshappa"]
for i in name:
    print(i)"""


"""color=["oil red","pink","black","white"]
for c in color:
    if c=="black":
        print("The colour is found",c)
        break
    print(c)
"""

num=int(input("Enter number : "))
total=1
i=1

while i<=num:
    total=total*i
    i += 1
print("Total",total)






