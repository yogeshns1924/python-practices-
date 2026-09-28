class student:                     # class is blueprint for crating objects ex.. (design of car is class and the actual car is object)
    def __init__(self):
        self.name="yogesh"
        self.regno="42111507" 
    def display(self):                 # self is refers to the correct object of the class
        print("name:",self.name)
        print("regno:",self.regno)

s1=student()                # object is an instance of a class
s2=student()

s1.name="yog"
s1.regno="3"

s2.name="abc"
s2.regno="5"

#print(s1.name)
#print(s1.regno)
s1.display()
s2.display()


class fruit:
    def __init__(self,yo):
        self.color=yo
apple=fruit("black")
print(apple.color)


class king:
    def __inti__(self,ck):
        self.bat=ck
c=king("virat kohli")
print(c.bat)