import tkinter
from tkinter import ttk

def mifuncion():
    print("Clickado")

   

# instancio el objeto ventana
window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Diseno de RadioButtons

# variables
seleccionado = tkinter.StringVar()
seleccionado2 = tkinter.StringVar()

# todos los botones que tengan la misma variable solo permite seleccionar uno
r1 = ttk.Radiobutton(window, text='si',     value='1', variable=seleccionado)
r2 = ttk.Radiobutton(window, text='no',     value='2', variable=seleccionado)
r3 = ttk.Radiobutton(window, text='quiza',  value='3', variable=seleccionado)

rs1 = ttk.Radiobutton(window, text='Si2',  value='12', variable=seleccionado2)

# Pocisionamiento de los botones

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)

rs1.grid(column=1, row=0, pady=5, padx=5)

# crear un checkbox

checkbox = ttk.Checkbutton(window, text='Acepto todas las condiciones', variable=seleccionado, command=mifuncion)
checkbox.grid(row=0,column=0)

window.mainloop()