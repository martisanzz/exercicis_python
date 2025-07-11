#Desenvolupar un programa que carregui les dades d'un triangle. Implementar una classe amb els mètodes per inicialitzar els atributs, imprimir el valor del costat amb una mida més gran i el tipus de triangle que és (equilàter, isòsceles o escalè).

class triangle:
    def __init__(self, costat1, costat2, costat3):
        self.c1 = costat1
        self.c2 = costat2
        self.c3 = costat3

    def costat_mes_gran(self):
        costat_maxim = max(self.c1, self.c2, self.c3)
        print("El costat mes gran es:", costat_maxim)

    def tipus_triangle(self):
        if self.c1 == self.c2 == self.c3:
            print("es un triangle equilater")
        elif self.c1 == self.c2 or self.c1 == self.c3 or self.c2 == self.c3:
            print("es un triangle isosceles")
        else:
            print("es un triangle escale")

c1 = float(input("Introdueix el primer costat: "))
c2 = float(input("Introdueix el segon costat: "))
c3 = float(input("Introdueix el tercer costat: "))

t = triangle(c1, c2, c3)
t.costat_mes_gran()
t.tipus_triangle()
