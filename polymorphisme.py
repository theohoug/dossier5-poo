from unicodedata import name
from abc import ABC, abstractmethod


class Profile(ABC):

    def __init__(self, id, nom, password):
        self.id = id
        self.name = nom
        self.password = password
        print(f"{self.name} vient d\'etre créé.")

    def check_password(self, password):
        return self.password == password
    
    @abstractmethod
    def get_profile(self):
        pass

class User(Profile):
    def get_profile(self):
        return "user"

class Admin(Profile):
    def manage(self):
        print('Je suis un administrateur')
    def get_profile(self):
        return "admin"
        
class SuperAdmin(Profile):
    def manage(self):
        print('Je suis un super administrateur ! ')
    def get_profile(self):
        return "superadmin"

user1 = User(1, 'John', '12345')
user2 = Admin(2, 'Faustine', '67890')
user3 = SuperAdmin(3, 'Théo', '163758')

users = [user1, user2, user3]
for user in users:
    print(f"{user.name} est {user.get_profile()}")
