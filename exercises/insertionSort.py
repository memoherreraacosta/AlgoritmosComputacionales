#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 15:51:29 2018

@author: memoherrera

Insertion Sort sorting algorithm 


"""
def insertionSort(lista):
    for i in range(1, len(lista)):
        j = i-1 
        siguienteElemento = lista[i]
        
        while (lista[j] > siguienteElemento) and (j >= 0):
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = siguienteElemento

lista = [2, 3, 5, -23, 45, 35, 445, -345, 4532, 0]
print(lista)
insertionSort(lista)
print(lista)
