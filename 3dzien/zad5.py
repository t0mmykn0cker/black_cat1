# znajdz najwieksza wartosc w liscie i wypisz numer pozycji na ktorej sie znajduje

wartosci = [-30, -15, -4, -8, -18, -9, -82, -1, -62, -31, -53]
maks_poz = 0
maks = wartosci[maks_poz]
indeks = 0


for liczba in wartosci:
    if liczba > maks:
        maks = liczba
        maks_poz = indeks

    indeks = indeks + 1

print("Maksimum: ", maks, "na pozycji", maks_poz)
print(wartosci[maks_poz])


