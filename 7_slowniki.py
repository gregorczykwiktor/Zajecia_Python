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
