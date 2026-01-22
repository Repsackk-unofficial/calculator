import tkinter as tk
from tkinter import ttk, messagebox
import funkcje as f

root = tk.Tk()
root.title("Kalkulator Studencki")
root.geometry("900x700")  # trochę większe, żeby zmieścić TextBoxy

# =========================
# Zakładki
# =========================
tabControl = ttk.Notebook(root)

tab_basic = ttk.Frame(tabControl)
tab_matrix = ttk.Frame(tabControl)

tabControl.add(tab_basic, text='Podstawowe działania')
tabControl.add(tab_matrix, text='Macierze')
tabControl.pack(expand=1, fill="both")

# =========================
# PODSTAWOWE DZIAŁANIA
# =========================
tk.Label(tab_basic, text="Liczba a:").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(tab_basic)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(tab_basic, text="Liczba b / podstawa:").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(tab_basic)
entry_b.grid(row=1, column=1, padx=5, pady=5)

combo_op = ttk.Combobox(tab_basic, values=[
    "Dodawanie", "Odejmowanie", "Mnożenie", "Dzielenie", "Potęgowanie",
    "Pierwiastkowanie", "Silnia", "Logarytm"
])
combo_op.current(0)
combo_op.grid(row=2, column=1, padx=5, pady=5)
tk.Label(tab_basic, text="Wybierz działanie:").grid(row=2, column=0, padx=5, pady=5)

def update_fields(event=None):
    op = combo_op.get()
    if op in ["Dodawanie", "Odejmowanie", "Mnożenie", "Dzielenie", "Potęgowanie"]:
        entry_a.config(state='normal')
        entry_b.config(state='normal')
        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
    elif op == "Pierwiastkowanie":
        entry_a.config(state='normal')
        entry_b.delete(0, tk.END)
        entry_b.config(state='disabled')
    elif op == "Silnia":
        entry_a.config(state='normal')
        entry_b.delete(0, tk.END)
        entry_b.config(state='disabled')
    elif op == "Logarytm":
        entry_a.config(state='normal')
        entry_b.config(state='normal')
        entry_b.delete(0, tk.END)
        entry_b.insert(0, "10")  # domyślna podstawa

combo_op.bind("<<ComboboxSelected>>", update_fields)

label_result_basic = tk.Label(tab_basic, text="Wynik:")
label_result_basic.grid(row=4, column=0, columnspan=2, pady=10)

def calculate_basic():
    try:
        op = combo_op.get()
        a_text = entry_a.get()
        b_text = entry_b.get()
        result = None

        if op in ["Dodawanie", "Odejmowanie", "Mnożenie", "Dzielenie", "Potęgowanie"]:
            a = float(a_text)
            b = float(b_text)
            if op == "Dodawanie": result = f.add(a, b)
            elif op == "Odejmowanie": result = f.subtract(a, b)
            elif op == "Mnożenie": result = f.multiply(a, b)
            elif op == "Dzielenie": result = f.divide(a, b)
            elif op == "Potęgowanie": result = f.power(a, b)
        elif op == "Pierwiastkowanie":
            a = float(a_text)
            result = f.sqrt(a)
        elif op == "Silnia":
            n = int(a_text)
            result = f.factorial(n)
        elif op == "Logarytm":
            a = float(a_text)
            base = float(b_text) if b_text else 10
            result = f.logarithm(a, base)

        label_result_basic.config(text=f"Wynik: {result}")
    except Exception as e:
        messagebox.showerror("Błąd", str(e))

btn_calc_basic = tk.Button(tab_basic, text="Oblicz", command=calculate_basic)
btn_calc_basic.grid(row=3, column=0, columnspan=2, pady=10)
update_fields()  # ustawienia początkowe

# =========================
# ZAKŁADKA MACIERZE
# =========================
# MACIERZ A
tk.Label(tab_matrix, text="Macierz A - wymiary:").pack(pady=2)
frame_dims = tk.Frame(tab_matrix)
frame_dims.pack()

tk.Label(frame_dims, text="Wiersze:").grid(row=0, column=0)
entry_rows = tk.Entry(frame_dims, width=5)
entry_rows.grid(row=0, column=1)

tk.Label(frame_dims, text="Kolumny:").grid(row=0, column=2)
entry_cols = tk.Entry(frame_dims, width=5)
entry_cols.grid(row=0, column=3)

frame_matrix = tk.Frame(tab_matrix)
frame_matrix.pack(pady=5)
matrix_entries = []

