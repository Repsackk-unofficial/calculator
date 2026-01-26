def add_matrices_steps(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Macierze muszą mieć te same wymiary!")

    C = []
    steps = []

    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            val = A[i][j] + B[i][j]
            steps.append(
                f"A[{i+1},{j+1}] + B[{i+1},{j+1}] = {A[i][j]} + {B[i][j]} = {val}"
            )
            row.append(val)
        C.append(row)

    return C, steps
def det_2x2_steps(A):
    if len(A) != 2 or len(A[0]) != 2:
        raise ValueError("Macierz musi być 2×2")

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
    if len(A) != 3 or len(A[0]) != 3:
        raise ValueError("Macierz musi być 3×3")

    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]

    pos = a*e*i + b*f*g + c*d*h
    neg = c*e*g + b*d*i + a*f*h

    steps = [
        "Wyznacznik macierzy 3×3 (reguła Sarrusa):",
        "",
        f"{a}·{e}·{i} + {b}·{f}·{g} + {c}·{d}·{h}",
        f"{c}·{e}·{g} + {b}·{d}·{i} + {a}·{f}·{h}",
        "",
        f"Suma dodatnia = {pos}",
        f"Suma ujemna = {neg}",
        f"det = {pos} − {neg} = {pos - neg}"
    ]

    return pos - neg, steps
def det_nxN_steps(A, level=0):
    """
    Oblicza wyznacznik dowolnej macierzy NxN metodą Laplace'a
    Zwraca:
        det - wartość wyznacznika
        steps - lista kroków opisujących obliczenia
    """
    n = len(A)
    if n != len(A[0]):
        raise ValueError("Macierz musi być kwadratowa!")

    indent = "    " * level  # wcięcie w krokach
    steps = []

    # przypadki bazowe
    if n == 1:
        steps.append(f"{indent}Wyznacznik macierzy 1x1: {A[0][0]}")
        return A[0][0], steps

    if n == 2:
        det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
        steps.append(f"{indent}Wyznacznik 2x2: |{A[0][0]} {A[0][1]}| |{A[1][0]} {A[1][1]}| = {det}")
        return det, steps

    det_total = 0
    steps.append(f"{indent}Rozwinięcie względem pierwszego wiersza:")

    for j in range(n):
        # tworzymy macierz mniejszą usuwając pierwszy wiersz i kolumnę j
        minor = [row[:j] + row[j+1:] for row in A[1:]]
        cofactor = ((-1) ** j) * A[0][j]

        det_minor, minor_steps = det_nxN_steps(minor, level + 1)

        det_total += cofactor * det_minor

        steps.append(f"{indent}A[0][{j}] = {A[0][j]}, współczynnik = {cofactor}, det(minor) = {det_minor}, wkład = {cofactor * det_minor}")

        for s in minor_steps:
            steps.append(s)

    steps.append(f"{indent}Wyznacznik całej macierzy = {det_total}")
    return det_total, steps