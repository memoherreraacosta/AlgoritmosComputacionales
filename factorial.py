#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 10:15:09 2018

@author: memoherrera

Funcion Factorial
"""

def factorial(n):
    if n==0 :
        return 1
    else :
        return n*factorial(n-1)
    
print(factorial(3))