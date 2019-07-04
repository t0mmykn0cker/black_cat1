# import random

# print("Witaj w zgadywajce :) Naciśnij ENTER aby kontynuować")

# contin = input()

# print("Zasady: Program losuje jedną liczbę z zakresu od 1 do 1000. "
#       "Twoim zadaniem jest odgadnięcie co to za liczba w jak najmniejszej ilości kroków")

# print("Naciśnij ENTER aby przejść dalej")
# contin = input()

# i = 0
# i = int(i)

# print("Trwa losowanie liczby...")

# losowa = random.randint(1,100)

# print("Liczba została wylosowana")

# print("Podaj liczbę:")
# x = input()
# x = int(x)

# while losowa != x:
#     if x > losowa:
#         i += 1
#         print("Twoja liczba jest za duża!")
#         print("Podaj liczbę:")
#         x = input()
#         x = int(x)
#     else:
#         i += 1
#         print("Twoja liczba jest za mała!")
#         print("Podaj liczbę:")
#         x = input()
#         x = int(x)

# if losowa == x:
#     i += 1
#     print("Udało się :)")
#     print("Szukana liczba to: ")
#     print(losowa)
#     print("Ilość prób: ")
#     print(i)

# print("Koniec")


# algorytmy O(n2), O(nlogn), O(logn)


import random

print("Zgadnij jaką liczbę zakresu od 1-100 dla Ciebie mam...")
liczba = random.randint(1, 101)
zgadl = False

x = 1

while not zgadl:   #rozwin warunek dla while
    zgadywana = int(input("podaj liczbe: ")) 

    x =+ x + 1

    if zgadywana == liczba:   
        print("Brawo, udało Ci się")
    
    elif zgadywana > liczba:
        print("za dużo")
    
    elif zgadywana < liczba:
        print("za mało")
        elif x = 7:
            print("Game Over")
        break





# import random
# print("Zagrajmy w grę, jaką? TumbRajder zgadnij jaka ta liczba?")
# print("masz tylko 7 szans, nie zmarnuj ich")
# liczba = random.randint(0,101)
# proba = 1

# zgadl = False
# while not zgadl:
#     zgadywana = int(input("Podaj liczbe: "))
#     proba =+ proba + 1
#     # pass
#     if zgadywana == liczba:
#         zgadl = True
#         print("Dobrze!")
#     elif proba == 8:
#         print("No, no... 7 razy strzelać i nie trafić... Jesteś godnym następcą Milika")
#         break
#     elif zgadywana < liczba:
#         print("Za mało, mierz wyżej!")
#     elif zgadywana > liczba:
#         print("Ale Cię poniosło! Obniż loty!")
































