class AnimalAero:
    def comer(self):
        print("Animal aereo comiendo")
    
    def volar(self):
        print("Volando")
    
class AnimalTerrestre:
    def comer(self):
        print("Animal terrestre comiendo")
    
    def caminar (self):
        print("Caminando")

class Pajaro(AnimalTerrestre,AnimalAero):
    pass

pato= Pajaro()
pato.volar()
pato.caminar()
pato.comer()