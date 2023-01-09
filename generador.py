#número >= que ini y <= que fin.

import random 
import math 

def leer_numero (ini,fin,mensaje)
while True: 
    try: 
        num = int(input(mensaje))
        return num 
    
def generador(): #funcion sin parametros 
    numeros = leer_numeros(1,20, "¿Cuantos números quieres generar? [1-20]")
    modo = leer_numero(1,3,"¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal:")
    redondeados = [] #rendondea los numeros anteriores
    for i in range numeros: 
        num = random.uniform(0,100) #uniform devuelve un numero aleatorio entre 0 y 100
        if modo == 4:
            redondeado = math.ceil #redondeo hacia arriba 
        elif modo == 1:
            redondeado = round(num)
    redondeados.append(redondeado)
    print(f"{num}{redondeado}")
  return redondeados

generador()





