import time
nivel = 50
valvula_abierta = False
while True:
    print(f"\nNivel actual del tanque: {nivel}")
    nivel -= 5
    if nivel < 0:
        nivel = 0
    if nivel == 0:
        print("Sensor de tanque vacío activado")
        valvula_abierta = True
        print("Válvula ABIERTA")
    if nivel == 100:
        print("Sensor de tanque lleno activado")
        valvula_abierta = False
        print("Válvula CERRADA")
        if valvula_abierta:
            nivel = 10
    if nivel > 100:
            nivel = 100
    time.sleep(1)