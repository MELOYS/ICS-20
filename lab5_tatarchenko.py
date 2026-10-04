import math

x = float(input("Введіть x: "))

if x > 9:
    y = 3.11 + math.log10(2 * x) + math.log(x + 8, 3)
elif 1 <= x <= 9:
    y = 1 / x + (2 + x) / (math.exp(x) + x ** 2)
else:
    y = 6.23 * (x - 0.7 + math.exp(3 * x))

print("y =", y)