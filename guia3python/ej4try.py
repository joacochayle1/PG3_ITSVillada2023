try:
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))
    division = numero1/numero2
    print(f"La división de los dos numeros ingresados es: {division}")
except ZeroDivisionError:
    print("La division no es dividible por 0")
except ValueError:
    print("Ingresa números solamente")