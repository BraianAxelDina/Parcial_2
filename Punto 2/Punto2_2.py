class Rectangulo:
    #Se crean los atributos alto y ancho y se les brinda el tipo de dato
        ancho = (float)
        alto = (float)

        def __init__(self, ancho, alto):
        #Construccion de los atributos
            self.ancho = ancho
            self.alto = alto
        #Creamos la funcion para el area
        def area(self):
            #Dado que el area de un rectangulo es la multiplicacion del ancho por alto, realizamos un retorno directo del resultado de dicha operacion a quien llame la funcion
            return self.ancho * self.alto
        #Creamos la funcion para el perimetro
        def perimetro(self):
            #Dado que el perimetro de un rectangulo cumple la formula (P=2L+2W), donde "L" es la longitud y "W" es el ancho del rectángulo. 
            #Generamos un retorno con dicha formula
            return 2 * (self.ancho + self.alto)

# Prueba de la clase

rectangulo1 = Rectangulo(4, 7)
print ("El ancho de nuestro rectangulo es",rectangulo1.ancho,"y el alto es de",rectangulo1.alto)
print("El area de nuestro rectangulo es:", rectangulo1.area())       # Salida: 28
print("El perimetro de nuestro rectangulo es:", rectangulo1.perimetro())  # Salida: 22
