# Escriure una classe a Python anomenada Circulo que contingui un radi, amb un mètode quetorni l'àrea i un altre que torni el perímetre del cercle.

import math
class cercle:
    def __init__(self, radi):
        self.radi = radi

    def calcular_area(self):
        return math.pi * self.radi ** 2

    def calcular_perimetre(self):
        return 2 * math.pi * self.radi

cercleradi = cercle(4)
print("area del cercle:", cercleradi.calcular_area())
print("perimetre del cercle:", cercleradi.calcular_perimetre())
