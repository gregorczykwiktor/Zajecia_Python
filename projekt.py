print("Operacje matematyczne.")

def potega(a):
    return a ** 2

print(potega(int(input("Podaj liczbe której chcesz otrzymac potęge."))))

def podajTekst(tekst):
    print(len(tekst))

podajTekst(input("Podaj tekst: "))

dlugoscv2 = input("Podaj tekst: ")
print(len(dlugoscv2))

zmienna = input("Podaj value: ")
print(type(zmienna))
zmienna = int(zmienna)
print(type(zmienna))

imie = "Wiktor"
nazwisko = "Gregorczyk"

print("Twoje imie to: "+ imie + "\nTwoje nazwisko to: "+ nazwisko)

pierwszyZnak = nazwisko[0]
ostatniZnak = nazwisko[-1]

print("Pierwsza litera to: "+ pierwszyZnak + "\nOstatni znak to: " + ostatniZnak)

bezPoczatkuKonca = nazwisko[1:-1]

print("Bez początkowej i końcowej: " + bezPoczatkuKonca)

zawartosc = "Kaczucha.Małpka.Trawnik"
tab = zawartosc.split(".")

print(zawartosc)
print(tab)
print(type(tab))

zawartosc1 = input("Podaj tekst: ")
print(zawartosc1.upper())
print(zawartosc1.lower())
