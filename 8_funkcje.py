def witaj():
    print('Witaj Janusz!')

witaj()

def wyswietlWiek(wiek):
    print('Twoj wiek: ',wiek)

wyswietlWiek(23)

def iloczyn(a, b):
    return a * b

print(iloczyn(3, 4))

def iloraz(a, b):
    return a / b

iloraz1 = iloraz(3, 4)
print(iloraz1)
print(type(iloraz1))

print(iloraz(b=5, a=2))

# Uzytkownik podaje z klawiatury:
# marka, model, pojemnosc, predkoscMax
# utowrz funkcje, ktora pobierze od uzytkownika i przypisze do slownika
# utworz druga funkcje wyswietlajaca dane w formacie:
# Marka:...
# Model:...

auto={
    'marka':'',
    'model':'',
    'pojemnosc':'',
    'predkoscMax':''
}

print(type(auto['marka']))

def wprowadz():
    auto['marka'] = input('Marka: ')
    auto['model'] = input('Model: ')
    auto['pojemnosc'] = input('Pojemnosc: ')
    auto['predkoscMax'] = input('PredkoscMax: ')

wprowadz()

print(auto)




