#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:09:08 2019

@author: Jorge
"""
import leerDatos as da


def guardar():
    
    lecturas = da.leerDatos()
    
    nombreArchivo = entrada1.get()
    archivo = open(nombreArchivo,'w')
    dato = lecturas[0]
    for i in range(len(lecturas)-1):
        dato = dato + ','+ lecturas[i+1]
    archivo.write(dato)
    archivo.close()
    
    # print(nombreArchivo + " Creado con exito")
    return nombreArchivo

