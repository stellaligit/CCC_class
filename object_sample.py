
class Animal:
    def breath(self):
        print("hu...")

    def eat(self):
        print("yom...")

    def move(self):
        print("thud...")

    def talk(self):
        print("la la la...")

class Mammal(Animal):
    def milk(self):
        print("slurp...")

jack = Animal()
jack.breath()

fred = Animal()
fred.eat()

george = Animal()
george.move()

tom = Mammal()
tom.milk()
tom.move()
tom.eat()