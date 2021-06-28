## else if

numero = float(input("Ingrese una nota del 1 al 5"))

if numero >= 4 and numero <= 4.5:
    print("Alto")
elif numero >= 3 and numero <= 3.9:
     print("Básico")
elif numero <= 2.9 and  numero >= 0.0:
    print("Bajo")
elif numero >= 4.6 and numero <= 5.0:
     print("Superior")
else:
    print("Nota no valido o no existe")