
#when we create an object, it is a bit of data and a bit of code that allows it to do things
class PartyAnimal:
    #we create a new template, a class
    x = 0
    #we put in a bit of data
    def party(self):
    #here we define the code that will do things with the data inside of the object
        self.x = self.x + 1
        print("So far",self.x)

an = PartyAnimal()
#we actually create an object using the class (the template), and store it in side of an

an.party()
an.party()
an.party()
an.party()

print(dir(an))