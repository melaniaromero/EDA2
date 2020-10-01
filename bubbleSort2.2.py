def bubbleSort2(A):
    bandera = True
    pasada = 0
    while pasada < len(A)-1 and bandera:
        bandera = False
        print ("Pasada # ", pasada)
        for j in range (len(A)-1-pasada):
            if(A[j] > A[j+1] ):
                bandera = True
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                print (A)
        pasada = pasada+1
    print ("\n")
    print ("Total de pasadas = ", pasada)
    print("La cadena de n caracteres ordenada del menor al mayor es: ")
    print (A)
        
A = [1, 2, 6, 3, 22, 7, 9, 23, -6, -2, -9]
bubbleSort2(A)
