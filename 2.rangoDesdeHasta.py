def rango(A, n, i):
  n+=1
  A.append(n)
  if n < i:
    return  rango(A,n, i) 
  else:
    return A

d= int(input("Escriba el limite minimo de su lista:\n"))
while (d<0):
    print("---Vuelve a ingresar tus datos---\n")
    d= int(input("Escriba el numero de elementos de la lista:\n"))
h=int(input("Escribe el limite maximo de su lista:\n"))
if(h<d):
    h=int(input("Escribe el limite maximo de su lista:\n"))
A=[]
rango(A,d-1,h)
print(A)
