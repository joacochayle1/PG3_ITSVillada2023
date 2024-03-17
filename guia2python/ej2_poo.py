class Alumno:
    
    def inicializar(self,nombre:str,nota:int):
        self.nombre=nombre
        self.nota=nota
        
    def mostrar(self):
        print("Su nombre es ",self.nombre)
        print("tiene un ",self.nota)
    def mostrar_estado(self):
        if self.nota>=8:
            print("Excelente")
        elif self.nota>=4:
            print("Regular")
        else:
            print("Libre")
alumno1=Alumno()
alumno1.inicializar("El Pepe",2)
alumno1.mostrar()
alumno1.mostrar_estado()
alumno2=Alumno()
alumno2.inicializar("Ete Sech",10)
alumno2.mostrar()
alumno2.mostrar_estado()

