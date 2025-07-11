#Anem a crear una classe anomenada Persona. Els seus atributs són: nom, edat i DNI.
#Construeix els següents mètodes per la classe:
#• Un constructor, on les dades poden estar buides.
#• Els setters i getters per a cadascun dels atributs. S'han de validar les entrades de dades.
#• mostrar(): Mostra les dades de la persona.
#• esMayorDeEdad(): Torna un valor lògic indicant si és major d' edat.

class Persona:
    def __init__(self, nom="", edat=0, dni=""):
        self.setnom(nom)
        self.setedat(edat)
        self.setdni(dni)

    def setnom(self, nom):
        if nom:  
            self.nom = nom
        else:
            self.nom = ""

    def setedat(self, edat):
        if edat >= 0:
            self.edat = edat
        else:
            self.edat = 0

    def setdni(self, dni):
        if len(dni) >= 5:  
            self.dni = dni
        else:
            self.dni = ""

    def getnom(self):
        return self.nom

    def getedat(self):
        return self.edat

    def getdni(self):
        return self.dni

    def mostrar(self):
        print("Nom:", self.nom)
        print("Edat:", self.edat)
        print("DNI:", self.dni)

    def esmajordeedat(self):
        return self.edat >= 18

persona1 = Persona("Marti", 19, "11223344A")
persona1.mostrar()
print("Es major d'edat?", persona1.esmajordeedat())
