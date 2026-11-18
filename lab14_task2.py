
import requests
from bs4 import BeautifulSoup
import json

sites = input("Введіть URL-адреси через пробіл: ").split()

result = {}

for site in sites:
    try:
        response = requests.get(site, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        count = len(paragraphs)

        result[site] = count

        print(site, "- кількість абзаців:", count)

    except requests.RequestException:
        print("Помилка доступу до сайту:", site)
        result[site] = None

with open("paragraph.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)

print("Результати записано у paragraph.json")
