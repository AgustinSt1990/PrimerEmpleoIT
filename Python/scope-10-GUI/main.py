# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado
# y que contenga un botón de reinicio para que deje todo como al principio.

# Al principio no tiene que haber una opción seleccionada.

import tkinter as tk
from tkinter import ttk

window = tk.Tk()

canvas = tk.Canvas(window, width=240, height=120)  # , bg='lightgray')
canvas.pack(fill="both")

frame = ttk.Frame()
frame.place(relx=0.03, rely=0.05, relwidth=0.94, relheight=0.9)

selected = tk.StringVar(frame)
r1 = ttk.Radiobutton(frame, text="BTC", value="Bitcoin", variable=selected)
r2 = ttk.Radiobutton(frame, text="ATOM", value="Cosmos", variable=selected)
r3 = ttk.Radiobutton(frame, text="ZIL", value="Zilliqa", variable=selected)

r1.grid(row=0, column=0, columnspan=2, sticky=tk.W)
r2.grid(row=1, column=0, columnspan=2, sticky=tk.W)
r3.grid(row=2, column=0, columnspan=2, sticky=tk.W)

boton_check = ttk.Button(frame, text="Confirmar", command=lambda: print(selected.get()))
boton_check.grid(row=3, column=0)
boton_reset = ttk.Button(frame, text="Reset", command=lambda: selected.set(None))
boton_reset.grid(row=3, column=1)


window.mainloop()
