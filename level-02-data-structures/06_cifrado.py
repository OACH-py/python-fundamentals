def cifrado_cesar(texto,desplazamiento):

    abecedario = "abcdefghijklmnopqrstuvwxyz"
    texto_resultado = []
    texto = texto.lower()

    for letra in texto:
        if letra in abecedario:
            indice_actual = abecedario.find(letra)
            indice_nuevo = (indice_actual + desplazamiento) % 26
            letra_nueva = abecedario[indice_nuevo]
            texto_resultado.append(letra_nueva)
        else:
            texto_resultado.append(letra)
    
    return "".join(texto_resultado)

def fuerza_bruta_cesar(texto_cifrado):

    abecedario = "abcdefghijklmnopqrstuvwxyz"
    texto_cifrado = texto_cifrado.lower()

    for clave_prueba in range(1,26):
        texto_resultado = []
        for letra in texto_cifrado:
            if letra in abecedario:
                indice_actual = abecedario.find(letra)
                indice_nuevo = (indice_actual - clave_prueba) % 26
                
                letra_nueva = abecedario[indice_nuevo]
                texto_resultado.append(letra_nueva)
            else:
                texto_resultado.append(letra)
        mensaje_final = "".join(texto_resultado)
        print(f"Clave {clave_prueba}: {mensaje_final}")

while True:
    try:
        print("-" * 30)
        print("¿Qué desea realizar?")
        print("1. Cifrar un texto")
        print("2. Descifrar un texto")
        print("3. Salir") 
        
        opcion = input("Seleccione una opción: ")
        print("-" * 30)

        if opcion == "1":
            texto = input("Ingresa el texto a cifrar: ")
            desplazamiento = int(input("Ingresa la clave del cifrado (1-26): "))
            
            resultado = cifrado_cesar(texto, desplazamiento)
            print(f"Texto cifrado: {resultado}")

        elif opcion == "2":
            texto_cifrado = input("Ingresa el texto a descifrar: ")
            fuerza_bruta_cesar(texto_cifrado)

        elif opcion == "3":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

    except ValueError:
        print("Error: Debes ingresar un número válido para el desplazamiento.")
        continue