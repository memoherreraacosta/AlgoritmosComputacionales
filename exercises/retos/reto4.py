#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:49:16 2018

@author: memoherrera


Plotear las siguientes graficas

con distintos colores para n de 1 al 100

1. 6n Log(n)
2. 6n 
3. 6n Log(n) +6n
4. n Log(n)

"""
from matplotlib import pyplot
import math as math

def f1(x):
    return 6*x*math.log(x,2)

def f2(x):
    return 6*x

def f3(x):
    return 6*x*math.log(x,2)+6*x

def f4(x):
    return x*math.log(x,2)


#Estilo de la grafica
pyplot.style.use('seaborn')
# Valores del eje X que toma el gráfico.
rangoX = range(1, 15)
# Graficar funciones.
pyplot.plot(rangoX, [f1(i) for i in rangoX], 'blue', label='6n Log(n)')
pyplot.plot(rangoX, [f2(i) for i in rangoX], 'red', label='6n')
pyplot.plot(rangoX, [f3(i) for i in rangoX],'orange', label='6n Log(n) +6n')
pyplot.plot(rangoX, [f4(i) for i in rangoX], 'green', label='n Log(n)')
# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(0, 16)
pyplot.ylim(0, 50)
# Mostrarlo.
pyplot.show()
