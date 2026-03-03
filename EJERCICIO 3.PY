import time 
hora = input("ingrese la hora actual (formato HH:MM AM/PM): ")
if hora == "6:00 AM":
    print("Es la hora de levantarse")
    inicio = time.time()

    while time.time() - inicio < 60: 
        print("🔔 SONANDO ALARMA 🔔")
        time.sleep(1)  

        apagar = input("Presione 's' para apagar la alarma o ENTER para continuar: ")
        if apagar.lower() == 's':
            print("Alarma apagada.")
            break
    else:
        print("La alarma se detuvo después de 1 minuto.")
else:
    print("No es hora de activar la alarma.")