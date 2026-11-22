import pandas as pd
import math

f = open('cords.txt', 'r')

points = []

for line in f:
    x, y = map(float, line.split())
    points.append((x, y))

f.close()

A, B, C, D = points

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 +
                     (p2[1] - p1[1])**2)

m = pd.Series(
    [distance(A, B), distance(B, C),
     distance(C, D), distance(D, A)],
    index=['AB', 'BC', 'CD', 'DA']
)

m['AC'] = distance(A, C)
m['BD'] = distance(B, D)

print('Сторони та діагоналі:')
print(m)

m.to_json('figure.json', indent=4)

print('\nДані збережено у файл figure.json')