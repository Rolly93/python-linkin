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