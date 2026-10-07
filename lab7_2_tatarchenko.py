import random

s = input("Введіть повідомлення: ")

n = 1

while n * n < len(s):
    n = n + 1

symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

while len(s) < n * n:
    s = s + random.choice(symbols)

print("Доповнений рядок:")
print(s)

print("Зашифроване повідомлення:")

for i in range(n):
    result = ""
    for j in range(n):
        result = result + s[j * n + i]
    print(result)