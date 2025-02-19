def tetration(a, b):
    if b == 1:
        return a
    return a ** tetration(a, b - 1)

print(tetration(2, 4)) # 2 ** 2 ** 2 ** 2 = 65536

def pentation(a, b):
    if b == 1:
        return a
    return tetration(a, pentation(a, b - 1))

print(pentation(2, 3)) # 2 ** 2 ** 2 = 16
