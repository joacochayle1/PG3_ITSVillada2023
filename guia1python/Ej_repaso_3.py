ancho=int(input("Ingrese el ancho: "))
alto=int(input("Ingrese el alto: "))
caracter=input("Ingrese el caracter que va a usar: ")
for n in range(1,alto+1):
    print(f"{caracter*(ancho)}")
