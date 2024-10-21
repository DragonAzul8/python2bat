#Pensar palabra
#Escribir _____
#Pedir letra
#Buscar si está en la palabra
    #Si --> escribir ____a____
    #NO --> quitar intentos -1
#(while)
palabraSecreta = "perro"

letrasCorrectas = []
letrasIncorrectas = []

seguirJugando = True

while seguirJugando == True:
    for letra in palabraSecreta:
        if letra in letrasCorrectas:
            print(letra, end = "")
        else :
            print('_', end = "")

    letraPedida = input("Dime una letra\n")

    if letraPedida in palabraSecreta:
        letrasCorrectas.append(letraPedida)
    else:
        letrasIncorrectas.append(letraPedida)
    print(f"correctas:{letrasCorrectas}")
    print(f"incorrectas:{letrasIncorrectas}")

    if set(letrasCorrectas) == set(palabraSecreta):
        seguirJugando = False
        print("Has ganado")

    if len(letrasIncorrectas) == 6:
        seguirJugando = False
        print("Has perdido") 
        print("La palabra era:", palabraSecreta)