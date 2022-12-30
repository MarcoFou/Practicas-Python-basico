""" el posicionamiento de la geometria place sirve para posicionar de fornma absoluta dentro de una ventana
o relativa dentro del elemento de una ventana con posicionamiento exacto"""
import random
import tkinter
from tkinter import ttk

window = tkinter.Tk()

colors = ['blue', 'yellow', 'red', 'purple', 'green', 'black']

for x in range(0,10):
    color = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors)-1)

    label = tkinter.Label(window, text="etiqueta!", bg=colors[color], fg=colors[color])
    label.place(x=random.randint(0,100), y=random.randint(0,100))

label1 = tkinter.Label(window, text="posicionamiento absoluto", bg='blue', fg='white')
label1.place(x=10, y=50) # 10 pix hacia x y 50  pix hacia y

label2 = tkinter.Label(window, text="Otro mas", bg="red", fg='white')
label2.place(relx=0.10, rely=0.15, relwidth=0.5, anchor="ne") # 10 pix hacia x y 50  pix hacia y





window.mainloop()