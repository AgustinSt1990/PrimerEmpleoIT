# En este segundo ejercicio, tendréis que crear una interfaz sencilla 
# la cual debe de contener una lista de elementos seleccionables, 
# también debe de tener un label con el texto que queráis.

import tkinter as tk
from tkinter import ttk

window = tk.Tk()

canvas = tk.Canvas(window, width=220, height=250)#, bg='lightgray')
canvas.pack(fill='both')

frame = ttk.Frame()
frame.place(relx=0.03, rely=0.05, relwidth=0.94, relheight=0.9)


selected = tk.StringVar()
label = tk.Label(frame, bg='green', fg='yellow',font=('Arial', 12), width=10, textvariable=selected)
label.grid(row=0, column=0, sticky=tk.W)

def print_selected():
    value = listbox.get(listbox.curselection())   
    selected.set(value) 
b1 = tk.Button(frame, text='Selecciona Cripto', width=15, height=2, command=print_selected)
b1.grid(row=2, column=0, sticky=tk.W)

selected_2 = tk.StringVar(frame)
selected_2.set(('BTC', 'ATOM', 'ZIL'))
listbox = tk.Listbox(frame, listvariable=selected_2)
listbox.grid(row=1, column=0, sticky=tk.W)

window.mainloop()