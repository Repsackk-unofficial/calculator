import tkinter as tk
from tkinter import messagebox, ttk
from funkcje.matrix_ops import (
    add_matrices_steps,
    det_2x2_steps,
    det_3x3_steps,
    det_nxN_steps
)

def create_matrix_tab(tab):
    # ----------------------------
    # MACIERZ A
    # ----------------------------
    tk.Label(tab, text="Macierz A - wymiary:").pack(pady=2)
    frame_dims = tk.Frame(tab)
    frame_dims.pack()

    tk.Label(frame_dims, text="Wiersze:").grid(row=0, column=0)
    entry_rows = tk.Entry(frame_dims, width=5)
    entry_rows.grid(row=0, column=1)

    tk.Label(frame_dims, text="Kolumny:").grid(row=0, column=2)
    entry_cols = tk.Entry(frame_dims, width=5)
    entry_cols.grid(row=0, column=3)

    frame_matrix_A = tk.Frame(tab)
    frame_matrix_A.pack(pady=5)
    matrix_entries_A = []

    def create_matrix_A():
        nonlocal matrix_entries_A
        for w in frame_matrix_A.winfo_children():
            w.destroy()
        matrix_entries_A = []

        try:
            rows = int(entry_rows.get())
            cols = int(entry_cols.get())
        except:
            messagebox.showerror("Błąd", "Niepoprawne wymiary!")
            return

        for r in range(rows):
            row_entries = []
            for c in range(cols):
                e = tk.Entry(frame_matrix_A, width=6)
                e.grid(row=r, column=c, padx=2, pady=2)
                row_entries.append(e)
            matrix_entries_A.append(row_entries)

    tk.Button(tab, text="Stwórz macierz A", command=create_matrix_A).pack(pady=5)

    # ----------------------------
    # MACIERZ B (dla dodawania)
    # ----------------------------
    tk.Label(tab, text="Macierz B (tylko przy dodawaniu)").pack(pady=2)
    frame_matrix_B = tk.Frame(tab)
    frame_matrix_B.pack(pady=5)
    matrix_entries_B = []

    def create_matrix_B():
        nonlocal matrix_entries_B
        for w in frame_matrix_B.winfo_children():
            w.destroy()
        matrix_entries_B = []

        try:
            rows = int(entry_rows.get())
            cols = int(entry_cols.get())
        except:
            messagebox.showerror("Błąd", "Niepoprawne wymiary!")
            return

        for r in range(rows):
            row_entries = []
            for c in range(cols):
                e = tk.Entry(frame_matrix_B, width=6)
                e.grid(row=r, column=c, padx=2, pady=2)
                row_entries.append(e)
            matrix_entries_B.append(row_entries)

    tk.Button(tab, text="Stwórz macierz B", command=create_matrix_B).pack(pady=5)

    # ----------------------------
    # Text - kroki
    # ----------------------------
    text_steps = tk.Text(tab, height=15, width=80)
    text_steps.pack(pady=5)

    # ----------------------------
    # Combobox wyboru operacji
    # ----------------------------
    tk.Label(tab, text="Wybierz operację:").pack(pady=5)
    combo_op = ttk.Combobox(tab, values=[
        "Dodawanie macierzy",
        "Wyznacznik 2x2",
        "Wyznacznik 3x3",
        "Wyznacznik NxN"
    ])
    combo_op.current(0)
    combo_op.pack(pady=5)

    # ----------------------------
    # Funkcje pomocnicze
    # ----------------------------
    def read_matrix(entries):
        return [[float(e.get()) for e in row] for row in entries]

    def execute_operation():
        try:
            A = read_matrix(matrix_entries_A)
            op = combo_op.get()
            text_steps.delete(1.0, tk.END)

            if op == "Dodawanie macierzy":
                B = read_matrix(matrix_entries_B)
                result, steps = add_matrices_steps(A, B)
                for s in steps:
                    text_steps.insert(tk.END, s + "\n")
                text_steps.insert(tk.END, "\nWynik:\n")
                for r in result:
                    text_steps.insert(tk.END, f"{r}\n")

            elif op == "Wyznacznik 2x2":
                det, steps = det_2x2_steps(A)
                for s in steps:
                    text_steps.insert(tk.END, s + "\n")
                text_steps.insert(tk.END, f"\nWyznacznik = {det}")

            elif op == "Wyznacznik 3x3":
                det, steps = det_3x3_steps(A)
                for s in steps:
                    text_steps.insert(tk.END, s + "\n")
                text_steps.insert(tk.END, f"\nWyznacznik = {det}")

            elif op == "Wyznacznik NxN":
                det, steps = det_nxN_steps(A)
                for s in steps:
                    text_steps.insert(tk.END, s + "\n")
                text_steps.insert(tk.END, f"\nWyznacznik = {det}")

        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    tk.Button(tab, text="Wykonaj", command=execute_operation).pack(pady=10)
