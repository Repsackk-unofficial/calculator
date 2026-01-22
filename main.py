import funkcje as f
import time

def menu():
    print("\n===== KALKULATOR STUDENCKI =====")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")
    print("6. Pierwiastkowanie")
    print("7. Losowanie liczby")
    print("8. Silnia")
    print("9. Logarytm")
    print("20. Dodawanie macierzy")
    print("21. Mnożenie macierzy")
    print("22. Wyznacznik macierzy")
    print("0. Wyjście")

while True:
    menu()
    choice = input("Wybierz opcję: ")

    try:
        # ====================
        # PODSTAWOWE DZIAŁANIA
        # ====================
        if choice == "1":
            a = float(input("a: "))
            b = float(input("b: "))
            print("Wynik:", f.add(a, b))

        elif choice == "2":
            a = float(input("a: "))
            b = float(input("b: "))
            print("Wynik:", f.subtract(a, b))

        elif choice == "3":
            a = float(input("a: "))
            b = float(input("b: "))
            print("Wynik:", f.multiply(a, b))

        elif choice == "4":
            a = float(input("a: "))
            b = float(input("b: "))
            print("Wynik:", f.divide(a, b))

        elif choice == "5":
            a = float(input("a: "))
            b = float(input("b: "))
            print("Wynik:", f.power(a, b))

        elif choice == "6":
            a = float(input("a: "))
            print("Wynik:", f.sqrt(a))

        # ====================
        # INNE
        # ====================
        elif choice == "7":
            start = int(input("Początek zakresu: "))
            end = int(input("Koniec zakresu: "))
            print("Wylosowana liczba:", f.random_number(start, end))

        elif choice == "8":
            n = int(input("Podaj n: "))
            print("Wynik:", f.factorial(n))

        elif choice == "9":
            a = float(input("Podaj a: "))
            base = input("Podaj podstawę logarytmu (ENTER = 10): ")
            base = float(base) if base else 10
            print("Wynik:", f.logarithm(a, base))

        # ====================
        # MACIERZE
        # ====================
        elif choice == "20":
            print("MACIERZ A:")
            A = f.read_matrix()
            print("MACIERZ B:")
            B = f.read_matrix()
            C, steps = f.add_matrices_steps(A, B)
            print("\n--- KROK PO KROKU ---")
            for s in steps:
                print(s)
            print("\nWYNIK:")
            f.print_matrix(C)

        elif choice == "21":
            print("MACIERZ A:")
            A = f.read_matrix()
            print("MACIERZ B:")
            B = f.read_matrix()
            C, steps = f.multiply_matrices_steps(A, B)
            print("\n--- KROK PO KROKU ---")
            for s in steps:
                print(s)
            print("\nWYNIK:")
            f.print_matrix(C)

        elif choice == "22":
            print("PODAJ MACIERZ:")
            A = f.read_matrix()
            if len(A) == 2 and len(A[0]) == 2:
                det, steps = f.det_2x2_steps(A)
            elif len(A) == 3 and len(A[0]) == 3:
                det, steps = f.det_3x3_steps(A)
            else:
                print("Obsługiwane tylko macierze 2×2 i 3×3")
                continue

            print("\n--- KROK PO KROKU ---")
            for s in steps:
                print(s)
            print("\nWYNIK:")
            print("det =", det)

        # ====================
        # WYJŚCIE
        # ====================
        elif choice == "0":
            print("Do zobaczenia!")
            break

        else:
            print("Niepoprawny wybór, spróbuj jeszcze raz.")

        print("\n==============================\n")
        time.sleep(0.5)

    except Exception as e:
        print("Błąd:", e)
        print("\n==============================\n")
        time.sleep(0.5)
