class Phone:
    storage="256"
    def __init__(self,battery,price):
        self.battery=battery
        self.price=price
        
    def display(self):
        print("Battery:",self.battery)
        print("Price:",self.price)
        print("Storage:",self.storage)
model=Phone("poco","20000")
model.display()
redme=Phone("redme","20000")
redme.display()
realme=Phone("realme","20000")
realme.display()

        
