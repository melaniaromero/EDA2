# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 23:38:22 2020

@author: abihs
"""

def ordenar(lista1):
    if len(lista1) == 0:
        return []
    else:
        menor = lista1 [0]
        for i in range(1,len(lista1)):
            if lista1[i] < menor:
                menor = lista1[i]
        lista1.remove(menor) #se elimina el elemento menor
        return [menor] + ordenar(lista1)

elementos = int( input("Ingresa el número de elementos que tendrá tu lista: "))
print("Ingresa tus elementos: ")
lista1 = []
for i in range (0, elementos):
    lista1.append(float(input())) #append es para añadir elementos a un arreglo
print("Tu lista es: ", lista1)
lista2 = ordenar(lista1)
print("Tu lista ordenada es : ", lista2)