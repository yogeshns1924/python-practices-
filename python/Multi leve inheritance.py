class grandpa():
    def phone(self):
        print("grandpa phone")

class dad(grandpa):
    def money(self):
        print("dad money")

class son(dad):
    def laptop(self):
        print("son laptop")

family=son()
family.laptop()
family.money()
dadhome=dad()
dadhome.phone()
family.phone()

#home=dad()
#home.money()

#gdhome=grandpa()
#gdhome.phone()
