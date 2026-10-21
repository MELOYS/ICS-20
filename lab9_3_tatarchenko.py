
cities = input("Введіть назви міст через пробіл: ").split()

city_dict = {}

for city in cities:
    value = input(f"Введіть значення для міста {city}: ")
    city_dict[city] = value

print("Створений словник:")
for city, value in city_dict.items():
    print(city, ":", value)