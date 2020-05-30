#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 09:45:13 2018

@author: memoherrera

Algoritmo de ordenamiento 

MergeSort

"""

def mergeSort(lista):
    if len(lista)>1 : 
        mid = len(lista)//2
        mitadIzq = lista[:mid]
        mitadDer = lista[mid:]
        
        mergeSort(mitadIzq)
        mergeSort(mitadDer)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(mitadIzq) and j < len(mitadDer) :
            if mitadIzq[i] < mitadDer[j]:
                lista[k] = mitadIzq[i]
                i+=1
            else: 
                lista[k] = mitadDer[j]
                j+=1
                
            k+=1
            
        while i < len(mitadIzq) :
            lista[k] = mitadIzq[i]
            i+=1
            k+=1
        
        while j < len(mitadDer) :
            lista[k] = mitadDer[j]
            j+=1
            k+=1


lista = [2,3,5,-23,45,35,445,-345,4532,0]
print(lista)
mergeSort(lista)
print(lista)