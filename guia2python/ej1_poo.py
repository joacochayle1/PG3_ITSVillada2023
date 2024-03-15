class Persona:
    def inicializar(self,nombre:str):
        self.nom=nombre
        
    def mostrar(self):
        print("El nombre es",self.nom)
persona=Persona()
persona.inicializar("El Pepe")
persona.mostrar()

persona2=Persona()
persona2.inicializar("Ete Sech")
persona2.mostrar()
    