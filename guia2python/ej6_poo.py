class Familia:
    def __init__(self):
        self.lista_hijos=[]
        self.nom_padre=input("ingrese el nombre del padre: ")
        self.nom_madre=input("ingrese el nombre de la madre: ")
        self.hijos=int(input("ingrese la cantidad de hijos que tienen: "))
        for hijo in range(self.hijos):
            hijo=input("Escriba el nombre de su hijo: ")
            self.lista_hijos.append(hijo)
    def __str__(self):
        union_lista = ", ".join(self.lista_hijos) 
        return f"El nombre del padre es {self.nom_padre}, el nombre de la madre es: {self.nom_madre} y sus hijos son {union_lista}"
    
flia=Familia()
print(flia)