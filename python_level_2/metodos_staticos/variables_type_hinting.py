from typing import List,Tuple,Dict

#variables tipadas
nombre :str = "Anan"

edad :int = 25
pi: float = 3.1416
#apellidos :list[str]=["Guadalupe","Rios","Lopez"]
apellidos :List[str]=["Guadalupe","Rios","Lopez"]

#lenguajes_programacion :tuple=("python","java","javascript","golang")
lenguajes_programacion :Tuple[str,str,str,str]=("python","java","javascript","golang")

#lenguaje: dict = {    "nombre":"python",    "creador":"Guido Van Rossum"}
lenguaje: Dict[str,str] = {
    "nombre":"python",
    "creador":"Guido Van Rossum"
}