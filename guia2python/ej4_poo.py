class Operacion:

    def __init__(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        s=self.valor1+self.valor2
        print(f"La suma es: {s}")

    def restar(self):
        r=self.valor1-self.valor2
        print(f"La resta es: {r}")

    def multiplicar(self):
        m=self.valor1*self.valor2
        print(f"El producto es: {m}")

    def dividir(self):
        d=self.valor1/self.valor2
        print(f"La division es: {d}")




operacion1=Operacion()