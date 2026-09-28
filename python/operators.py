a=11
b=2
print(a+b) #Arithmetic operators

c=12
d=67
print(c>=d)#comparssion operators

e=5
e-=12  #e=e(5)-12 = -7
print(e) #assigement operators

f=18
g=17
print(f<g and g >15)
print(f<g or g >= 17) #LOgic operators
print(not(g>16))

num1=12
num2=10
print(num1 & num2) #bitwise operaators
print(num1<<num2)
print(~num2)


car=("audi","bmw","tata punch") #membership operators
print("bmw" in car)
print("suvs" not in car)


a=[1,2,3]
b=a
c=[1,2,3]

print(a is b)
print(c is a)  #identity operators
print(b is not c)

