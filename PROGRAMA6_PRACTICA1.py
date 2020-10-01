def bubbleSort2(A):
    bandera = True
    pasada = 0
    while pasada < len(A)-1 and bandera:
        bandera = False
        for j in range (len(A)-1-pasada):
            if(A[j] < A[j+1] ):
                bandera = True
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
        pasada = pasada+1
        
A = [1, 2, 6, 3, 22, 7, 9, 23, -6, -2, -9]
bubbleSort2(A)
print ("\n")
print (A)


#CODIGO DE LA FUNCION DOS PARA PONERLOS AL REVES

