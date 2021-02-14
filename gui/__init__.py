from tkinter import *
from model.User import User
root = Tk()
root.title("Calories Calculator")

# Interfaz Definición usuario
e0 = Entry(root, width=25, borderwidth=5)


e1 = Entry(root, width=25, borderwidth=5)
e2 = Entry(root, width=25, borderwidth=5)
e3 = Entry(root, width=25, borderwidth=5)
e4 = Entry(root, width=25, borderwidth=5)

l0 = Label(root, text="Edad")
l1 = Label(root, text="Peso")
l2 = Label(root, text="Altura (cm)")
l3 = Label(root, text="Sexo (M/F)")
l4 = Label(root, text="Nivel Intensidad")

# e0.get()
# e1.pack()
# e2.pack()
# e3.pack()
# e4.pack()


# Funciones de los botones
def accion_calcular():
    e0.pack()
    edad = e0.get()

    print("hola" + edad)


# Botones
boton_borrar = Button(root, text="Borrar")
boton_calcular = Button(root, text="Calcular", command=lambda: accion_calcular())


# GRID
l0.grid(row=0, column=0)
l1.grid(row=1, column=0)
l2.grid(row=2, column=0)
l3.grid(row=3, column=0)
l4.grid(row=4, column=0)

e0.grid(row=0, column=1)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)

boton_borrar.grid(row=5, column=0)
boton_calcular.grid(row=5, column=1)


root.mainloop()
