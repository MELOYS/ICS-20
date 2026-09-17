import math

def func1(x, y, z, a):
    L = (x * math.cos(y) + z) - \
        (math.tan(y) + math.exp(a)) / math.pow(2, z + 2.4)
    return L

x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
z = float(input("Введіть z: "))
a = float(input("Введіть a: "))

L = func1(x, y, z, a)

print("L =", L)