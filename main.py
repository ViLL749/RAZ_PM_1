import os
import tkinter as tk


def IsLeapYear(Y, date_str):
    # Определяет, является ли год Y високосным и возвращает результат в виде строки
    if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
        return f"{date_str} является високосным\n"
    else:
        return f"{date_str} не является високосным\n"


def main():
    Dates = "/Users/vill/Desktop/tex/Ucheb_PR/RAZ_PM_1/Dates"

    with open(Dates, "r") as file:
        lines = file.readlines()

    results = ""  # Переменная для хранения всех результатов
    for line in lines:
        date_str = line.strip()  # Убираем пробелы и символы новой строки
        day, month, year = map(int, date_str.split('.'))  # Разбиваем строку и преобразуем части в числа
        results += IsLeapYear(year, date_str)  # Добавляем результат к общей строке

    label1.config(text=results)  # Обновляем текст виджета сразу со всеми результатами


root = tk.Tk()
root.title("Високосный год")
root.geometry("300x200")

btn = tk.Button(root, text="Проверить даты", command=main)
btn.pack(pady=20)

label1 = tk.Label(root, text="", font=("Arial", 14), justify="left")
label1.pack()

root.mainloop()
