import random
from datetime import date

annee = date.today().year

class Personnage:

    compteur = 0
    _matricule = ""

    def __init__(self, nom, force, points):
        Personnage.compteur += 1
        self._matricule = f"{date.today().year}-{Personnage.compteur:03}"
        self.nom = nom
        self.force = random.randint(25, 50)
        self.points = random.randint(95, 250)
        print(f"Le personnage n° {Personnage.compteur} {self.nom} vient d\'être créé.")

        @property
        def matricule(self):
            return self._matricule

    def frapper(self, adversaire):
        print(f"{self.nom} frappe {adversaire.nom} ")        
        if random.randint(1, 5) == 4:
            print(f"{adversaire.nom} a esquivé l'attaque");
        else:
            adversaire.points = adversaire.points - self.force
        print(f'Points de vie de {self.nom} :  "{self.points}"')
        print(f'Points de vie de {adversaire.nom} :  "{adversaire.points}"')
        if adversaire.points <= 0:
            print(f"{adversaire.nom} est mort ")
        print("-------------------------------")

    @property
    def matricule(self):
        return self._matricule

perso1 = Personnage(input("Veuillez saisir le nom du joueur 1 :"), 100, 30)
perso2 = Personnage(input("Veuillez saisir le nom du joueur 2 :"), 100, 30)

while perso1.points > 0 and perso2.points > 0:
    perso1.frapper(perso2)
    if perso1.points > 0 and perso2.points > 0:
        perso2.frapper(perso1)

print(f"Matricule de {perso1.nom} = {perso1.matricule}")
print(f"Matricule de {perso2.nom} = {perso2.matricule}")