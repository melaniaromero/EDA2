def bubbleSort(A):
    for i in range(1, len(A)+1):
        for j in range(len(A)-1):
            if x == 1: 
                if A[j]<A[j+1]:
                    temp = A[j]
                    A[j] = A[j+1]
                    A[j+1] = temp
            if x== 2 :
                if A[j]>A[j+1]:
                    temp = A[j]
                    A[j] = A[j+1]
                    A[j+1] = temp
                    
import random #Necesario para poder utilizar la funcion random
print("¡Hola! Este es algoritmo de la burbuja y ordenara 1000 numeros aleatorios\n")

print("Si quieres que los ordene de  mayor a menor presiona 1")
print("Si quieres que los ordene de menor a mator presiona 2")
x=int(input("Escribe tu opcion: "))
while x > 2 or x <= 0:
    print("\nOpción no valida: \n1) Para ordenarlos de  menor a mayor. \n2) Para ordenarlo de mayor a menor")
    x=int(input("Escribe tu opcion: "))
A=[]
for i in range (0,1000,1):
    f=(random.randrange(-1000,1000,1))  
    A.append(f) #.append para añadir valores a la lista
print("\nLos caracteres principales son:")
print ("\n", A)
bubbleSort(A)
print("\n")
if x == 1 :
    print("Los números ordenados de mayor a menor son:\n ")
    print(A)
if x == 2:
    print("Los números ordenados de menor a mayor son:\n")
    print(A)
    