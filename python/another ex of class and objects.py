class Teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("Name:",self.name)
        print("Reg No:",self.regno)

t1=Teacher("Yogesh","21")
t2=Teacher("Shinchan","5")

t1.display()
t2.display()




class Cal:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add",self.num1+self.num2)
ob=Cal(2,4)
ob.add()
