import random 
import os
palabras = [
    "python", "ingenieria", "teclado", "servidor", "codigo", 
    "algoritmo", "sistema", "linux", "fedora", "programa", 
    "pantalla", "dato", "variable", "nube", "redes"
]

intentos = 3
palabra_secreta = random.choice(palabras)

for i in palabra_secreta:
    length 