def mdc(a, b):
    if a == 0 and b == 0:
        return "indeterminado."
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

# TESTES
print(mdc(-30, 50))
print(mdc(48, 18))
print(mdc(1234, 5678))
print(mdc(0, 35))
print(mdc(-10, -25))