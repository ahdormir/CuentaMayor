from cuenta import Cuenta

class CuentaPlus(Cuenta):
    def __init__(self, nombre, edad, credito, bonificacion):
        super().__init__(nombre, edad, credito)
        self.bonificacion = bonificacion
        
        #getter
    def getBonificacion(self):
        return self.bonificacion
    
        #setter
    def setBonificacion(self,bonificacion):
        self.bonificacion = bonificacion

        #mostra detalles de cuenta
    def mostrardatos(self):
        print("=== datos ===\n-> " + self.nombre + "\n-> edad: " + str(self.getEdad()) + "\n-> credito: " + str(self.getCredito()) + "\n-> bonificacion: " + str(self.getBonificacion()))