titular = input("Ingrese nombre del titular "),
cantidad = input("Ingrese la cantidad expresada en números ")
class Cuenta():

    def __init__(self,titular,cantidad=0):
        self.titular=titular
        self.__cantidad=cantidad
    
    def titular(self):
        return self.__titular
    
    def cantidad(self):
        return self.__cantidad

    def titular(self,titular):
        self.__titular=titular

       
    def mostrar(self):
        return "Cuenta\n"+"Titular:"+self.titular.mostrar()+" - Cantidad:"+str(self.cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad


