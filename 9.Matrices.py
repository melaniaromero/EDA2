##PROGRAMA QUE DADA UNA MATRIZ NXN, OBTENGA NUMEROS ALEATORIOS Y ORDENARLOS OON METODO BURBUJA
def imprimir(matriz, N):
    print("\n")
    for i in range(1):
        for j  in range(0,N):
            print (matriz[j])

def bubbleSort(A):
    for i in range(1, len(A)+1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

def Acomodar(matriz, N):
    matrizl = []
    for i in range(1):
        for j  in range(0,N):
            matrizl = matrizl + matriz[j]
    bubbleSort(matrizl)
    k = 0
    matriz2 = [[0 for x in range(N)] for y in range (N)]
    for i in range(0,N):
        for j  in range(0,N):
            matriz2[i][j] = matriz2[i][j] + matrizl[k]
            k = k+1
    print("\nLa matriz ordenda es:")
    imprimir(matriz2, N)

#Creando la matriz aleatoria
import random 
print ("ATENCION... MATRICES MENORES A 11x11")
N= int(input("Ingrese el tamaño de la matriz (nxn): "))
while (N > 10 or N <=0):
    print ("\nSolo puedes ingresar matriz menores de 11x11")
    N= int(input("Ingrese el tamaño de la matriz (nxn): "))

matriz = [[0 for x in range(N)] for y in range (N)]
for i in range (0,N):
	for j in range (0,N):
 		matriz[i][j] = random.randint(0,100) 
#Iprimiend la matriz aleatoria y acomodandola
print("\nLa matriz aleatoria es: ")
imprimir(matriz, N)
Acomodar(matriz,N)
