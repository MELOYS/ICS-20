import re
import numpy as np
import pylab

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()

words = re.findall(r'\b[a-z]+\b', text)

keywords = input('Введіть ключові слова через пробіл: ').lower().split()

frequencies = []

for word in keywords:
    count = words.count(word)
    frequencies.append(count)
    print(word, '-', count)

x = np.arange(len(keywords))

pylab.bar(x, frequencies)
pylab.xticks(x, keywords)
pylab.xlabel('Ключові слова')
pylab.ylabel('Кількість повторень')
pylab.title('Частота появи слів у тексті')
pylab.show()