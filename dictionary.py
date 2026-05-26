
#1. creating dictionary
music={
    "classical":"Hindustani",
    "jazz":"Jazz",
    "western":"Hollywood"
}

#2.Accessign dict elements
print(music["jazz"])
#or
#we can use get(),which is safer because it doesn’t throw an error if the key doesn’t exist.
print(music.get("jaz","not able to find or not found"))
print(music.get("classical"))

#3.Adding and Updating Dictionary Elements
music["instrument"]="flute"
print("Adding dict")
print(music)
#updating
print("updting exsiting dict")
music["classical"]="karnatic"
print(music)
music["kannada"]="sandalwood"
print(music)

#4.Removing Elements from a Dictionary
#pop()
a=music.pop("kannada")
print(a)
#del
del music["jazz"]
print(music)
#clear
music.clear()
print(music)

#5.Dictionary methods
#keys()
print(music.keys())
#values()
print(music.values())
#items
print(music.items())

#update()
hero={
    "kannada":"darshan",
    "tamil":"surya",
    "Hindi":"sharukh"
}
hero.update(music)
print("final",hero)
#or
music.update(hero)
print("final",music)

item1={
    "name":"milk",
    "weight": 1,
     "price":20.50
}
item2={
    "name":"sugar",
    "weight": 3,
     "price":100
}
print(f"{item1} and {item2}")
#or
print(item1,item2)
#or
items=[item1,item2]
print(items)

w1=int(item1['weight'])
w2=int(item2['weight'])
p1=int(item1["price"])
p2=int(item2["price"])

#total sum of weight
print(f"Total sum of weight : {w1+ w2} kg ")
print(f"Total sum of the prices : {p1+p2} Rs")


#Homework
#Basic Dictionary Operations:

#Create a dictionary to store information about 5 cities in Karnataka
#and their famous dishes.

cities={
    "Mysuru":"mysurpak",
    "bengaluru":"bisi bele bath",
    "Managaluru":"neer dose",
    "Dharwad":"peda",
    "udupi":"udupi sambar"
}
print(cities)

#Add a new city and its dish to the dictionary.
cities["Davanagere"]="Ragi mudde"
print(cities)

#Update the dish for Bengaluru.
cities["bengaluru"]="dosa"
print(cities)

#Remove one city from the dictionary.
del cities["bengaluru"]
print(cities)
#or
rem=cities.pop("bengaluru")
print(rem)

#Use the keys() method to print all city names in the dictionary.
print(cities.keys())
#or(asked in interviews like to do below:
for city in cities.keys():
    print("city",city)

#Use the values() method to print all dishes in the dictionary.
print(cities.values())
#or
for dishes in cities.values():
    print("dishes : ",dishes)

#2.Nested Dictionary Practice (Simple for now):
#Create a dictionary to store details of two of your friends, including their names,
# favorite subject, and favorite food.
frnds={
    "frnd1":{
    "name":"Reni",
    "subject":"CS",
    "age":27,
    "food":"veggies"
    }
,

    "frnd2":{
    "name":"Megha",
    "subject":"Python",
    "age":27,
    "food":"rice items"
    }
}



#Access and print the favorite food of one friend.
print("fav food of reni:",frnds["frnd1"]["food"])
print("fvrt food of megha is : ",frnds["frnd2"]["food"])


student={
    "name":"Megha",
    "marks":{
        "pyhton":90,
        "sql":85
    }
    }
print(student["marks"]["sql"])


frnd1={
    "name":"Reni",
    "subject":"CS",
}
frnd2={
    "name":"Megha",
    "subject":"Python",
}
print(frnd1)

friends={
    "friend1":frnd1,
    "friend2":frnd2
}
print("Both frnd r here : ",friends)


print(friends["friend1"]["name"])
print(friends["friend2"]["name"])

#overwrite the value
data={
    "name":"Megha",
    "name":"Ravi"
}

#exercies:
#Student Dictionary
student={
    "name":"Megha",
    "age":27,
    "course":"Python",
    "marks":80
}
print("student name: ",student["name"])
print("student age : ",student["age"])
print("student course : ",student["course"])
print("student marks  : ",student["marks"])
for key, value in student.items():
    print(key,":",value)

#Update marks
print("--updating student marks ----")
student["marks"]=90
print("student marks  : ",student["marks"])

#Remove a Key
print("----removing a key -----")
print(student.pop("age"))

#Print Only Keys
for key in student.keys():
    print(key)

#Print Only Values
for value in student.values():
    print(value)

word="python"
print(word)

















