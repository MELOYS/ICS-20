
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Вартість товарів")
window.geometry("220x180")
window.configure(bg="blue")

products = [
    ("Хліб", 20, 25, 30),
    ("Молоко", 30, 35, 42),
    ("Яйця", 40, 50, 60),
    ("Цукор", 25, 30, 35),
    ("Сіль", 10, 12, 15),
    ("Масло", 50, 65, 80),
    ("Сир", 100, 120, 150),
    ("Кава", 80, 95, 110),
    ("Чай", 40, 45, 55),
    ("Рис", 35, 40, 50),
    ("Гречка", 45, 50, 60),
    ("Макарони", 25, 30, 40)
]

def save_data():
    with open("products.txt", "w", encoding="utf-8") as file:
        file.write(
            f"{'Товар':<15}{'2022':<10}"
            f"{'2023':<10}{'2024':<10}\n"
        )
        file.write("-" * 45 + "\n")

        for name, y1, y2, y3 in products:
            file.write(
                f"{name:<15}{y1:<10}"
                f"{y2:<10}{y3:<10}\n"
            )

    messagebox.showinfo(
        "Готово",
        "Дані збережено у products.txt"
    )

label = tk.Label(
    window,
    text="Вартість товарів",
    bg="blue",
    fg="white"
)
label.place(x=50, y=30)

button = tk.Button(
    window,
    text="Зберегти таблицю",
    command=save_data
)
button.place(x=45, y=80)

window.mainloop()
