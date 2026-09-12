number_str = input("Введіть чотирицифрове число: ")
d1 = int(number_str[0])
d2 = int(number_str[1])
d3 = int(number_str[2])
d4 = int(number_str[3])
product = d1 * d2 * d3 * d4 
geometric_mean = product ** 0.25
print(f"Середнє геометричне цифр: {geometric_mean:.2f}")