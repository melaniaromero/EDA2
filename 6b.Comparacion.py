print("Programa que compara numeros")
A=int(input("Ingrese el valor A: "))
B=int(input("Ingrese el valor B: "))
C=int(input("Ingrese el valor C: "))
if A>B and A>C:
	print(A," = A Es mayor")
elif B>A and B>C:
	print(B," = B Es mayor")
else:
	print(C," = Es el mayor")