from time import time #importamos la función time para capturar tiempos
import random         #antes de utilizar una función se debe importar la función o la biblioteca entera
def bubbleSort(A):
    for i in range(1,len(A)+1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
def listaAleatorios(n):
      lista = [0] * n
      for i in range(n):
          lista[i] = random.randint(0, 2000)
      return lista

A=listaAleatorios(2000)
print("Los números aleatorios son: \n", A)
tiempo_inicial = time() 
bubbleSort(A)
tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial
print('\nEl tiempo de ejecucion fue de:',tiempo_ejecucion)
print("\nA continuación se muestran los números aleatorios ordenados:\n", A)
