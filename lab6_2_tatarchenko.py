import math

a=float(input("Введіть a: "))
b=float(input("Введіть b: "))
h=float(input("Введіть h: "))

x=a
y=0.0

while x<=b:
    y=(math.cos(x)+math.exp(x))/(math.log2(abs(x))+0.19)
    print("x=",x," y=",y)
    x=x+h