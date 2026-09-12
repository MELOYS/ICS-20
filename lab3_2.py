import sys

number = int(sys.argv[1])

a = number // 1000
b = number // 100 % 10
c = number // 10 % 10
d = number % 10

result = (a * b * c * d) ** (1 / 4)

print("Середнє геометричне цифр =", result)