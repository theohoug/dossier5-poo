from unicodedata import name


class User:

    def __init__(self, id, nom, password):
        self.id = id
        self.name = nom
        self.password = password
        print(f"{self.name} vient d\'etre créé.")

    def check_password(self, password):
        return self.password == password
    
    def __str__(self):
        return f"{self.name}"

class Admin(User):
    def manage(self):
        print('Je suis un administrateur')
        
class SuperAdmin(User):
    def manage(self):
        print('Je suis un super administrateur ! ')

user1 = User(1, 'John', '12345')
user2 = Admin(2, 'Faustine', '12345')
user3 = SuperAdmin(3, 'Théo', '12345')
etablissement = "Lycee NDLP"
service = "Service informatique"
liste_divers = [etablissement, service, user1, user2, user3]

for item in liste_divers:
    print(item)
