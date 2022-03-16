class Animal:
    def be_happy(self):
       raise Exception('not implemented')

class Dog(Animal):
    def be_happy(self):
        print("ouaf, ouaf !")

class Cat(Animal):
    def be_happy(self):
        print("miaou, miaou !")

class Canary(Animal):
    def be_happy(self):
        print("coin, coin !")

animal1 = Dog()
animal2 = Cat()
animal3 = Canary()

animal1.be_happy()
animal2.be_happy()
animal3.be_happy()