try:
    with open("\\wsl.localhost\Ubuntu\home\joacochayle\PG3_ITSVillada2023\PG3_ITSVillada2023\guia3python\\archivo.txt"),"W" as archivo:
        string=["Hola","Mundo",";D"]
        
        entero=123
        archivo.write(entero)
    
except TypeError:
    print("Escribiste un tipo de dato entero cuando solo se puede string.")
except Exception:
    print("Hiciste algo mal...")