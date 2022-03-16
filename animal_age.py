from abc import ABC, abstractmethod

class Cat(ABC):
    color = "inconnue"

    def __init__(self, name, size, age):
        self.name = name
        self.size = size
        self.age = age
        print(f"Le chat {name} vient d\'etre crée")

    def grow(self, x):
        print(f"{self.name} a grandi de {x} cm")
        self.size = self.size + x

    def showColor(self):
        print(self.color)

    @abstractmethod
    def calc_real_age(self):
        pass
    
class Korat(Cat):
    color = "bleue"
    def calc_real_age(self):
        return (self.age + 1.1) * 6

class Bombay(Cat):
    color = "noire"
    def calc_real_age(self):
        return self.age * 7

cats = [Korat('Minou', 21, 3), Bombay('Kitty', 64, 5)]
for cat in cats:
    print(f"{cat.name} : {cat.calc_real_age():.1f} ans réels")
