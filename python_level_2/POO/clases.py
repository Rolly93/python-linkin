class Empleado:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        self.horas_trabajadas =0

    def trabajar(self,horas):
        self.horas_trabajadas += horas
        print(f"se han añadido {horas} de trabajo")
        print(f"Ha trabajado en total {self.horas_trabajadas} horas")

