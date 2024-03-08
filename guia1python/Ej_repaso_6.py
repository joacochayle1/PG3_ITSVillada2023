def es_vocal(palabra):
    contador_vocales=0
    vocales="aeiou"
    for i in palabra:
        if i in vocales:
            contador_vocales+=1
    return f"La palabra ingresada ({palabra}) tiene {contador_vocales} vocales"
    
palabraver=input("escriba una palabra para verificar cuantas vocales tiene: ").lower()
print(es_vocal(palabraver))