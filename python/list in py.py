# list [] = is collection which is orderd and changeable.
#Allows the duplicate number.#Any type of data can be stored.
#we can modify the list.insert(),append()..ect....

a=[1,2,3,4,5,5]
print(a)

a = [2,3,4]    
a.append(5)   
print(a)


b=[7,8,]
b.extend([8,9,10])   
print(b)


c=[11,12]
c.insert(12,13)
print(c)


d=[14,15,16]
d.remove(15)
print(d)

e=[17,18]
e.pop()
print(e)


f=[19,21,20] 
f.sort()
print(f)

g=[23,24,22]
g.sort(reverse=True)
print(g)


h=[25,26,27]
h.reverse()
print(h)

i=[1,1,2,2,3,3,3,3,4]
print(len(i))

j=[20,30,40]
j[0]=10
print(j)

i=[1,1,2,2,3,3,3,3,4]
print(i.count(1))

