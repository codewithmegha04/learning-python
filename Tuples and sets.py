
#tuple
genders=('male','female','other')
print(type(genders))
print(genders[:2])
print(genders[-0])
print(genders[-1])
print(len(genders))


#one element tuple

one_ele=('4',)
#In tuple, we cannot add item directly so , here is the below things to add
#from tuple to list to tuple
a=(5,)
b=3
c=list(a)
c.append(b)
print(c)

#or--->with a longer list of items to append
a=(6,)
items=['o','r','m','a']

l1=list(a)

for x in items:
    l1.append(x)
print(l1)

#Tuple operation-combining 2 tuples
t1=(1,2)
t2=(3,4)
comb_tuple=t1+t2
print(comb_tuple)

#tuple repetition
tuple=("megha ,")*2
print(tuple)

#membership
tup=(1,2,3,4,"megha")
print(1 in tup)
print("is megha there?","megha" in tup)
print("is megha there?","megha" not in tup)

#tuple methods
gem=(1,5,2,4,2,4,5,6,(1,2))
print(gem)
print(gem.count(2))
print("index",gem.index(6))

#nested tuple
nest=((1,2),(2,3))
print(1 in nest[0])
#Find which inner tuple contains 2
for row in nest:
    if 3 in row:
        print(row)

c=(10,20,30,40,50)
print("first ele",c[0])
print("middle ele",c[2])
print("last ele",c[-1])

numbers = (1,5,2,5,3,5)
print("the num of times 5 appeared is:",numbers.count(5))

fruits = ("apple","banana","orange")
print(fruits.index("banana"))

student = ("Megha",27,"Python")
name,age,country=student
print(name)
print(age)
print(country)

person=("male",20,"SQL")
name,age,course=person
print(name)
print(age)
print(course)


data = (10,20,30,40,50)
print(data[-2])
print(len(data))

numbers = (1,2,3,4,5)
print(sum(numbers))

a = (1,2,3)
b = (4,5,6)
joined_tuple=a+b
print(joined_tuple)

data = (10,20,30,40,50)
"""print(data[1:3])
print(data[1::3])"""
print(data[::-1])

#Sets in python
d={2,6,7,5,6,10}
print(type(d))
#0r
d2=set((1,3,4,6))
print(type(d2))

#set operations
#union
set1={3,4,5}
set2={6,7,4}
union_Set=set1.union(set2)
print(union_Set)
#or
print(set1 | set2)#union
print(set1 & set2)#intersection
print("diff",set1 ^ set2)#symmetric diff
print(set1 - set2)

#set methods
fruits={"banana","mango","apple"}
fruits.add("papaya")
print(fruits)
fruits.remove("papaya")
print(fruits)
fruits.discard("papaya")
fruits.pop()
print(fruits)
fruits.add("papaya")
print(fruits)
fruits.discard("apple")
print(fruits)




#remove duplicates from :
numbers ={1,2,2,3,4,4,5}
print(numbers)
#bt in real world data coms in list to remove dupicates , the time do like below:
numbers = [1,2,2,3,4,4,5]
print(numbers)
unique=set(numbers)
print(unique)

#find common numbers
a = {1,2,3,4}
b = {3,4,5,6}
print(a & b)

#add mango to set
fruits = {"apple","banana"}
fruits.add("mango")
print(fruits)
fruits.remove("banana")
print(fruits)

p={1,2,3}
a=list("megha")
print(a)

y=[1,2]
y.extend([3,4,5])
print(y)
y[0]=6
print(y)
z=[3]

del y[2]
print(y)

"""Homework
Tuple Operations:
"""

#Create a tuple with 5 elements.
element=("sunday","monday","tuesday","wednesday","thursday")
#Try to modify one of the elements. What happens?
#it will no print or ll give error

#Perform slicing on the tuple to extract the second and third elements.
print(element[1:3])

#Concatenate the tuple with another tuple.
t1=(1,2)
t2=(3,4)
print(t1+t2)

#Set Operations:
"""Create two sets: one with your favorite fruits and another with your 
 friend’s favorite fruits."""

my_fvrt_fruits={"kiwi","banana","mango","watermelon"}
my_frnd_fvrt_fruits={"pomo","apple","mango","papaya"}

#Find the union, intersection, and difference between the two sets.
#union
union=my_fvrt_fruits|my_frnd_fvrt_fruits
print(union)
#or
union=my_fvrt_fruits.union(my_frnd_fvrt_fruits)
print("union :",union)

#intersection
inter=my_fvrt_fruits&my_frnd_fvrt_fruits
print("intersection : ",inter)

#diff
diff=my_fvrt_fruits-my_frnd_fvrt_fruits
print("difference : ",diff)

#Add a new fruit to your set.
my_fvrt_fruits.add("guava")
print(my_fvrt_fruits)

#Remove a fruit from your set using both remove() and discard().
# What happens when the fruit doesn’t exist?
my_fvrt_fruits.remove("guava")
print("my",my_fvrt_fruits)
my_fvrt_fruits.discard("guava")
print("my after remove",my_fvrt_fruits)

#Tuple and Set Comparison:
#Create a list of elements and convert it into both a tuple and a set.
l=[1,3,4,5,6,7]
t=tuple(l)
print("tuple",t)
s=set(l)
print("set",s)

#Print both the tuple and the set.
print("tuple",t)
print("set",s)

#Try to add new elements to the tuple and set.
# What differences do you observe?, please answer these
# Set can add
s.add(10)
print(s)

# Tuple cannot add
# t.add(10) -> Error



















