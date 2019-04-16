slownik = {'klucz1':'wartosc1','klucz2':'wartosc2'}

# Utworz sklownik o nazwie pracownik zawierajacy klucze:
# imie, nazwisko, miasto, wiek, imionaDzieci, imionaRodzicow

pracownik ={
    'imie':'',
    'nazwisko':'',
    'miasto':'',
    'wiek':'',
    'imionaDzieci':[],
    'imionaRodzicow':[]
}

pracownik['imie']='jaroslaw'
pracownik['nazwisko']='smorawa'
pracownik['miasto']='gdynia'
pracownik['wiek']=42
pracownik['imionaDzieci'].append('Mariusz')
pracownik['imionaDzieci'].append('Daniel')
pracownik['imionaRodzicow'].append('Mariola')
pracownik['imionaRodzicow'].append('Antioni')

print(pracownik)

pracownik['wzrost'] = 175
pracownik['waga'] = 75

print(pracownik)

klucz = 'wiek'

pracownik1 ={
    'imie':'Anna',
    'nazwisko':'Kazimierkowa',
    'miasto':'Gdynia',
    'wiek':'43',
    'imionaDzieci':['Blazej','Martyna'],
    'imionaRodzicow':['Magda','Janusz']
}

print(pracownik1)

if klucz in pracownik1:
    del pracownik1[klucz]
    print(f'klucz {klucz} zostal usuniety')
else:
    print(f'klucz {klucz} nie zostal usuniety')

print(pracownik1)
print(pracownik1.keys())
print(pracownik1.values())
print(list(pracownik1.values()))
print(pracownik1.items())

for value in pracownik1.values():
    print(value, end=' ')

for key, value in pracownik1.items():
    print(f'{key}:{value}')