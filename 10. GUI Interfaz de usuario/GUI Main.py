"""GUI: Grafical user interfaces."""

import tkinter
import pprint

#Creo la instancia

window = tkinter.Tk()

print(type(window))
pprint.pprint(dir(window))

# crear un widget

label_saludo = tkinter.Label(window, text='hola!', bg="blue", fg="black")
label_saludo.pack(ipadx=50, ipady=100, fill='x', expand=True)

label_adios = tkinter.Label(window, text="adios", bg="red", fg="white")
label_adios.pack(ipadx=50, ipady=100, side='right')

#Crear una ventana:

window.mainloop()