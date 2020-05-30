#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:22:05 2018

@author: memoherrera

"""

#Probela 1
#Escribe una función recursiva que tome un entero
#y calcule la suma cumulativa desde cero hasta ese entero.
#ejemplo SumCum(3)=6

def sumatoria(n):
    if n==0:
        return 0 
    else: 
        return n + sumatoria(n-1)
    
print(sumatoria(100))

#Problema 2
#Dado un entero, sumar todos los dígitos de ese entero:
#Ejemplo sumdigit(43)= 7

def sumaDig(n):
    if (n<10) :
        return n
    else:
        return n%10 + sumaDig(int(n/10))

print(sumaDig(433))

#Problema 3
#Crea una función recursiva que invierta un string:
#Ejemplo dereversa(raborper_a_yov)= voy_a_reprobar
#def dereversa(string):

def deReversa(palabra):
    if (len(palabra) == 1):
        return palabra
    else :
        return deReversa(palabra[1:]) + palabra[0]

print(deReversa("raborper_a_yov"))
