import random

print("-"*30)
print("*Piedra, Papel o Tijera*")
print("-"*30)

ob = ["piedra", "papel", "tijera"]
pc_ganadas = 0
us_ganadas = 0 
reglas = {
    "piedra":"tijera",
    "papel":"piedra",
    "tijera":"papel"
}

def juego(ob):
    while True:
        pc = random.choice(ob)
        usuario = input("Tu turno (piedra, papel, tijera) o 'salir': ").lower().strip()

        if usuario == "salir":
            print("Gracias por jugar")
            break
        if usuario not in ob:
            print("Ingresa una opcion valida")
            continue

        print(f"La pc escojio:{pc}")

        if usuario == pc:
            print("⚖️ Empate")
            continue
        elif reglas[usuario] == pc:
            print("🏆 Tu ganas") 
        else:
            print("💀 Tu pierdes")
juego(ob)

print("-"*30)
print("Contador de victorias")
print(f"La PC gano:{pc_ganadas}")
print(f"El usuario gano:{us_ganadas}")