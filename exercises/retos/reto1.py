#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 11:35:07 2018

@author: GuillermoHerrera & EkatherinaChumakova

Se tienen un arreglo A y un numero N objetivo, el
objetivo es encontrar un numero de convinaciones de 
subconjuntos diferentes que den la suma N 

Ej. A = [1,2,3,4]  
    N = 7
    
Respuesta = 2 
        {3,4}
        {1,2,4}
    
"""
def conjuntosValidos():
    arreglo = input("Introducir arreglo: ")
    n = int(input("Introducir n: "))
    arreglosEncontrados = []
    arreglo = arreglo.split(" ")
    arreglo = list(map(int, arreglo))
    sets = []
    for i in range(1 << len(arreglo)):
        subset = [arreglo[bit] for bit in range(len(arreglo)) if (i & (1 << bit) > 0)]
        aux = 0
        for i in subset:
            aux = aux + i
        if aux == n:
            print(subset)

conjuntosValidos()
