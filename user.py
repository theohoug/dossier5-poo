class User:

    _age = 0

    def __init__(self, name):
        self.name = name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age > 0 and new_age < 120:
            self._age = new_age
        else:
            print("Veuillez renseigner un âge valide")


user1 = User('John')

#user1.age = 152

user1.age = 34

print(f'{user1.name} a {user1.age} ans')

