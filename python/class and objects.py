class goa():
    name=""
    drink=""
    def party(self):
        print("lets party....")
    def beach(self):
        print("enjoy the beach")

yogesh=goa()
madan=goa()

yogesh.name="Yogesh"
madan.name="madan"

yogesh.drink="yes"
madan.drink="no"

print(yogesh.name)
print("drink:",yogesh.drink)
print(madan.name)
print("drink:",madan.drink)

yogesh.party()
madan.beach()
