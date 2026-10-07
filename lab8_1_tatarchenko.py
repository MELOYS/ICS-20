from array import *
import random

n = int(input("Введіть N (N >= 12): "))

K = array('i', [])
M = array('i', [])
T = array('i', [])

for i in range(6):
    K.append(random.randint(12, n))

for i in range(24):
    M.append(random.randint(12, n))

for i in range(24):
    if M[i] in K:
        T.append(M[i])

print("Масив K:")
print(K)

print("Масив M:")
print(M)

print("Масив T:")
print(T)