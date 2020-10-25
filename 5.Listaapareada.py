###PROGRAMA QUE DADO CIERTOS VALORES, LOS CONCATENA A UNA SOLA LISTA EN PARES
def Asignar(num, letter):
    i = len(num) - len(letter)
    x = num[i]
    y = letter[i]
    num.append((x,y))

def Aparear(num,letter):
    if(len(num) != 2*len(letter)):
        Asignar(num,letter)
        Aparear(num,letter)
    if ((len(num)-len(letter)) != 0):
        j = len(num) - len(letter) -1
        z = num[j]
        num.remove(z)

nummy = []
letty = []
n = int(input('Ingresa el número de elementos  '))
for j in range(n):
    nummy.append(int(input("Ingresa un valor para la lista de NUMEROS: " )))
print("\n")
for j in range(n):
    letty.append(input("Ingresa un caracter para la lista de LETRAS: "))
print("\n",nummy)
print("\n",letty)
Aparear(nummy,letty)
print("\n",nummy)

