# narysuj tabliczkę mnożenia
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16
# itd.
# postaraj się ładnie to wyświetlać
# użyj znaku "\t" do wyświetlania tabulatora


# zadanie domowe o ŚREDNICH !!!!
X = [1, 2, 5, 7122, 34, 6, 123, 3]


iloczyn = 1
liczba_el = 0

for el in X:                        # dla kazdego elementu w X wykonaj
    iloczyn = iloczyn * el          # po kazdym obrocie FOR'a pomnoz przez element
    liczba_el = liczba_el + 1       # po kazdym obrocie FOR'a zwieksz element o 1





print(iloczyn, sum(X))
print(liczba_el, len(X))
print(iloczyn ** (1/liczba_el))     # zapis PIERWISATKOWANIA do pierwiastka z nieokreślonym stopniem (2 stopnia, 3 stopnia, 4 stopnia itd.)


suma_odwr = 0
liczba_el = 0

for el in X:
    suma_odwr = suma_odwr + (1/el)
    liczba_el = liczba_el + 1

print(suma_odwr, sum(X))
print(liczba_el, len(X))
