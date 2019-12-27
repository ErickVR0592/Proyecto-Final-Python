#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:35:19 2019

@author: erickvr
"""

import matplotlib.pyplot as plt
import proyectoGuardar as gu

def graficarDatos():
    abrirArchivo = gu.guardar()
    
    archivo = open(abrirArchivo,'r')
    numeros = archivo.readline()
    archivo.close()
    numeros = numeros.split(',')
    for i in range(len(numeros)):
        numeros[i] = int(numeros[i])
    print(numeros)
    
    plt.plot(numeros)
    plt.xlabel("Numero de dato")
    plt.ylabel("Valor[V]")
    plt.show()