#Programa que calcula pi mediante la serie de Leibniz
def Sumatoria(n):
    suma = ((-1)**n)/((2*n)+1)
    return suma

aproxPi = 0
a= int(input("Elige un numero y presiona enter \n"))
for i in  range (a):
    aproxPi = aproxPi + Sumatoria(i)
print(aproxPi*4)