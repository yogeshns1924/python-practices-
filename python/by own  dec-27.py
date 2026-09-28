def yogesh(a,b):
    for i in range(a,b):
        print(i)
n=int(input("enter the n:"))
m=int(input("enter the m:"))
yogesh(n,m)


class login():
    def __init__(self):
        self.username=""
        self.password=""
    def display(self):
        print("username:",self.username)
        print("password:",self.password)
app=login()      
app.username="yog"
app.password="123"
app.display()


