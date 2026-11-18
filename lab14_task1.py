
import requests
from bs4 import BeautifulSoup
import re

with open("sites.txt", "r", encoding="utf-8") as file:
    sites = file.readlines()

with open("result.txt", "w", encoding="utf-8") as result:
    for site in sites:
        site = site.strip()

        if not site:
            continue

        try:
            response = requests.get(site, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(" ")

            emails = re.findall(
                r'[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}',
                text
            )

            for link in soup.find_all("a", href=True):
                href = link["href"]
                if href.startswith("mailto:"):
                    email = href[7:].split("?")[0]
                    emails.append(email)

            emails = sorted(set(emails))

            result.write("Сайт: " + site + "\n")

            for email in emails:
                result.write(email + "\n")

            if not emails:
                result.write("E-mail не знайдено\n")

            result.write("\n")

        except requests.RequestException:
            result.write(
                "Помилка доступу до сайту: " + site + "\n\n"
            )

print("Готово! Результати записано у result.txt")
