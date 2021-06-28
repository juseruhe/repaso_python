## Número para operaciones
numero = int(input("Ingrese una opción del 1 al 4 \n 1. suma \n2. Resta \n3.Multiplicación \n4. División"))

if numero is 4:
       n1 = int(input("Ingrese un número para dividir: "))
       n2= int(input("Ingrese otro número para dividir:"))
       dividir= n1/n2
       print("La división es: ",dividir)
elif numero is 3:
       n1 = int(input("Ingrese un número para multiplicar: "))
       n2= int(input("Ingrese otro número para multiplicar:"))
       multiplicar= n1*n2
       print("La multiplicación es: ",multiplicar)
elif numero is 2:
       n1 = int(input("Ingrese un número para restar: "))
       n2= int(input("Ingrese otro número para restar:"))
       restar= n1-n2
       print("La resta es: ",restar)
elif numero is 1:
        n1 = int(input("Ingrese un número para sumar: "))
        n2=int(input("Ingrese otro número para sumar:"))
        sumar= n1+n2
        print("La suma es: ",sumar)
        
     
else:
    print("Nota no valido o no existe")
    
    
  