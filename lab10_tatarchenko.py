keys = ["python", "file", "text", "data", "program"]

with open("site.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

with open("fr.txt", "w", encoding="utf-8") as file:
    for key in keys:
        count = text.count(key.lower())
        file.write(f"{key}-{count}\n")

print("Результат записано у файл fr.txt")