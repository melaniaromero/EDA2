# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:10:15 2020

@author: abihs
"""
#sumar N(n, numeros)
#Realizar una función que dada una lista de números y un número N, retorna la suma de todos los N primeros elementos
#Ejemplo sumarN (3, [2, 4, 6, 8, 10, 12]) -> 2+4+6 = 24
def sumarN (n, e):
    if( n==0 or len(e) == 0): #caso base
        return 0
    else:
        primer_elemento = e.pop(0)#quita primer elemento del arreglo y lo devuelve
        resultado = primer_elemento + sumarN(n-1, e)
        return resultado

elementos = int( input("Ingresa el número de elementos que tendrá tu lista:"))
print(elementos) 
print("Ingresa tus elementos:")
e = []
for i in range (0, elementos):
    e.append(float(input()))#append es para añadir elementos a un arreglo
print("Tu lista es: ", e)
n = int (input("Ingresa la cantidad de elementos a sumar: "))
suma1 = sumarN(n, e)
print(suma1)
