def bubbleSort(A):
    pasada = 0
    for i in range(1, len(A)+1):
        print ("Pasada # ", pasada)
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                pasada = pasada + 1
                print (A)
    print ("\n")
    print ("Total de pasadas = ", pasada)
    print("La cadena de n caracteres ordenada del menor al mayor es: ")
    print (A)

A = [1, 2, 6, 3, 22, 7, 9, 23, -6, -2, -9]
bubbleSort(A)