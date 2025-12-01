import random 
import os


def juego_ahorcado():
    palabras = [
    "python", "ingenieria", "teclado", "servidor", "codigo", 
    "algoritmo", "sistema", "linux", "fedora", "programa", 
    "pantalla", "dato", "variable", "nube", "redes"
    ]

    vida = 5
    palabra_secreta = random.choice(palabras).upper()
    
    progreso = ["_"] *len(palabra_secreta)

    while vida > 0:
        os.system('clear') # esto depende de OS del usuario
        print(f"Vidas:{vida}")
        print(progreso)
        if "_" not in progreso:
            print("Ganaste!!!")
            break
        
        letra = input("Intoduce una letra:\n").upper()

        if len(letra)!=1 or not letra.isalpha():
            print("Ingresa un valor valido")
            input("Precione ENTER para continuar")
            continue
        
        if letra in palabra_secreta:
            for indice, char_secreto in enumerate(palabra_secreta):
                if char_secreto == letra:
                    progreso[indice] = letra
        else:
            vida -= 1
        if vida == 0:
            print(f"La palabra secreta es: {palabra_secreta}")
                
juego_ahorcado()