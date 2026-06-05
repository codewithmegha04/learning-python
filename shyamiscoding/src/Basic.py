
#sep
"""print(1,2,3,4,5,sep=' , ')#to seperate with comma and we can put anything
#inside the sep
print("2026","05","29",sep="-")
print("2026","05","29",sep="/")
print(1,2,3,4,5,sep='')#no space ll be there"""

#end
"""print("hi, megha",end=" ")
print("Age 27")
print("one",end="-")
print("two",end="-")
print("three",end="-")
print("etc",end="-.......")
"""
#file-Print to a File Instead of Screen
"""with open("log.txt.py", "w") as f:
    print("App started", file=f)
    print("User logged in", file=f)"""

#flush-Force Output Immediately
"""import time
print("Step 1...",flush=True)
time.sleep(1)
print("Step 2...",flush=True)
time.sleep(2)
print("Step 3...",flush=True)
time.sleep(3)
"""

# print("-->"*7,"Hi","<--"*7)
# print("="*50)
# print("-->"*7,"Welcome Megha","<--"*7)
# print("Hi"*3,"Meg"*5,sep="----")
# print("""
#       ===========================
#       "Hi Megha, Welcome to python
#       ===========================
#       """)

#repr()

# string="Hello\tmegha\n"
# print(repr(string))
# #\t=tab,\n=new line

"""print(f"{14000:,}")
print(f"{'python':*^20}")
print(f"{0.8567:.2%}")"""

"""#tokens (lexing step):
import tokenize, io
tokens = tokenize.generate_tokens(io.StringIO("x = 10").readline)
for tok in tokens:
    print(tok)

#AST (parsing step):
import ast
print(ast.dump(ast.parse("x = 10"), indent=2))

#bytecode (compilation step):
import dis
dis.dis("x = 10")"""




