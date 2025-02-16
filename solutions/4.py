"""
calculator:
get the user to choose an option from 1 to 4
1 - add
2 - subtract
3 - multiply
4 - divide

get the user to input 2 numbers and then print the answer

hints:
input("message") - gets the user to input something after the message.
if statements
"""

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def divide(a,b):
    return a/b

print("Calculator")
choice = int(input("""1: add\n2: subtract\n3: multiply\n4: divide\nPick an option: """))
while choice < 1 or choice > 4:
    choice = int(input("Invalid choice. Pick an option: "))

if choice == 1:
    x = float(input("enter a number: "))
    y = float(input("enter another number: "))
    print(add(x,y))
elif choice == 2:
    x = float(input("enter a number: "))
    y = float(input("enter another number: "))
    print(sub(x,y))
elif choice == 3:
    x = float(input("enter a number: "))
    y = float(input("enter another number: "))
    print(mult(x,y))
elif choice == 4:
    x = float(input("enter a number: "))
    y = float(input("enter another number: "))
    print(divide(x,y))
else:
    print("Invalid choice")