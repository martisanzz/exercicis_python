import tkinter as tk
from tkinter import filedialog as fd
import io
import re
import time

def minim(lista):
    return min(lista)

def funcio():
    cadena = e1.get()
    lista = cadena.split(',')
    resultado = [int(numero) for numero in lista]

    minimo = minim(resultado)

    Label1.config(text=f"El mínim és: {minimo}")
    
root = tk.Tk()
amplada = root.winfo_screenwidth() // 2
alçada = root.winfo_screenheight() // 2
root.geometry(f"{amplada}x{alçada}")

c1 =tk.Canvas(root, bg="#FFD700", width=amplada, height=alçada)
c1.place(x=0, y=0)

b1=tk.Button(c1, text="Veure el resultat", command=funcio)
b1.place(x = amplada // 2, y = 8 * alçada // 10, width=100, height=25, anchor = tk.CENTER)

e1=tk.Entry(c1, text="")
e1.place(x = amplada // 2, y = 4 * alçada // 10, width=100, height=25, anchor = tk.CENTER)

Label1 = tk.Label(c1, text = "Posa una llista de numeros separats per comas i donare el minim.", width=0, font = ('Arial', 20), bg = c1.cget('bg'))
Label1.place(x = amplada // 2, y = 6 * alçada // 10, anchor = "center")

root.mainloop()
