
# Cerinta 1 - Conjectura lui Goldbach

def este_prim(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


try:
    n = int(input("Introdu un numar par mai mare decat 2: "))

    if n <= 2 or n % 2 != 0:
        print("Eroare: introdu un numar par mai mare decat 2!")
    else:
        print("Descompunerile Goldbach:")

        for p in range(2, n // 2 + 1):
            q = n - p

            if este_prim(p) and este_prim(q):
                print(n, "=", p, "+", q)

except ValueError:
    print("Eroare: introdu un numar natural valid!")
