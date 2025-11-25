"""Brandon Montoya Vidales 
Manuela Osorio Galvan
Jose Fernando Perea"""



class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido")
class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato maulla")  

# Función que aplica polimorfismo
def reproducir_sonido(animal):
    animal.hacer_sonido()

reproducir_sonido(Perro())  # Salida: El perro ladra
reproducir_sonido(Gato())   # Salida: El gato maulla
