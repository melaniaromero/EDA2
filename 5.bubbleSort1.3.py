def bubbleSort(A):
    for i in range(1, len(A)+1):
        for j in range(len(A)-1):
            if A[j]<A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                
A = [5,4,3,2,1,0]
bubbleSort(A)
print("\n")
print("La cadena de n caracteres ordenada del mayor a menor es: ")
print(A)
