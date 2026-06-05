bill=int(input("Enter your bill : "))
people=int(input("Enter the number of people : "))

exact_split=bill/people
rounded_split=bill // people
remainder=bill % people

print(f"Total bill : {bill}\nNumber of people : {people}\nExact split : {exact_split}\nRounded split : {rounded_split}\nRemainder : {remainder}")

