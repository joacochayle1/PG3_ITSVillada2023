try:
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))
    suma = numero1 + numero2
    print(f"La suma de los dos numeros ingresados es: {suma}")

    lista_num = []
    lista_num.append(numero1)
    lista_num.append(numero2)

    pregunta = input("¿Quiere seguir añadiendo numeros? (s/n)").lower()
    if pregunta == "s":
        seguir = input("PRESIONE ENTER")
        while seguir != "n":
            try:
                numeros_extra = int(input("Agrega el siguiente numero: "))
                print("----------------------------------------------------")
                seguir = input("¿Quieres agregar otro numero? (s/n)")
                
                lista_num.append(numeros_extra)
            except ValueError:
                print("El dato ingresado no es numérico. Inténtalo de nuevo.")
    else:
        pass

    print(f"La suma de todos los números ingresados es: {sum(lista_num)}")

except ValueError:
    print("El dato ingresado no es numérico")
