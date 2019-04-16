# listy
imiona = ['Julia','Anna','Krystyna']
print(type(imiona))
imiona.append('Janusz')
ilosc = len(imiona)
# print(f'Ilosc imion: {ilosc}')
print('Ilosc imion: ',ilosc)

# tuple
nazwiska = ('Kowalski','Nowak')
print(type(nazwiska))
print(nazwiska)
# nazwiska.append('test')

# slowniki
osoba = {
    'imie':'Julia',
    'nazwisko':'Nowak',
    'wiek':23
}

print(osoba)
print(type(osoba))
print(osoba[nazwisko])
print(osoba.keys())
print(osoba.get('wzrost','Brak danych'))
print(osoba.get('imie','Brak danych'))

