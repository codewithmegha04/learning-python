
#Assignment operator
a=50
a += 60 #short form of a=50+60
print(a)

a1=20
a1 *= 10
print(a1)

s=30
s /=10
print(s)

f=50
f -=15
print(f)

#comparison operator
#==: Checks if two values are equal.
"""a=10
b=20
print(a==b)
#!=: Checks if two values are not equal.
a=10
b=30
print(a!=b)
#>: Checks if the left operand is greater than the right operand.
print(a>b)
#<: Checks if the left operand is less than the right operand.
print(a<b)
#>=: Checks if the left operand is greater than or equal to the right operand.
print(a>=b)
#<=: Checks if the left operand is less than or equal to the right operand.
print(a<=b)"""
"""
#Logical operators
x=12
y=10
z=8
print(x>y and y>x)
print(x>z or z>y)
print(not(y>x))"""

#Membership operators
m="Megha"
m2="MeghaRani"
print(("m" in m) and ("e" in m2))
print(("g" in m) and ("l" in m2))
print(("e" in m) or ("l" in m2))
print(not("g" in m) or not("l" in m2))

#Bitwise operator
"""&: Bitwise AND (sets each bit to 1 if both bits are 1).
|: Bitwise OR (sets each bit to 1 if one of the bits is 1).
^: Bitwise XOR (sets each bit to 1 if only one of the bits is 1).
~: Bitwise NOT (inverts all the bits).
<<: Left shift (shifts bits to the left by a specified number of positions).
>>: Right shift (shifts bits to the right by a specified number of positions)."""
#Examples:
a = 5  # In binary: 101
b = 3  # In binary: 011

# Bitwise AND
print(a & b)  # Output: 1 (binary: 001)

# Bitwise OR
print(a | b)  # Output: 7 (binary: 111)

# Bitwise XOR
print(a ^ b)  # Output: 6 (binary: 110)

# Bitwise NOT
print(~a)  # Output: -6 (inverts all bits)

# Left shift
print(a << 1)  # Output: 10 (binary: 1010)

# Right shift
print(a >> 1)  # Output: 2 (binary: 010)