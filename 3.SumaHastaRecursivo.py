

def Suma(N,sums,cont): 
    
    if (cont <= N):
        sums=sums+cont
        cont+=1
        Suma(N,sums,cont)
    else:
        print("La suma desde 0 hasta ", N , " es: ", sums)
    
print("¿Hasta que numero deseas sumar? \n")
N=int(input())
sums=0
cont=0
Suma(N,sums,cont)

