def Conejos(meses):
    if meses == 1:
        return 1
    if meses == 2 or meses == 3:
        return 1
    return Conejos(meses-1) + Conejos(meses-2)


print("acabas de comprar una pareja de conejos\n¿cuantos meses vas a esperar?")
meses = int(input())
print(f"El numero de parejas de conejos a los {meses} meses seran:", Conejos(meses+1))
