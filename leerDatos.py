#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:09:56 2019

@author: erickvr
"""
import serial, time 
from tkinter import *

def leerDatos():
    arduino = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(4)

    arduino.write(b'1')
    
    # entrada = int(entrada2.get())
    
    while True:
        try:
            entrada = int(entrada2.get())
            break
        except:
            # print("Introduce un valor valido")
            messagebox.showinfo('Alerta', 'Introduzca un número')
            break
    lecturas = []
    for i in range(entrada):
        lecturas.append(arduino.readline())
        lecturas[i] = lecturas[i].decode('utf-8')
        lecturas[i] = lecturas[i].replace('\r','')
        lecturas[i] = lecturas[i].replace('\n','')
        
    

    arduino.close()
    # print(lecturas)
    return lecturas
    
    
# leerDatos()
