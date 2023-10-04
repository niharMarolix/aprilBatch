class Animal: # parent class
    def sleep(self):
        return("I can sleep")
    def walk(self):
        return("I can walk")
    def fight(self):
        return("i fought with big show")
    def eat(self):
        return(" I eat secy girrafe")

class Cheetah(Animal): # child class
    def eat(self):
        return(" I eat secy deers")
    def walk(self):
        return("I run faster than a moped")

chi = Cheetah()
c = (chi.eat())
print(c)