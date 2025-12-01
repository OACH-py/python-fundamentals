import random 
import os

def limpiar_pantalla ():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def juego_ahorcado():
    palabras = [
    "python", "ingenieria", "teclado", "servidor", "codigo", 
    "algoritmo", "sistema", "linux", "fedora", "programa", 
    "pantalla", "dato", "variable", "nube", "redes"
    ]

    vida = 5
    palabra_secreta = random.choice(palabras).upper()
    letras_usadas = set()

    progreso = ["_"] *len(palabra_secreta)

    while vida > 0:
        limpiar_pantalla()
        print(f"Vidas:{vida}")
        print(f"Letras ya usadas: {letras_usadas}")
        print(" ".join(progreso))


        if "_" not in progreso:
            print("Ganaste!!!")
            break
        
        letra = input("Intoduce una letra:\n").upper()

        if len(letra)!=1 or not letra.isalpha():
            print("Ingresa un valor valido")
            input("Precione ENTER para continuar")
            continue
        if letra in letras_usadas:
            print(f"Ya usaste esta letra")
            input("recione ENTER para continuar")
            continue

        letras_usadas.add(letra)

        if letra in palabra_secreta:
            for indice, char_secreto in enumerate(palabra_secreta):
                if char_secreto == letra:
                    progreso[indice] = letra
        else:
            vida -= 1

    if vida == 0:
            limpiar_pantalla()
            print(f"Vidas: {vida}")
            print(" ".join(progreso))
            print(f"\nGame Over. La palabra secreta era: {palabra_secreta}")  
juego_ahorcado()