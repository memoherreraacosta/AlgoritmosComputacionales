#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 16:14:16 2018

@author: memoherrera


Selection Sort sorting algorithm 
"""

def selectionSort(lista):
    for i in range(len(lista)):
        minI = i
        for j in range(minI, len(lista)):
            if lista[minI] > lista[j] :
                minI = j
        
        lista[i],lista[minI] = lista[minI], lista[i]

lista= [2, 3, 5, -23, 45, 35, 445, -345, 4532, 0]
print(lista)
selectionSort(lista)
print(lista)