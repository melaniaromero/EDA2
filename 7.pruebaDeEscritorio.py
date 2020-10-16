def numeros(x, y):
    suma_x = 0
    suma_y = 0
    for i in range(1, x):
        if x % i == 0:
            suma_x += i

    for k in range(1, y):
        if y % k == 0:
            suma_y += k
    return suma_x == y and suma_y == x


# cuerpo del programa
n1 = int(input('introduzca el n1\n'))
n2 = int(input('introduzca el n2\n'))

if numeros(n1, n2):
    print('¡son!: ')
else:
    print('no son: ')
