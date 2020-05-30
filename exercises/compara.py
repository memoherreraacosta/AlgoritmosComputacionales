#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:36:24 2018

@author: memoherrera

Esta funcion verifica si existe un objeto dentro de la lista
"""
def compara(lista, item):
	for i in lista :
		if item == i :
			return True
			break
	
	return false