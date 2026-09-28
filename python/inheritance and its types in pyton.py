class dad():
    def phone(self):
        print("dad phone")

class mom():
    def money(self):
        print("mom money")

class son(dad,mom):
    def laptop(self):
        print("son laptop")

family=son()
family.laptop()
family.phone()
family.money()

#single inheritance

class frontend():
    def program(self):
        print("HTMLL and CSS")

class backend(frontend):
    def programs(self):
        print("python")
 
fullstack=backend()
fullstack.programs()
fullstack.program()