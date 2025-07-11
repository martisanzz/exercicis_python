#Escriure una classe a Python anomenada Rectangulo que contingui una base i una altura, i que contingui un mètode que torni l'àrea del rectangle.

class rectangle:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

rect = rectangle(5, 3)
print("L'area del rectangle es:", rect.calcular_area())
