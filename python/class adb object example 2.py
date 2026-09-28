class laptop:
    def inti (self):
        self.ram=""
        self.procssor=""
    def display(self):
        print("ram:",self.ram)
        print("processor:",self.processor)
hp=laptop()
dell=laptop()

hp.ram="8gb"
hp.processor="i6"

dell.ram="6gb"
dell.processor="i8"

hp.display()
dell.display()
