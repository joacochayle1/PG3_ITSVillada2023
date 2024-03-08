def es_numero_step(numero):
    
    str_numero = str(numero)
    
    
    longitud = len(str_numero)
    
    
    for i in range(longitud - 1):
        
        digito_actual = int(str_numero[i])
        digito_siguiente = int(str_numero[i + 1])
        
       
        if abs(digito_actual - digito_siguiente) != 1:
            return False
    
    
    return True

# Ejemplos de uso
numero_ejemplo_1 = 123234
numero_ejemplo_2 = 9876787654

print(es_numero_step(numero_ejemplo_1))  
print(es_numero_step(numero_ejemplo_2))  
