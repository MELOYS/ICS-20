
import mymodule

n = int(input("Введіть натуральне число: "))

if n > 0:
    print("Кількість простих дільників =", mymodule.prosti(n))
    print("Кількість усіх дільників =", mymodule.dilniki(n))
else:
    print("Введіть натуральне число більше нуля")
