def suma (variable1,variable2):
    try:
        return variable1 + variable2
    except TypeError:
        print ("Error")

def resta (variable1,variable2):
    try:
        return variable1 - variable2
    except TypeError:
        print ("Error")

def multiplicacion (variable1,variable2):
    try:
        return variable1 * variable2
    except TypeError:
        print ("Error")

def division (variable1,variable2):
    try:
        return variable1 / variable2
    except TypeError:
        print ("Error")
    
    except ZeroDivisionError: 
        print("error, no se puede dividir entre cero")