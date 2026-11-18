
import tkinter as tk
import string
import unicodedata

def clean_text():
    text = entry.get()

    result = ""

    for char in text:
        category = unicodedata.category(char)

        if category.startswith("P"):
            continue

        if category.startswith("C"):
            continue

        result += char

    entry.delete(0, tk.END)
    entry.insert(0, result)

window = tk.Tk()
window.title("Очищення тексту")
window.geometry("400x200")

label = tk.Label(
    window,
    text="Введіть текст:"
)
label.pack(pady=10)

entry = tk.Entry(
    window,
    width=45
)
entry.pack(pady=10)

button = tk.Button(
    window,
    text="Очистити текст",
    command=clean_text
)
button.pack(pady=10)

window.mainloop()
