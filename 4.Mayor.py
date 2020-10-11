def maximo(N1,N2):
    if N1 > N2:
        return N1
    else:
        return N2
    
print ("Ingresa dos numeros y te dire cual es el mayor:")
N1 = int(input("Ingresa el primer numero: "))
N2 = int(input("Ingresa el segundo numero: "))
print("\n\tN1 = " + str(N1) + "; N2 = " + str(N2) + ".")
if (maximo(N1,N2) == N1):
    print("El numero mayor entre N1 y N2 es: N1 = " + str(maximo(N1,N2)) + ".")
else:
    print("El numero mayor entre N1 y N2 es: N2 = " + str(maximo(N1,N2)) + ".")
    