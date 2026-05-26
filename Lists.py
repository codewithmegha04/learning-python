
#lists
food_items=["idli","dosa","rice bath","tomato bath","vang bath",[1,2,3]]
print(food_items)
print(food_items[3])
print(food_items[-1])
print(food_items[-0])

#pop()
food_items.pop()
print(food_items)
food_items.pop(0)
print("pop(0) :",food_items)
#append()
food_items.append("biscuit")
print(food_items)

# Inserts an element at a specific index.
food_items.insert(2,"rice")
print(food_items)

#remove
food_items.remove("rice")
print(food_items)

"""food_items.clear()
print(food_items)"""


#slicing lists
#def-You can extract a portion of a list using slicing.
"""ex:numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [1, 2, 3] (from index 1 to 3)
print(numbers[:4])  # Output: [0, 1, 2, 3] (from start to index 3)
print(numbers[2:])  # Output: [2, 3, 4, 5, 6] (from index 2 to end)
print(numbers[::2])  # Output: [0, 2, 4, 6] (every 2nd element)"""
m=[10,20,30,40,50,60]
#list_name[start:stop:steps]
n=m[0:5]
print(n)
n2=m[2::3]
print(n2)

#List functions and methods
#common functions
"""len(list)"""
student=["pruthvi","megha","manju","amma","pappa","megha"]
print(len(student))
ind=student.index("megha")
print(ind)
#or
print("the index of meghs is :",student.index("megha"))

"""sorted(list)"""
numb=[1,5,3,7,5,4]
print(sorted(numb))

#common methods
#index(element)
student=["pruthvi","megha","manju","amma","pappa","megha"]
print(len(student))
ind=student.index("megha")
print(ind)

#count(element)
print(student.count("megha"))
#or
print("The count is:",student.count("megha"))

#reverse(element)
student.reverse()
print(student)

#sort()-by default it ll be acs order
n=[4,2,16,7]
n.sort()
print(n)
# if we want for desc
n.sort(reverse=True)
print(n)
#or
print(sorted(n,reverse=True))
print(n)

#nested lists
list=[[1,3],[4,5]]
print(list[1][1])
print(list[1])

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][1])
print(matrix[2][2])
print(matrix[0][1])

print(matrix[1])

matrix=[[1,2,3],[4,5,6],[7,8,9]]#doubt ide nodko wht if i want result as 2,6,7

for row in matrix:
    print(row[0])


matrix=[[1,2,3],[4,5,6],[7,8,9]]

rows = len(matrix)
columns = len(matrix[0])

print("Rows =", rows)
print("Columns =", columns)

#1.List Manipulation Exercise:
items=["badam","orange","mango","banana","raisins"]#created list
items.append("pista")#Add a new item to the end of the list
items.insert(1,"makhana")#and another at the second position.
print("adding item: ",items)
items.pop(2)#Remove the third item from the list.
print("popping item: ",items)

#2.Reverse and Sort a List:
numbers=[3,4,2,7,10,12,4,9]
"""numbers.sort()#sorting in ascending by default
print("Sorting in ascending ordr by default : ",numbers)"""#this is fr my ref
numbers.sort(reverse=True)#Sort it in descending order.
print("Sorting in descending order ",numbers)
numbers.reverse()
print("reversing : ",numbers)

matrix=[[1,2,3],[4,5,6]]
total=0
for row in matrix:
     total+= sum(row) # is equal to total=total+sum(row)
print("Total",total)

#Print all elements using nested loop
matrix=[[1,2,3],[4,5,6]]
for row in matrix:
    element: int
    for element in row:
        print(element)

#Find largest number in matrix
matrix = [[2,8,1],[9,3,5]]

largest=matrix[0][0]
for row in matrix:
    for ele in row:
        if ele>largest:
            largest=ele
print("Largest is :",largest)

#Count even numbers in matrix
matrix = [[1,2,3],[4,5,6]]

count=0
for row in matrix:
    for item in row:
        if item%2==0:
            count +=1
print("count",count)

#Find the Largest Number in a List
numbers=[3,7,1,9,4]

largest=numbers[0]
for element in numbers:
    if element>largest:
        largest=element
print("largest is :",largest)

#Find the Smallest Number in a List
numbers=[8,2,10,1,5]

smallest =numbers[0]
for num in numbers:
    if num<smallest:
        smallest=num
print("smallest is :",smallest)

#Count Even and Odd Numbers
numbers=[1,2,3,4,5,6,7,8]

even=0
odd=0

for num in numbers:
    if num%2==0:
        even += 1
    else:
        odd += 1
print("even num is :",even)
print("odd num is :",odd)

#print even and odd numbers: in a separate loop
numbers=[1,2,3,4,5,6,7,8]

print("even numbers: ")
for num in numbers:
    if num%2==0:
     print(num)

print("odd numbers: ")
for num in numbers:
    if num%2!=0:
        print(num)

#print even and odd numbers: in one loop
numbers=[1,2,3,4,5,6,7,8]

even=[]
odd=[]

for num in numbers:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)

print("even numbers are : ",even)
print("odd numbers are : ",odd)
#if i want like this result= 2,4,6,8 then print using *
print("even numbers are : ",*even)
print("odd numbers are : ",*odd)


































