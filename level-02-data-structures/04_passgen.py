import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation
print("Password Generator")
print("-"*40)
password_length = int(input("¿Qué tan larga quieres la contraseña?\n"))
print("-"*40)
password = []
for i in range (password_length):

    random_characters = secrets.choice(characters)
    password.append(random_characters)

password = "".join(password)

print(password)