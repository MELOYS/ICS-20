import math

x = float(input("Введіть x: "))

f = math.exp(x + math.sqrt(x) + math.cos(x)) - \
    (2.9 * x - 1 / math.tan(x)) / math.pow(3, 0.7 * x + math.sqrt(x))

print("f(x) =", f)