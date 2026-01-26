import tkinter as tk
from tkinter import ttk

from gui.basic_tab import create_basic_tab
from gui.matrix_tab import create_matrix_tab

root = tk.Tk()
root.title("Kalkulator Studencki")
root.geometry("900x700")

tabControl = ttk.Notebook(root)

tab_basic = ttk.Frame(tabControl)
tab_matrix = ttk.Frame(tabControl)

tabControl.add(tab_basic, text="Podstawowe działania")
tabControl.add(tab_matrix, text="Macierze")
tabControl.pack(expand=1, fill="both")

create_basic_tab(tab_basic)
create_matrix_tab(tab_matrix)

root.mainloop()
