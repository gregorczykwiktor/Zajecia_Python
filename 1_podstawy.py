print("CDV")
print(2)
print("kaczucha")

#potega
potega = 2 ** 10

tekst= "CDV"
print(tekst*2)

#pobieranie danych z klawiatury
imie=input()
print("twoje imie:" + imie)

nazwisko=input()
print("twoje imie:" + imie + "twoje nazwisko:" + nazwisko)

dlugosc = len(nazwisko)
print(type(nazwisko))
print(type(dlugosc))
print("dlugosc nazwiska: ", dlugosc)
dlugosc = str(dlugosc) #konwersja typu danych z int na string
print("dlugosc nazwiska: " + dlugosc)

#uzytkownik wpisauje z klawiatury swoj wiek,
#wyswietl dane w formacie: twoj wiek: ... lat

print("\nPodaj swój wiek: ", end="")
wiek=input()
#print("Twój wiek: ", wiek, " lat.")
print("Twój wiek: " + wiek + " lat.")

pierwszyZnak = nazwisko[0]
print(pierwszyZnak)

ostatniZnak = nazwisko[len(nazwisko)-1]
print(ostatniZnak)
ostatniZnak = nazwisko[-1]
print(ostatniZnak)

#konwerjsa
x="5"
print(type(x)) #str
x = int(x)
print(type(x)) #int

y = 4
print(type(y)) #int
y = y / 2
print(type(y)) #float

wiek = 21
print("Twój wiek: ", wiek)
wiek = str(wiek)
print("Twój wiek: " + wiek)

nazwisko = "Kowalski"
print(nazwisko[0]) #k
print(nazwisko[0:3]) #kow