def create_matrix():
    global matrix_entries
    for widget in frame_matrix.winfo_children():
        widget.destroy()
    matrix_entries = []

    try:
        rows = int(entry_rows.get())
        cols = int(entry_cols.get())
        if rows <= 0 or cols <= 0:
            raise ValueError("Wymiary muszą być dodatnie")
    except Exception as e:
        messagebox.showerror("Błąd", str(e))
        return

    tk.Label(frame_matrix, text=f"Wprowadź liczby do macierzy A {rows}x{cols}:").grid(row=0, column=0, columnspan=cols)
    for r in range(rows):
        row_entries = []
        for c in range(cols):
            e = tk.Entry(frame_matrix, width=8)
            e.grid(row=r+1, column=c, padx=2, pady=2)
            row_entries.append(e)
        matrix_entries.append(row_entries)

btn_create_matrix = tk.Button(tab_matrix, text="Stwórz macierz A", command=create_matrix)
btn_create_matrix.pack(pady=5)

def get_matrix_values():
    mat = []
    try:
        for row in matrix_entries:
            mat_row = []
            for e in row:
                val = float(e.get())
                mat_row.append(val)
            mat.append(mat_row)
    except Exception as e:
        messagebox.showerror("Błąd", f"Niepoprawne dane w macierzy A: {e}")
        return None
    return mat

# MACIERZ B
tk.Label(tab_matrix, text="Macierz B - wymiary:").pack(pady=2)
frame_dims_B = tk.Frame(tab_matrix)
frame_dims_B.pack()

tk.Label(frame_dims_B, text="Wiersze:").grid(row=0, column=0)
entry_rows_B = tk.Entry(frame_dims_B, width=5)
entry_rows_B.grid(row=0, column=1)

tk.Label(frame_dims_B, text="Kolumny:").grid(row=0, column=2)
entry_cols_B = tk.Entry(frame_dims_B, width=5)
entry_cols_B.grid(row=0, column=3)

frame_matrix_B = tk.Frame(tab_matrix)
frame_matrix_B.pack(pady=5)
matrix_entries_B = []

def create_matrix_B():
    global matrix_entries_B
    for widget in frame_matrix_B.winfo_children():
        widget.destroy()
    matrix_entries_B = []

    try:
        rows = int(entry_rows_B.get())
        cols = int(entry_cols_B.get())
        if rows <= 0 or cols <= 0:
            raise ValueError("Wymiary muszą być dodatnie")
    except Exception as e:
        messagebox.showerror("Błąd", str(e))
        return

    tk.Label(frame_matrix_B, text=f"Wprowadź liczby do macierzy B {rows}x{cols}:").grid(row=0, column=0, columnspan=cols)
    for r in range(rows):
        row_entries = []
        for c in range(cols):
            e = tk.Entry(frame_matrix_B, width=8)
            e.grid(row=r+1, column=c, padx=2, pady=2)
            row_entries.append(e)
        matrix_entries_B.append(row_entries)

btn_create_matrix_B = tk.Button(tab_matrix, text="Stwórz macierz B", command=create_matrix_B)
btn_create_matrix_B.pack(pady=5)

def get_matrix_values_B():
    mat = []
    try:
        for row in matrix_entries_B:
            mat_row = []
            for e in row:
                val = float(e.get())
                mat_row.append(val)
            mat.append(mat_row)
    except Exception as e:
        messagebox.showerror("Błąd", f"Niepoprawne dane w macierzy B: {e}")
        return None
    return mat

# TextBox do kroków obliczeń
tk.Label(tab_matrix, text="Kroki obliczeń:").pack()
text_steps = tk.Text(tab_matrix, height=15, width=80)
text_steps.pack(pady=5)

# Funkcja dodawania macierzy
def add_matrices():
    A = get_matrix_values()
    B = get_matrix_values_B()
    if not A or not B:
        return

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        messagebox.showerror("Błąd", "Macierze muszą mieć te same wymiary!")
        return

    rows = len(A)
    cols = len(A[0])
    result = []

    text_steps.delete(1.0, tk.END)

    for i in range(rows):
        result_row = []
        for j in range(cols):
            sum_cell = A[i][j] + B[i][j]
            result_row.append(sum_cell)
            text_steps.insert(tk.END, f"A[{i+1},{j+1}] + B[{i+1},{j+1}] = {A[i][j]} + {B[i][j]} = {sum_cell}\n")
        result.append(result_row)

    text_steps.insert(tk.END, f"\nWynikowa macierz:\n")
    for r in result:
        text_steps.insert(tk.END, f"{r}\n")

btn_add_matrices = tk.Button(tab_matrix, text="Dodaj macierze", command=add_matrices)
btn_add_matrices.pack(pady=5)

root.mainloop()
