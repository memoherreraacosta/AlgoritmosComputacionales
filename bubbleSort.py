#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 19:48:04 2018

@author: memoherrera
"""

def bubbleSort(lista):
    for i in range(len(lista)-1, 0,-1):
        for j in range(i):
            if lista[j] > lista [j+1]:
                tmp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = tmp

    return lista

lista = [1,2,4,3.5,2,7,43,-12,0]
print(bubbleSort(lista))