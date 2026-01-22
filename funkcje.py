# ===============================
# FUNKCJE MATEMATYCZNE – KALKULATOR STUDENCKI
# ===============================

import math
import random

# ===============================
# PODSTAWOWE DZIAŁANIA
# ===============================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero!")
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError("Pierwiastek z liczby ujemnej!")
    return math.sqrt(a)

# ===============================
# INNE
# ===============================

def random_number(start, end):
    return random.randint(start, end)

def factorial(n):
    if n < 0:
        raise ValueError("Silnia z liczby ujemnej!")
    return math.factorial(n)

def logarithm(a, base=10):
    if a <= 0:
        raise ValueError("Logarytm z liczby ≤ 0!")
    return math.log(a, base)

# ===============================
# MACIERZE – NARZĘDZIA
# ===============================

def read_matrix():
    rows = int(input("Podaj liczbę wierszy: "))
    cols = int(input("Podaj liczbę kolumn: "))

    matrix = []

    print("Podaj wiersze macierzy (liczby oddzielone spacją):")
    for i in range(rows):
        row = list(map(float, input(f"Wiersz {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError("Zła liczba elementów w wierszu!")
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("|", "  ".join(f"{x:6.2f}" for x in row), "|")
        
# ===============================
# MACIERZE – DZIAŁANIA
# ===============================

def add_matrices_steps(A, B):
    rows = len(A)
    cols = len(A[0])
    steps = []
    C = []

    steps.append("Dodawanie macierzy: C[i][j] = A[i][j] + B[i][j]\n")

    for i in range(rows):
        row = []
        for j in range(cols):
            steps.append(
                f"C[{i+1}][{j+1}] = {A[i][j]} + {B[i][j]} = {A[i][j] + B[i][j]}"
            )
            row.append(A[i][j] + B[i][j])
        C.append(row)

    return C, steps

def multiply_matrices_steps(A, B):
    steps = []
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        raise ValueError("Nieprawidłowe wymiary macierzy!")

    C = [[0]*cols_B for _ in range(rows_A)]
    steps.append("Mnożenie macierzy: C[i][j] = Σ A[i][k]·B[k][j]\n")

    for i in range(rows_A):
        for j in range(cols_B):
            parts = []
            for k in range(cols_A):
                parts.append(f"{A[i][k]}·{B[k][j]}")
                C[i][j] += A[i][k] * B[k][j]
            steps.append(
                f"C[{i+1}][{j+1}] = " + " + ".join(parts) + f" = {C[i][j]}"
            )

    return C, steps

# ===============================
# WYZNACZNIKI
# ===============================

def det_2x2_steps(A):
    a, b = A[0]
    c, d = A[1]

    steps = [
        "Wyznacznik macierzy 2×2:",
        f"| {a}  {b} |",
        f"| {c}  {d} |",
        "",
        "det = a·d − b·c",
        f"det = {a}·{d} − {b}·{c}",
        f"det = {a*d} − {b*c}",
        f"det = {a*d - b*c}"
    ]

    return a*d - b*c, steps

def det_3x3_steps(A):
    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]

    positive = a*e*i + b*f*g + c*d*h
    negative = c*e*g + b*d*i + a*f*h

    steps = [
        "Wyznacznik macierzy 3×3 (reguła Sarrusa):",
        "",
        f"{a}·{e}·{i} + {b}·{f}·{g} + {c}·{d}·{h}",
        f"{c}·{e}·{g} + {b}·{d}·{i} + {a}·{f}·{h}",
        "",
        f"Suma dodatnia = {positive}",
        f"Suma ujemna = {negative}",
        f"det = {positive} − {negative} = {positive - negative}"
    ]

    return positive - negative, steps