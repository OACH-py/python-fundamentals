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

while True:
    password = []
    for i in range (password_length):

        random_char = secrets.choice(characters)
        password.append(random_char)
        
    password = "".join(password)
    
    has_letter = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char in string.ascii_letters:
            has_letter = True
        if char in string.digits:
            has_digit = True
        if char in string.punctuation:
            has_symbol = True
    
    if has_digit and has_letter and has_symbol:
        break

print("-"*password_length)
print(f"Tu contraseña es:\n{password}")
print("-"*password_length)