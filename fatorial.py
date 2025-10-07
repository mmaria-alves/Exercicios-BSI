def fatorial(n):
    if n < 0:
        return 0
    if n == 1:
        return 1
    else:
        return n*fatorial(n-1)

# TESTES
print("6:", fatorial(6))
print("10:", fatorial(10))
print("0:", fatorial(0))
print("-1:", fatorial(-1))