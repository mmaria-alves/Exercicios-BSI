def exponencial(a, n):
    if a == 0 and n == 0:       # restrição
        return "Impossível calcular."
    if n < 0:       # restrição
        return 1
    if n == 0:      # caso base
        return 1
    else:
        return a*exponencial(a, n-1)


# TESTES
print("3^4:", exponencial(3, 4))
print("0^0:", exponencial(0, 0))
print("-2^2:", exponencial(-2, 2))
print("5^-2:", exponencial(5, -2))