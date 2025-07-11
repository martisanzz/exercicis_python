#Escriure una classe a Python amb 2 mètodes: get_string() i print_string(). get_string() accepta una cadena ingressada per l'usuari i print_string() imprimeix la cadena en majúscules.

class Cadenaclasse:
    def get_string(self):
        self.cadena = input("Introdueix una paraula: ")

    def print_string(self):
        print(self.cadena.upper())

obj = Cadenaclasse()
obj.get_string()
obj.print_string()
