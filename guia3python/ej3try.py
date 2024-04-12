meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
try:
    numero_mes = int(input("Ingresa el número de mes (1-12): "))
    
    
    if 1 <= numero_mes <= 12:
        nombre_mes = meses[numero_mes - 1]  
        print(f"El nombre del mes es: {nombre_mes}")
    else:
        print("Número de mes fuera de rango.")
        
except ValueError:
    print("Debes ingresar un número entero.")
except IndexError:
    print("Número de mes fuera de rango.")