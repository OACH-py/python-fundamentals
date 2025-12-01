import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation
print("Password Generator")
while True:
    try:
        password_length = int(input("¿Qué tan larga quieres la contraseña? (solo números)\n"))
        if password_length <= 0:
            print("Error: La longitud debe ser un número positivo mayor que cero.")
            continue # Volver al inicio del ciclo (sin ejecutar el 'break')
        break
    except ValueError:
        print("Error: Ingresa un valor numérico válido.")

password = []
for i in range (password_length):

    random_characters = secrets.choice(characters)
    password.append(random_characters)

password = "".join(password)

print(password)