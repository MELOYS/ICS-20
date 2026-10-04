import math

a=float(input("Введіть a: "))
b=float(input("Введіть b: "))
h=float(input("Введіть h: "))

x=a
y=0.0
A=[]

while x<=b:
    y=(math.cos(x)+math.exp(x))/(math.log2(abs(x))+0.19)
    A.append(y)
    x=x+h
    print("Список A:")

for elem in A:
    print(elem)

B=A[:3]+A[-3:]

print("Список B:")
print(B)