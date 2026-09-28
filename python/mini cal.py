a = int(input("enter the num1:"))
b = int(input("enter the num2:"))
op =input("add/sub/mul/div:")
if(op=="add"):
    print(a+b)
elif(op=="sub"):
    print(a-b)
elif(op=="mul"):
    print(a*b)
elif(op=="div"):
    print(a/b)
else:
    print("invalid op")
