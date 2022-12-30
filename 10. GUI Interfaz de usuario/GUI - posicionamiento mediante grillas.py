import tkinter
from tkinter import ttk

# instancio el objeto ventana
window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)

# Campo usuario
username_label = ttk.Label(window, text="Username:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5) # sticky.w es el posicionamiento del label (west)

username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)

# Campo Password
password_label = ttk.Label(window, text="Password:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5) # sticky.w es el posicionamiento del label (west)

username_entry = ttk.Entry(window, show='*')
username_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

# Boton
login_button = ttk.Button(window, text="Login")
login_button.grid(column=1,row=3, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()