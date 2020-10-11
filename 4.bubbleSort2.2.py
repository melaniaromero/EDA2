def bubbleSort2(A):
    bandera = True
    pasada = 0
    while pasada < len(A)-1 and bandera:
        bandera = False
        for j in range (len(A)-1-pasada):
            if(A[j] > A[j+1] ):
                bandera = True
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
        pasada = pasada+1
        print ("Pasada # ", pasada)
        print (A)
    print ("\n")
    print ("Total de pasadas = ", pasada)
    print("La cadena de n caracteres ordenada del menor al mayor es: ")
    print (A)
        
A = [5,4,3,2,1,0]
bubbleSort2(A)
