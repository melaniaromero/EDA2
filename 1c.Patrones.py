##Programa que solicita al usuario un número entero positivo,
## y utilizando ciclos imprima patrones
asterisco = int(input("Ingresa un número entero positivo: "))
for i in range(1, asterisco + 1):
    for j in range(i):
        print('*', end='')
    print()

print()
for i in range(asterisco):
    for j in range(asterisco):
        print('*', end= '')
    print()
    
