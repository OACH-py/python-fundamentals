import random

num_secreto = random.randint(1,100)
intentos = 0 
num_usuario = 0

print("-"*40)
print("El juego consite en adivinar el numero")
print("-"*40)

def pedir_num():
    dato = int(input("ingresa un mumero:"))
    return dato

while num_usuario != num_secreto:
    intentos += 1
    try:
        num_usuario = pedir_num()
    except ValueError:
        print("Error: Ingrese un numero entero")
        continue
    
    if num_usuario > num_secreto:
        print("Mas bajo...")
    elif num_usuario < num_secreto:
        print("Mas alto...")

print(f"¡Ganaste en {intentos} intentos!")
