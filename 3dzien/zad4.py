liczby = range(1,101)
for liczba in liczby:
    if liczba % 15 == 0:
        print(liczba, "jest podzielna przez 15")
    elif liczba % 3 == 0:
        print(liczba, "jest podzielna przez 3")
    elif liczba % 5 == 0:
        print(liczba, "jest podzielna przez 5")


