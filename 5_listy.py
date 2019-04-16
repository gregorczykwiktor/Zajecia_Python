# [] - listy
# () -
# {} - slowniki

programowanie = ['python','php','csharp','js','java']
print(type(programowanie))

pierwszy = programowanie[0]
print(pierwszy)

trzyElementy = programowanie[0:3]
print(trzyElementy)

ostatniElement = programowanie[-1]
print(ostatniElement)

# Dodanie nowego elementu na koniec listy

programowanie.append('R')
programowanie.append('Python')
print(programowanie)

#zliczanie elementow w liscie
ile = programowanie.count('Python')
print(ile)

# ilosc elementow
iloscElem = len(programowanie)
print(iloscElem)

# polaczenie list
inneJezyki = ['c','c++']
programowanie.extend(inneJezyki)
print(programowanie)

#czyszczenie list
nowa = programowanie
print('lista nowa:' ,end='')
print(nowa)
# nowa.clear()
print('Lista nowa:' ,end='')
