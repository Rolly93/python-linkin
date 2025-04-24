class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.documentos_identidad = None
    
    def agregar_documento_identidad(self,numero_documento):
        self.documentos_identidad= numero_documento
        print("Documento guardado")

    
    def ejecutar_accion(self):
        print("Haciendo algo")
    
class Deportista(Persona):
    def __init__(self, nombre, apellido, edad , deporte):
        super().__init__(nombre, apellido, edad)
        self.deporte = deporte
    
    def ejecutar_accion(self):
        # se tiene la opcion de mandar llamar el metodo de la clase padre  como no mandar a llamarlo
        #super().ejecutar_accion()  
        print(f"Practicando {self.deporte}")

class Ciclista(Deportista):
    def __init__(self, nombre, apellido, edad):
        self.deporte = "Ciclismo"
        super().__init__(nombre, apellido, edad, self.deporte)
    
    def pedalear(self):
        print("Pedaleando")

nairo =Ciclista("Nairo","Quintana",33)
nairo.ejecutar_accion()
nairo.agregar_documento_identidad(125)
nairo.pedalear()