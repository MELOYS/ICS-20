import csv

file = "phone.csv"

name = input("Ім'я: ")
phone = input("Телефон: ")

with open(file, "a", newline="", encoding="utf-8") as f:
    csv.writer(f).writerow([name, phone])

print("\nТелефонний довідник:")

with open(file, "r", encoding="utf-8") as f:
    for row in csv.reader(f):
        print(row[0], "-", row[1])