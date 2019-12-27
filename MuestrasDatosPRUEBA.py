# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:09:12 2019

@author: Hilda
"""

import leerDatos as da
import proyectoGuardar as gu
import graficarDatos as gra
from tkinter import *


ventana = Tk()
ventana.title("Comunicación con Arduino")

frame = Frame(ventana)
frame.pack(padx=20,pady=20)


etiqueta1= Label(frame, text = "Nombre del archivo")
etiqueta1.pack()

gu.entrada1 = Entry(frame)
gu.entrada1.pack()

etiqueta2= Label(frame, text = "Número de muestras")
etiqueta2.pack()

da.entrada2 = Entry(frame)
da.entrada2.pack()

etiqueta3= Label(frame, text = " ")
etiqueta3.pack()

leer = Button(frame, text = "Leer",command = da.leerDatos)
leer.pack(side = LEFT)

graficar = Button(frame, text = "Graficar",command = gra.graficarDatos)
graficar.pack(side = RIGHT)

guardar = Button(frame, text = "Guardar",command = gu.guardar)
guardar.pack()

ventana.mainloop()