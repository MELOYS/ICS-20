n = int(input("Введіть кількість слів: "))

words = []

for i in range(n):
    word = input("Введіть слово: ")
    if word not in words:
        words.append(word)

result = " ".join(words)

print("Результат:")
print(result)