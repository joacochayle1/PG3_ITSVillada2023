class Triangulo:
    def lados(self):
        lista_lados=[]
        self.lado1=input("Ingrese el primer lado: ")
        lista_lados.append(self.lado1)
        self.lado2=input("Ingrese el segundo lado: ")
        lista_lados.append(self.lado2)
        self.lado3=input("Ingrese el tercer lado: ")
        lista_lados.append(self.lado3)
        
        lado_mayor = max(lista_lados)
        if self.lado1==self.lado2==self.lado3:
            print(f"Todos los lados valen lo mismo: {lado_mayor}")
        else:    
            print(f"El lado mayor es: {lado_mayor} ")
        
    
    def equilatero(self):
        if (self.lado1 == self.lado2 == self.lado3):
            print("El triángulo es equilátero")
        else:
            print("No es equilatero")
            
  
triangulo=Triangulo()
triangulo.lados()
triangulo.equilatero()
 
        
   