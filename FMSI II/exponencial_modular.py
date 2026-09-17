def exp_modular(a, n, m):
    if m <= 1:
        return "Impossível calcular."
    if a == 0 and n == 0:       # restrição
        return "Impossível calcular."
    
    if n == 0:      # caso base
        return 1 % m
    
    return (a*exp_modular(a, n - 1, m)) % m

# TESTES
print(exp_modular(2, 20, 1))
print(exp_modular(3, 5, 13))
print(exp_modular(0, 0, 10))
print(exp_modular(4, 0, 7))