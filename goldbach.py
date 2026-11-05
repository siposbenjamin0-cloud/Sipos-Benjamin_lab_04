
# Cerinta 1 - Conjectura lui Goldbach

def este_prim(numar):
    if numar < 2:
        return False

    divizor = 2

    while divizor * divizor <= numar:
        if numar % divizor == 0:
            return False
        divizor += 1

    return True


def descompuneri_goldbach(n):
    for p in range(2, n // 2 + 1):
        q = n - p

        if este_prim(p) and este_prim(q):
            print(f"{n} = {p} + {q}")


def main():
    try:
        n = int(input("Introdu un numar par mai mare decat 2: "))
    except ValueError:
        print("Eroare: introdu un numar natural valid!")
        return

    if n <= 2 or n % 2 != 0:
        print("Eroare: numarul trebuie sa fie par si mai mare decat 2!")
        return

    print("Descompunerile Goldbach sunt:")
    descompuneri_goldbach(n)


if __name__ == "__main__":
    main()
