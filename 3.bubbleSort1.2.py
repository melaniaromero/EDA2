def bubbleSort(A):
    pasada = 0
    for i in range(1, len(A)+1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                pasada = pasada + 1
                print ("Pasada # ", pasada)
                print (A)
    print ("\n")
    print ("Total de pasadas = ", pasada)
    print("La cadena de n caracteres ordenada del menor al mayor es: ")
    print (A)

A = [5,4,3,2,1,0]
bubbleSort(A)
