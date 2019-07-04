# powkładaj z listy wartości do odpowiednich "worków"

import random

owoce = ["jablko"] * 4 + ["pomarancz"] * 3 + ["mandarynka"] * 4 + \
        ["gruszka"] * 3 + ["pomidor"] * 4

random.shuffle(owoce)
print(owoce)

jablka = []
pomarancze = []
mandarynki = []
gruszki = []
pomidory = []

for element in owoce:
    if element == "jablko":
        jablka.append(element)
    if element == "pomarancz":
        pomarancze.append(element)
    if element == "mandarynka":
        mandarynki.append(element)
    if element == "gruszka":
        gruszki.append(element)
    if element == "pomidor":
        pomidory.append(element)

            



print(jablka) 
print(pomarancze) 
print(mandarynki) 
print(gruszki) 
print(pomidory)

#print(f"{pomidory}")







#for jablko in owoce.append(jablka):
#    if pomarancz in owoce.append[pomarancze]:
#        if mandarynka in owoce.append[mandarynki]:
#            if gruszka in owoce.append[gruszki]:
#                if pomidor in owoce.append[pomidory]:






