class laptop:
    chargertype="b type"

    def __init__(self):
        self.brand=""
        self.price=23
    def setPrice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)

    @classmethod
    def chargertype(cls):
        cls.chargetype="c type"
        print("charger type changed to c")

    @staticmethod 
    def info():
        print("this is laptop")


dell=laptop()
dell.getprice()

laptop.chargertype()

dell.info()