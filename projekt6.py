'''
uzytkownik podaje z klawiatury haslo
"okon" poprawne
max 3 proby
'''

haslo = "okon"

for i in  range (0,3):
    zmienna = input("Podaj haslo: ")
    if zmienna != haslo:
        print("Złe hasło.")
    else:
        print("Hasło poprawne.")
        break

