import numpy as np
import random

a = int(input("Введіть a: "))

A = np.zeros((4, 6), dtype=int)

for i in range(4):
    for j in range(6):
        A[i][j] = random.randint(-a, a)

B = []

for i in range(4):
    for j in range(6):
        if A[i][j] > 0:
            B.append([i, j])

B = np.array(B)

print("Масив A:")
print(A)

print("Масив B:")
print(B)