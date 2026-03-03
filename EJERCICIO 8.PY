x = 0
y = 0

print("Posición inicial: (0, 0)\n")

for lanzamiento in range(1, 11):
    dado = int(input(f"Ingrese el resultado del lanzamiento {lanzamiento} (1-4): "))

    if dado == 1:
        x += 1
    elif dado == 2:
        y -= 1
    elif dado == 3:
        x -= 1
    elif dado == 4:
        y += 1
    else:
        print("Valor inválido")

    print(f"Posición actual: ({x}, {y})\n")

print("Posición final:", (x, y))