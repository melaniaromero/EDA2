def bubbleSort(A):
    for i in range(1, len(A)+1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
A=[1,2,6,3,22,7,9,23,-6,-2,-9]
bubbleSort(A)
print("\n")
print(A)

