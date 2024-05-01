class Cuenta:
    def __init__(self, nombre, edad, credito):
        self.nombre = nombre
        self.edad = edad
        self.credito = credito
        
        #getters
    def getNombre(self):
        return self.nombre
    
    def getEdad(self):
        return self.edad
    
    def getCredito(self):
        return self.credito
    
        #setters
    def setEdad(self,edad):
        self.edad = edad

    def setNombre(self,nombre):
        self.nombre = nombre

    def setCredito(self,credito):
        self.credito = credito    
    
        #mostra detalles de cuenta
    def mostrardatos(self):
        print(f"=== datos ===\n-> {self.nombre}\n-> edad: {self.edad}\n-> credito: {self.credito}")