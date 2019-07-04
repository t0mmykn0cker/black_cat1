
wartosci = [30, -15, -4, -8, -18, -9, -82, -1, -62, -31, -53]
maks_poz = 0
maks = wartosci[maks_poz]

for indeks, liczba in enumerate(wartosci):
    if liczba > maks:
        maks = liczba
        maks_poz = indeks

print("Maksimum: ", maks, "na pozycji", maks_poz)
print(wartosci[maks_poz])
