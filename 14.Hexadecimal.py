def Hexadecimal(B, res):
    mod = B % 16
    div = B//16
    if B == 0:
        return res[::-1]
    RES = str(mod)
    if mod < 10:
        res += RES
        return Hexadecimal(div, res)
    if mod == 10:
        res += 'A'
        return Hexadecimal(div, res)
    elif mod == 11:
        res += 'B'
        return Hexadecimal(div, res)
    elif mod == 12:
        res += 'C'
        return Hexadecimal(div, res)
    elif mod == 13:
        res += 'D'
        return Hexadecimal(div, res)
    elif mod == 14:
        res += 'E'
        return Hexadecimal(div, res)
    elif mod == 15:
        res += 'F'
        return Hexadecimal(div, res)


B = int(input("Dame un numero y lo convertire a hexadecimal\n"))
res = ' '
print(f"El numero {B} en hexadecimal es: ", Hexadecimal(B, res))
