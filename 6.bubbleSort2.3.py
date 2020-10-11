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
        
A = [5,4,3,2,1,0]
bubbleSort2(A)
print ("\n")
print("La cadena de n caracteres ordenada del mayor a menor es: ")
print (A)
