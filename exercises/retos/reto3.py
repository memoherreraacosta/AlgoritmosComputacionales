#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 11:09:39 2018

@author: memoherrera
"""

def mergeSort(lista):
    if len(lista) > 1 :
        media = int(len(lista)/2)
        listaIzq = mergeSort(lista[:media])
        listaDer = mergeSort(lista[media:])
        return merge(listaIzq,listaDer)
    else:
        return lista

def merge(listaIzq, listaDer):
    i,j = 0,0 #i y j son apuntadores de las listas izq y der
    listaOrdenada = []
    while (i<len(listaIzq) and j<len(listaDer)):
        if (listaIzq[i] <= listaDer[j]):
            listaOrdenada.append(listaIzq[i])
            i += 1
        else:
            listaOrdenada.append(listaDer[j])
            j += 1

    listaOrdenada += listaIzq[i:]
    listaOrdenada += listaDer[j:]
    return listaOrdenada


lista = [2,3,5,-23,45,35,445,-345,4532,0]
print(lista)
print(mergeSort(lista))
