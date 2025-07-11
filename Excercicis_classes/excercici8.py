#1 - Crea una classe Cálculos amb un constructor per defecte (sense paràmetres) que permeti realitzar varis càlculs sobre números sencers.
class calculs:
    def __init__(self):
        pass 

#2 - Crea un mètode anomenat factorial() que permeti calcular el factorial d'un sencer.
    def factorial(self, n):
        resultat = 1
        for i in range(1, n + 1):
            resultat *= i
        return resultat

#3 - Crea un mètode anomenat suma() que permeti calcular la suma dels primers n sencers 1 + 2 + 3 + .. + n.
    def suma(self, n):
        resultat = 0
        for i in range(1, n + 1):
            resultat += i
        return resultat

#4 - Crea un mètode anomenat testPrimo() a la classe Cálculos per comprovar si un número és primer. El resultat serà True o False.
    def testPrimo(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

#5 - Crear un mètode anomenat testPrimos() que permeti comprovar si dos números són primers entre sí.
    def testPrimos(self, a, b):
        def mcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        return mcd(a, b) == 1

#6 - Crea un mètode tablaMult() que creï i mostri la taula de multiplicació d'un número sencer donat. A continuació, crea un mètode allTablesMult() per mostrar totes les taules de multiplicació de sencers 1, 2, 3, ..., 9.
    def tablaMult(self, n):
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")

    def allTablesMult(self):
        for n in range(1, 10):
            print(f"\nTaula del {n}:")
            self.tablaMult(n)

#7 - Crea un mètode listDiv() que obtingui tots els divisors d'un sencer donat en una nova llista anomenada Ldiv.
    def listDiv(self, n):
        Ldiv = []
        for i in range(1, n + 1):
            if n % i == 0:
                Ldiv.append(i)
        return Ldiv
# Crear l'objecte
c = calculs()

# Proves
print("Factorial de 5:", c.factorial(5))
print("Suma de 1 a 10:", c.suma(10))
print("És 7 primer?", c.testPrimo(7))
print("Són 8 i 15 primers entre si?", c.testPrimos(8, 15))
print("Divisors de 12:", c.listDiv(12))
print("\nTaula del 6:")
c.tablaMult(6)
print("\nTotes les taules del 1 al 9:")
c.allTablesMult()
