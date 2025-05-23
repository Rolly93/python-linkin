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
        super().ejecutar_accion()  
        print(f"Practicando {self.deporte}")

pedro = Deportista("Pedro","Cortez",26,"Soccer")
pedro.agregar_documento_identidad(1254)
print(pedro.deporte)
pedro.ejecutar_accion()