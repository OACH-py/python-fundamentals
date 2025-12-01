import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation
print("-"*30)
print("Password Generator")
while True:
    try:
        print("-"*30)
        password_length = int(input("¿Qué tan larga quieres la contraseña? (solo números)\n"))
        if password_length <= 0:
            print("-"*30)
            print("Error: La longitud debe ser un número positivo mayor que cero.")
            continue # Volver al inicio del ciclo (sin ejecutar el 'break')
        break
    except ValueError:
        print("-"*30)
        print("Error: Ingresa un valor numérico válido.")

password = []
for i in range (password_length):

    random_characters = secrets.choice(characters)
    password.append(random_characters)

password = "".join(password)
print("-"*password_length)
print(password)
print("-"*password_length)