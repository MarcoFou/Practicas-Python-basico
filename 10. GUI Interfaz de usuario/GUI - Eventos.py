# Un evento es cuando hago algo sobre una ventana (pasar el mouse, click, doble
#doble click, arrastre)

# se usan Callback que es una funcion que recibe un parametro

import tkinter


def saludar(event):
    print('han hecho click en saludar')
    
def saludarDobleClick(event):
    print('han hecho doble click en saludar')
    
def salir(event):
    print('adios')
    window.quit()
    
    
# instancio el objeto ventana
window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Diseno de eventos: 

boton = tkinter.Button(window, text='haz click')
botonSalir = tkinter.Button(window, text='Salir')

boton.pack() # muestra el boton
botonSalir.pack()

# Hago un Binding: es unir un evento a una accion

boton.bind('<Button-1>', saludar) # el evento button-1 es un click
boton.bind('<Double-1>', saludarDobleClick) # el evento button-1 es un click

botonSalir.bind('<Button-1>', salir)

window.mainloop()