#Escriu una classe de Python, i defineix dos mètodes que tornin l'àrea del quadrat i el perímetre.

class quadrat:
    def __init__(self, costat):
        self.costat = costat

    def area(self):
        return self.costat * self.costat

    def perimetre(self):
        return 4 * self.costat

quadratareaper = quadrat(5)
print("area del quadrat:", quadratareaper.area())
print("perimetre del quadrat:", quadratareaper.perimetre())
