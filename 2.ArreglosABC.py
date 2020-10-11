def bubbleSort(A):
    for i in range(1, len(A)+1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

def acomodar(A,B):
    C = []
    for i in range (0, 11):
        C.append(A[i])
    for j in range (0, 11):
        C.append(B[j])
    print ("\n\t\tLos arreglos A Y B convinados formndo a C: ")
    print ("\nArreglo C: " + str(C) + "; Tamaño: " + str(len(C)))
    bubbleSort(C)
    print ("\n\t\tC acomodado por medio de BubbleSort: ")
    print ("\nArreglo C: " + str(C) + "; Tamaño: " + str(len(C)))

print ("\n\t\tPrograma que crea dos arreglos de tamaño 11.")
print ("\t\tConvina ambos arreglos y los ordena de menor a mayos")
print ("\t\tcon el metodo de la burbuja \n")
#Creando los arreglos de tamaño 11
A = [-22, 4, -6, 8, -15, 9, -7, 44, -10, 13, -12]
B = [22, -4, 6, -8, 15, -9, 7, -44, 10, -13, 12]
print ("Arreglo A: " + str(A) + "; Tamaño: " + str(len(A)))
print ("Arreglo B: " + str(B) + "; Tamaño: " + str(len(B)))
acomodar(A,B)