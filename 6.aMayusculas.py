##PROGRAMA QUE DADO UNA CADENA, LA CONVIERTE A MAYUSCULAS, TODO CON RECURSIVIDAD
def aMayusculas(cadena, i):
        x = len(cadena)
        if x > i:
            if cadena[i].islower() == True and cadena[i].isdigit() == False and cadena[i].isspace() == False: 
                cadena[i] = cadena[i].upper()
                aMayusculas(cadena, i+1)
            else:
                aMayusculas(cadena, i+1)
i = 0  
palabras = input("Introduce una cadena de texto: \n")
cadena = list(palabras)
x = len(cadena)
aMayusculas(cadena, i)
palabras = "".join(cadena)
print (palabras)
