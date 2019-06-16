'''
    podaj wartość początkową i końcową ktora bedzie wypisana
    w porządku malejącym
'''

war1 = int(input("Podaj wartosc poczatkowa: "))
war2 = int(input("Podaj wartosc koncowa: "))

for zmienna in range(war1, war2+1):
    print(zmienna, end="  ")