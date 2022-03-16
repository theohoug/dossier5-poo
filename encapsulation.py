class Calcul:
    num1 = 10
    def __init__(self, num2):
        self.num2 = num2

    def mtd_instance(self, num3):
        print("Une méthode d'instance.")
        return self.num1 + self.num2 + num3

    @classmethod
    def mtd_class(cls, num3):
        print("Une méthode de classe.")
        return cls.num1 + num3

    @staticmethod
    def mtd_statique(num3):
        print("Une méthode statique")
        return num3

obj1 = Calcul(20)
print(obj1.mtd_instance(3))
print(obj1.mtd_class(3))
print(obj1.mtd_statique(3))

print(Calcul.mtd_class(4))
print(Calcul.mtd_statique(4))