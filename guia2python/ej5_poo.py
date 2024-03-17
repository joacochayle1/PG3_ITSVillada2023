class Persona:
    def personita(self):
        self.nombre=input("Escriba el nombre: ")
        self.edad=int(input("Escriba la edad: "))
        self.responsabilidades=input("Escriba sus responsabilidades: ")
    def  mostrar(self):
        print(f"El nombre de la persona es: {self.nombre}")
        print(f"Tiene {self.edad} años")
        print(f"Sus responsabilidades son: {self.responsabilidades}")
        
class Empleado(Persona):
    def empleadito(self):
        self.sueldo=int(input("Ingrese su sueldo: "))
        if self.sueldo>=3000:
            print("Debe pagar impuestos")
        else:
            print("No tiene que pagar impustos")
    
    
persona=Persona()
persona.personita()
persona.mostrar()
empleado=Empleado()
empleado.empleadito()