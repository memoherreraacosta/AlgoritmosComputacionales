#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 10:43:13 2018

@author: memoherrera

Implementa el Counting Sort
"""
def countingSort(array):

    valormax = max(array) + 1
    lista = [0] * valormax
    listaFinal = []

    for i in array:
         lista[i] += 1

    for j in range(len(lista)):
         listaFinal.extend([j] * lista[j])
             
    return listaFinal

def quickSort(array):
    quickSort(array, 0, len(array)-1)

def quickSort2(array, start, end):
    if (start < end) :
        p = partition(array, start, end)
        quickSort2(array, start, p-1)
        quickSort2(array, p+1, end)
    
def partition(A, start, end):
    pivote = A[ (start + end) // 2 ]
    swap(A, min,(start + end) // 2)
    i = start +1
    j = min +1 
    for j in range(end+1):
        if (A[j] < pivote):
            swap(A,i,j)
            i += 1
    swap(A,start,i-1)
    return i-1

def swap(A, start, end):
    tmp = A[start]
    A[start] =  A[end]
    A[end] = tmp

    
array = [1,0,7,3,3,9,12,25,17]
print(countingSort(array))
        