
wszystkie_liczby = set(range(3, 101))
np = [] # lista liczb nie-pierwszych
# liczba = 17 # przykladowa liczba do sprawdzenia

for liczba in range(3, 101):
    for potencjalny_dzielnik in range(2,liczba): # range zwraca liste o 1!!!! mniejsza - listy zaczynaja sie od pozycji 0
        if liczba % potencjalny_dzielnik == 0:
        # liczba dzieli sie bez reszty przez potecjalny dzielnik
        # a zatem nie jest liczba pierwsza
            np.append(liczba)
            break

liczby_niepierwsze = set(np)

liczby_pierwsze = wszystkie_liczby - liczby_niepierwsze

print(sorted(liczby_pierwsze)) # zbiory moga byc nie sortowane - dlatego z komenda sort

