def rangoHasta(A,l,i):
  i+=1
  A.append(i)
  if i < l:
    return  rangoHasta(A,l,i) 
  else:
    return A

n= int(input("Escriba el número de elementos de la lista:\n"))
while (n<0):
    print("---Vuelve a ingresar tus datos---\n")
    n= int(input("Escriba el numero de elementos de la lista:\n"))
A=[]
rangoHasta(A,n,-1)
print (A)
