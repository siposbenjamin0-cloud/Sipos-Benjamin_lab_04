# Cerinta 2 - Adunarea si inmultirea numerelor mari

from pathlib import Path


# Adunarea numerelor mari
def adunare(a, b):
    lungime = max(len(a), len(b))
    a = a.zfill(lungime)
    b = b.zfill(lungime)

    transport = 0
    rezultat = ""

    for i in range(lungime - 1, -1, -1):
        suma = int(a[i]) + int(b[i]) + transport
        rezultat = str(suma % 10) + rezultat
        transport = suma // 10

    if transport:
        rezultat = str(transport) + rezultat

    return rezultat.lstrip("0") or "0"


# Inmultirea numerelor mari
def inmultire(a, b):
    rezultat = [0] * (len(a) + len(b))

    for i in range(len(a) - 1, -1, -1):
        transport = 0

        for j in range(len(b) - 1, -1, -1):
            poz = i + j + 1
            produs = int(a[i]) * int(b[j])
            total = produs + rezultat[poz] + transport

            rezultat[poz] = total % 10
            transport = total // 10

        rezultat[i] += transport

    rezultat = "".join(str(c) for c in rezultat)

    return rezultat.lstrip("0") or "0"


# Citirea numerelor din fisier
try:
    cale = Path(__file__).with_name("numere.txt")

    with open(cale, "r", encoding="utf-8") as fisier:
        numere = [linie.strip() for linie in fisier]

    if len(numere) != 2:
        raise ValueError("Fisierul trebuie sa contina doua numere!")

    for numar in numere:
        if not numar or len(numar) > 200:
            raise ValueError("Numerele trebuie sa aiba maximum 200 de cifre!")

        if any(c not in "0123456789" for c in numar):
            raise ValueError("Fisierul trebuie sa contina doar numere naturale!")

    a, b = numere

    print("Suma:", adunare(a, b))
    print("Produsul:", inmultire(a, b))

except FileNotFoundError:
    print("Eroare: fisierul numere.txt nu exista!")

except ValueError as eroare:
    print("Eroare:", eroare)
