def add(a,b,c=0):
    print(a+b+c)
add(1,2)
add(1,2,3)

class animal():
    def sound(self):
        print("animal make sound")

class dog(animal):
    def sound(self):
        print("dog bark")

class bird(dog):
    def sound(self):
        print("bird sing")

a3=bird()
a3.sound()

a1=dog()
a1.sound() #this called as methodoverwrite it's also  called as poly 
a2=animal()
a2.sound()

class vehicle():
    def start(self):
        print("vehicle started")

class car(vehicle):
    def start(self):
        print("car started")

c=car()
c.start()
#d=vehicle()
#d.start()