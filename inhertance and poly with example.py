class shape():
    def area(self):
        return 0

class rectangle(shape):
    def area(self):
        length=10
        breath=12
        print(length*breath)
r=rectangle()
r.area()


class person():
    def __init__(self,name): 
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade

    def display(self):
        print(self.name,self.grade)
 
s=student("yog","A")
s.display()

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

    def display(self):
        print(self.name,self.salary,self.department)

m=manager("yog",25000,"IT")
m.display()
