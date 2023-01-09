#prioridad del pedido 
def prioridad (nombre,multiverso,descripcion):
    if nombre == 'Gran conquistador' or multiverso == '616' or descripcion== 'el que permanece'
    return "alta"

    elif nombre == 'Khan que todo lo sabe' or multiverso == '838' or '' descripcion == 'Carnicero de Dioses'
    return "media"

    else:
        return "baja"

#almacenar los pedidos de mayor prioridad en una pila llamada “bitácora” 
from heapq import heapify, heappush #algoritmo de monticulos (ordena en prioridad)

cola_prioridad = []
heapify(cola_prioridad) 

heappush(cola_prioridad, Pedido("Gran Conquistador", "616", "Necesito sugerencias para vencer al Infinito"))
heappush(cola_prioridad, Pedido("Khan que todo lo sabe", "838", "Carnicero de Dioses está causando estragos en mi multiverso"))
heappush(cola_prioridad, Pedido("Khan X", "999", "Necesito ayuda para proteger a mi pueblo"))

#bitcora 
bitcora = []

while cola_prioridad:
    pedido = heappop (cola_prioridad) #saco el mayor prioridad
    bitcora.append(pedido) #añado el pedido a bitcora 

    