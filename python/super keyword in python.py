class a():
    def __init__(self):
        print("A")
        
    def display(self):
        print("you in a class")

class b():#a
    def __init__(self):
        super().__init__()
        print("B")
    
    def display(self):
        print("you in b class")

class c(b,a):
    def __init__(self):
        super().__init__()
        print("C")

    def displsy(self):
        print("you in c class")

obj1=c()
obj1.display()

