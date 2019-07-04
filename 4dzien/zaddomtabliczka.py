# narysuj tabliczkę mnożenia
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16
# itd.
# postaraj się ładnie to wyświetlać
# użyj znaku "\t" do wyświetlania tabulatora


wiersz = range(1, 11)
kolumna = range(1, 11)

for x_w in wiersz:
    # print(x_w)
    for x_k in kolumna:
        print(x_w * x_k, end='\t')
    print()
    