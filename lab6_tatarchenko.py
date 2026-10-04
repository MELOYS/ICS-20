import math

a=int(input("Введіть a: "))
b=int(input("Введіть b: "))
h=int(input("Введіть h: "))

for x in range(a,b+1,h):
    y=(math.cos(x)+math.exp(x))/(math.log2(abs(x))+0.19)
    print("x=",x," y=",y)