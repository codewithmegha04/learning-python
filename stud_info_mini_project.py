"""name=input("Enter your name:")
formatted_name=name.strip().lower().replace(" ","_")
print(formatted_name)"""

#Student information system mini project

student_name=input("Enter the student name: ")
course=input("Enter the course: ")
marks=float(input("Enter the marks: "))
city=input("Enter the city: ")

print("\n---Student Details---")
print(f"{student_name} is doing {course} in {city} and she has scored {marks} marks.")

print("\n---String Operations----")
print(course.upper())
print(student_name.lower())
print(city.title())

print("\n---Character count----")
print("Number of characters in the student name : ",len(student_name))

#comparison operator
print("\n---Result status----")
print("passed marks: ",marks>35)
print("Scored exactly 100 : ",marks==100)
print("Marks not equal to zero :", marks!=0)

#Assignment operator
bonus_marks=marks
bonus_marks +=10
print("Marks after adding bonus marks:",bonus_marks)

#final formatted output
print("\n---Final Summary----")
print(f"{student_name} from {city} is studying {course} and scored {marks} marks.")













