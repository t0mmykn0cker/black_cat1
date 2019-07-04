
import random

print("Zgadnij jaką liczbę zakresu od 1-100 dla Ciebie mam...")
print("Masz tylko 7 prób")
liczba = random.randint(1, 101)
zgadl = False

x = 1

while not zgadl:   #rozwin warunek dla while
    zgadywana = int(input("podaj liczbe: ")) 

    x += 1

    if zgadywana == liczba:   
        print("Brawo, udało Ci się")
        break

    elif x == 7:
        print("Game Over")
        break


    elif zgadywana > liczba:
        print("za dużo")
    
    elif zgadywana < liczba:
        print("za mało")
