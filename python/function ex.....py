user_name="yog"
user_password="197"

name=input("enter the n:")
password=input("enter the p:")

def yog():
    if(user_name ==name and user_password==password):
        return True
    else:
        return False

print(yog())



def add(n1,n2):
    return n1+n2
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=add(a,b)
e=d*c
print(e)

x = "*"
for i in range(1,5):
    print(x*i)
