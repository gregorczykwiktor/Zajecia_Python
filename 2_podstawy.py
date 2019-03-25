tekst = "Anna, Paweł, Tomek"

tab = tekst.split(", ")

print(tekst)
print(tab)
print(type(tab)) #list

imie1 = tab[0]
print(imie1) #Anna

print("Twoje imie: " + imie1)

imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie1.lower()
print(imieMale)

#sprawdzenie zawartosci
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc)
print(type(zawartosc)) #zmienna bool

nazwisko = ""
zawartosc = nazwisko.isalpha()
print(zawartosc)


imie = "Julia"
print("\nDane uzytkownika \nMasz na imie: ", imie)

text1 = "Jan\n"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip() #czyszczenie bialych znaków
print(text1 + text2)

#wyswietlanie lancuchow znakow

#wszystkie wersje pythona
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze werscje pythona >2.6

text = "{0}, Java i {1}".format("PHP","Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisanie danych

rok = "2019"
miesiac = "marzec"
dzien = 25

#print("Data: ")
#print(dzien, miesiac, rok)

print("Data: ", end="")
print(dzien, miesiac, rok, sep="-")









print()
