
countries = input("Введіть назви країн через пробіл: ").split()

countries = tuple(sorted(countries, key=len))

print("Країни за зростанням довжини назв:")
for country in countries:
    print(country)
