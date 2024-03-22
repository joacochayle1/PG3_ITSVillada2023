class Persona:
    def personita(self):
        self.nombre=input("Escriba el nombre: ")
        self.edad=int(input("Escriba la edad: "))
       
    def  mostrar(self):
        print(f"El nombre de la persona es: {self.nombre}")
        print(f"Tiene {self.edad} años")
      
        
class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo=int(input("Ingrese su sueldo: "))
        if self.sueldo>=3000:
            print(f"{self.nombre} debe pagar impuestos")
        else:
            print("No tiene que pagar impustos")
    
    
persona=Persona()
persona.personita()
persona.mostrar()
empleado=Empleado()
empleado.empleadito()