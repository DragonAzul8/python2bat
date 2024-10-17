import random

#Elegir número
minimo = 1
maximo = 10
numeroElegido = random.randint(minimo,maximo)

#Pedir el número    
numeroPedido = int(input(f"Elige un número entre {minimo} y {maximo}"))
#Comprobar
if numeroElegido == numeroPedido:
    print("Enhorabuena")
else:
    print(f"No has acertado, el número era {numeroElegido}")