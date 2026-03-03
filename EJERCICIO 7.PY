voto = input("Ingrese el candidato por el que desea votar (A, M, N): ").upper()

voto = voto.upper()

if voto == "A":
    print("Usted ha votado por el partido Amarillo")

elif voto == "M":
    print("Usted ha votado por el partido Morado")

elif voto == "N":
    print("Usted ha votado por el partido Naranja")

else:
    print("Opción errónea")