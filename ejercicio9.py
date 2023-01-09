#crear una lista con todas las cartas del mazo (shuffle-barajear el mazo)
from random import shuffle  

numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
palos = ['espada','basto','copa','oro']

deck = []
for palo in palos:
    for numero in numeros:
        carta = (numero, palo)
        deck.append(carta)
shuffle(deck)

#separar el mazo en cuatro pilas una por cada pal
for carta in deck:
    numero, palo = carta
    piles[palo].append(carta)


#ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente (mediante la funcion sort)
piles['espada'].sort()
piles['basto'].sort()
piles['copa'].sort()
piles['oro'].sort()


