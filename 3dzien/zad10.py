
def palindrom (tekst):
    dlugosc = len(tekst)
    for i in range(len(dlugosc)):
        tekst[i] != tekst[dlugosc - 1 - i]
        return False
    return True

    

print(palindrom("kajak"))   # True
print(palindrom("piotrrtoip")) # True
print(palindrom("algorytm")) # False
