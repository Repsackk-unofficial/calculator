import tkinter as tk
from tkinter import ttk, messagebox
from funkcje import basic_ops as f

def create_basic_tab(tab):
    tk.Label(tab, text="Liczba a:").grid(row=0, column=0, padx=5, pady=5)
    entry_a = tk.Entry(tab)
    entry_a.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(tab, text="Liczba b / podstawa:").grid(row=1, column=0, padx=5, pady=5)
    entry_b = tk.Entry(tab)
    entry_b.grid(row=1, column=1, padx=5, pady=5)

    combo = ttk.Combobox(tab, values=[
        "Dodawanie", "Odejmowanie", "Mnożenie", "Dzielenie",
        "Potęgowanie", "Pierwiastkowanie", "Silnia", "Logarytm"
    ])
    combo.current(0)
    combo.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(tab, text="Wybierz działanie:").grid(row=2, column=0, padx=5, pady=5)

    result_label = tk.Label(tab, text="Wynik:")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate():
        try:
            a = float(entry_a.get())
            b_text = entry_b.get()
            op = combo.get()

            if op == "Dodawanie":
                res = f.add(a, float(b_text))
            elif op == "Odejmowanie":
                res = f.subtract(a, float(b_text))
            elif op == "Mnożenie":
                res = f.multiply(a, float(b_text))
            elif op == "Dzielenie":
                res = f.divide(a, float(b_text))
            elif op == "Potęgowanie":
                res = f.power(a, float(b_text))
            elif op == "Pierwiastkowanie":
                res = f.sqrt(a)
            elif op == "Silnia":
                res = f.factorial(int(a))
            elif op == "Logarytm":
                res = f.logarithm(a, float(b_text) if b_text else 10)

            result_label.config(text=f"Wynik: {res}")

        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    tk.Button(tab, text="Oblicz", command=calculate)\
        .grid(row=3, column=0, columnspan=2, pady=10)
