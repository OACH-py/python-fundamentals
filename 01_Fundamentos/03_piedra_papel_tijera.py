import random

print("-"*30)
print("*Piedra, Papel o Tijera*")
print("-"*30)

ob = ["piedra", "papel", "tijera"]
pc_ganadas = 0
us_ganadas = 0 


def ganador(usuario,pc):
    reglas = {
        "piedra":"tijera",
        "papel":"piedra",
        "tijera":"papel"
    }
    if usuario == pc:
        return "empate"
    elif reglas[usuario] == pc:
        return "usuario"
    else:
        return "pc"


while True:
    pc = random.choice(ob)
    usuario = input("Tu turno (piedra, papel, tijera) o 'salir': ").lower().strip()

    if usuario == "salir":
        print("Gracias por jugar")
        break   
    if usuario not in ob:
        print("Ingresa una opcion valida")
        continue
    resultado = ganador(usuario,pc)
    if resultado == "usuario":
        print("¡Ganaste esta ronda!")
        us_ganadas += 1
    elif resultado == "pc":
        print("Perdiste esta ronda.")
        pc_ganadas += 1
    else:
        print("Empate.")

print("-"*30)
print("Contador de victorias")
print(f"La PC gano:{pc_ganadas}")
print(f"El usuario gano:{us_ganadas}")