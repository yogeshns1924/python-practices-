a=1
b=10
for i in range(a,b):
    print(i)
    

import calendar
yy=2022
mm=7
print(calendar.month(yy,mm))



for i in "love":
    if i=="v":
        break
    print(i,end="")



rows=7
for i in range(rows):
    for j in range (rows):
        if i == j or j == rows - 1 - i:
            print("*",end="")
        else:
            print(" ",end="")
    print()  
    
