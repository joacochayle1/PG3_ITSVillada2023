class Triangulo:
    def lados(self,lado1:int,lado2:int,lado3:int):
        lista_lados=[]
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
        lista_lados.append(self.lado1)
        lista_lados.append(self.lado2)
        lista_lados.append(self.lado3)
        for lado in lista_lados:
            if self.lado1>self.lado2 and self.lado1>self.lado3:
                print(f"El lado mayor es: {self.lado1} ")
            
        if self.lado2>self.lado1 and self.lado2>self.lado3:
            print(f"El lado mayor es: {self.lado2} ")
            
        if self.lado3>self.lado1 and self.lado3>self.lado2:
            print(f"El lado mayor es: {self.lado3} ")
        else:
            print(f"Todos los lados son iguales, miden: {self.lado1}cm")
    
    def equilatero(self):
        if (self.lado1 == self.lado2 == self.lado3):
            print("El triángulo es equilátero")
        else:
            print("No es equilatero")
            
  
triangulo=Triangulo()
triangulo.lados(2,2,2)
triangulo.equilatero()
 
        
   