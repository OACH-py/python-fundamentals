def calculadora_propinas ():
    print("--- Calculadora de Propinas ---")

    try:
        cuenta = float(input("💰 ¿Cuál fue el total de la cuenta?: $"))
        propina_pct = float(input("📈 ¿Qué % de propina deseas dar?: "))
        personas = int(input("¿Entre cuántas personas se divide?: "))
    
        if personas <= 0:
            print("Error: El numero de personas debe ser mayor a 0")
            return
        propina = cuenta * (propina_pct / 100)
        total = cuenta + propina 
        pago_persona = total / personas
        
        print("---Datos de la Cuenta---")
        print("-"*30)
        print(f"Subtotal:${cuenta:,.2f}")
        print(f"Propina:${propina_pct:,.2f}")
        print(f"Total:${total:,.2f}")
        print("-"*30)
        print(f"Cada uno paga:{pago_persona:,.2f}")

    except ValueError:
        print("❌ Error: Ingresa valores validos ")
calculadora_propinas()
