class Panda:
    def nourrir_animal(self):
        print("Nourrir le panda avec du bambou !")

class Lion:
    def nourrir(self):
        print("Nourrir le lion avec de la viande crue !")

class Zebre:
    def nourriture(self):
        print("Nourrir le zèbre avec du foin bien sec !")

po = Panda()
leo = Lion()
tok = Zebre()

po.nourrir_animal()
leo.nourrir()
tok.nourriture()

zoo = [leo, po, tok]

for animal in zoo:
    pass