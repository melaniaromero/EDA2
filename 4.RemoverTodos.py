lista2=[]   #Lista con resultados
#Funcio que crea la lista con los numeros sin repetir
def crear(lista2, num):
    lista2.append(num)
    return lista2
#Funcion que quita los numeros duplicados
def sinDuplicado(lista,num):
    #Verificando si hay elementos en la lista
    if len(lista)==0:
        print("\n----------")
        print("La lista sin el numero 3 repetido es:")
        print (lista2)
    else:
        #Verificando si se repite el valor de la lista en ella misma
        for i in range (1,len(lista)):
            if lista[0]==num:
                lista.pop(0)
        #Asignando a la lista sin elementos duplicados el numero evauado
        crear(lista2, lista[0])
        sinDuplicado(lista[1:],num)
#Creacion de lista y llamando a la funcion recursiva que quita los numeros duplicados      
import random
lista = []
for i in range (0, 10):
    f=(random.randrange(0,10,1))
    lista.append(f)
print("\nLa lista original consta de 10 elementos aleatorios entre 0-8 para asegurar que se repitan n veces n numeros.\n")
print ("La lista original es: ")
print (lista)
num = 3
sinDuplicado(lista,num)

   