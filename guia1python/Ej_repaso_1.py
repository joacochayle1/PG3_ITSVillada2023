lista=[2,5,6,7]
def encontrar_num(lista,elemento):
    for n in lista:
        if elemento==n:
            print(f"el elemento que buscaste a sido encontrado: {elemento}, se encuentra en el lugar {lista.index(n)}")
            break
        else:
            print("el elemento no a sido encontrado")
            
        
            
            
    
encontrar=encontrar_num(lista,3)
