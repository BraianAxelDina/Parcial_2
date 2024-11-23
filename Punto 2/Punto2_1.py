#Se crea la clase "Persona"
class Persona:
    #Se define como atributos Nombre de tipo string y edad de tipo int
    nombre = (str)
    edad = (int)
    #Se construye, dichos atributos para utilizar posteriormente dentro de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #Se crea la funcion de uso interno de la clase saludar, que toma los atributos propios de la clase (Self) Nombre y edad para imprimir estos por pantalla
    def saludar(self):
         print("Hola, mi nombre es" , self.nombre , "y tengo", self.edad ,"años.")

# Prueba de la clase

persona1 = Persona("Juan", 25)
persona1.saludar()
