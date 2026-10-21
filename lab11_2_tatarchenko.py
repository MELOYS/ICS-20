import json

firms = []

with open("one.txt", "r", encoding="utf-8") as file:
    firms.extend(json.load(file))

with open("two.txt", "r", encoding="utf-8") as file:
    firms.extend(json.load(file))

print(f"{'Фірма':<15}{'Прибуток':<15}{'Працівники':<15}")
print("-" * 45)

for firm in firms:
    print(f"{firm['name']:<15}{firm['profit']:<15}{firm['employees']:<15}")

best_firm = max(
    firms,
    key=lambda firm: firm["profit"] / firm["employees"]
)

efficiency = best_firm["profit"] / best_firm["employees"]

print("\nНайефективніша фірма:", best_firm["name"])
print("Прибуток на одного працівника:", round(efficiency, 2))