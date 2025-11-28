def calculadora_propinas ():
    print("--- Calculadora de Propinas ---")

    try:
        cuenta = float(input("💰 ¿Cuál fue el total de la cuenta?: $"))
        propina_pct = float(input("📈 ¿Qué % de propina deseas dar?: "))
        personas = int(input("busts_in_silhouette ¿Entre cuántas personas se divide?: "))

        if personas <= 0:
            print("Error: El numero de personas debe ser mayor a 0")
            return
        propina = cuenta * (propina_pct / 100)
        total = cuenta + propina 
        pago_persona = total / personas
    except ValueError:
        print("❌ Error: Ingresa valores validos ")