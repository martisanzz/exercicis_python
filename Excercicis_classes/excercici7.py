#Enunciat: classe Compte Bancari

class CompteBancari:
    def __init__(self, nom, cognom, numerocompte, tipuscompte):
        self.nom = nom
        self.cognom = cognom
        self.numerocompte = numerocompte
        self.tipuscompte = tipuscompte
        self.saldo = 0.0

    def mostrardades(self):
        print("Titular:", self.nom, self.cognom)
        print("Numero de compte:", self.numerocompte)
        print("Tipus de compte:", self.tipuscompte)
        print("Saldo actual:", self.saldo)

    def consultarsaldo(self):
        return self.saldo

    def consignar(self, quantitat):
        if quantitat > 0:
            self.saldo += quantitat
            print(f"Has ingressat {quantitat}€. Nou saldo: {self.saldo}€")
        else:
            print("La quantitat a ingressar ha de ser positiva.")

    def retirar(self, quantitat):
        if quantitat > self.saldo:
            print("No es pot retirar, Saldo insuficient.")
        elif quantitat <= 0:
            print("La quantitat a retirar ha de ser positiva.")
        else:
            self.saldo -= quantitat
            print(f"Has retirat {quantitat}€. Nou saldo: {self.saldo}€")

compte = CompteBancari("Marti", "Sanz", "ES1234567890", "Estalvis")
compte.mostrardades()
compte.consignar(200)
compte.retirar(50)
compte.retirar(300)  
print("Saldo final:", compte.consultarsaldo(), "€")
