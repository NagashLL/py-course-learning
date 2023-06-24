class PartyAnimal:
    x = 0
    name = "" #empty string
    def __init__(self,z):
        self.name = z
        print("Constructed a:",self.name)
    
    def party(self):
        self.x = self.x + 1
        print(self.name,"partied",self.x,"many times")

s = PartyAnimal("Sally")
s.party()
s.party()

j = PartyAnimal("John")
j.party()
j.party()
j.party()