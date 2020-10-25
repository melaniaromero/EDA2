lista2=[]   #Lista con resultados
#Funcio que crea la lista con los numeros sin repetir
def crear(lista2, num):
    lista2.append(num)
    return lista2
#Funcion que quita los numeros duplicados
def sinDuplicado(lista):
    #Verificando si hay elementos en la lista
    if len(lista)==0:
        print("\n----------")
        print("La lista sin numeros repetidos es:")
        print (lista2)
    else:
        cont=0
        duplicado = []
        #Verificando si se repite el valor de la lista en ella misma
        for i in range (1,len(lista)):
            if lista[0]==lista[i]:
                cont = cont+1           #Cuantas veces se repite
                duplicado.append(i)     #Guardando en otra lista los indices de los elementos duplicados
        if cont>0:  #Si se repite el valor incial de la lista
            k=cont
            #Invertimos elementos de la lista duplicados para eliminar desde el final al inicio sin eliminar el primero
            duplicado2 = []
            for n in duplicado:
                duplicado2 = [n]+duplicado2
            #Eliminando de la lista los elementos duplicados para no volver a validar ese numero
            for j in range(k):
                lista.pop(duplicado2[j])
        #Asignando a la lista sin elementos duplicados el numero evauado
        crear(lista2, lista[0])
        sinDuplicado(lista[1:])
#Creacion de lista y llamando a la funcion recursiva que quita los numeros duplicados      
import random
lista = []
for i in range (0, 20):
    f=(random.randrange(0,8,1))
    lista.append(f)
print("\nLa lista original consta de 20 elementos aleatorios entre 0-7 para asegurar que se repitan n veces n numeros.\n")
print ("La lista original es: ")
print (lista)
sinDuplicado(lista)
