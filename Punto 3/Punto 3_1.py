def decorador_mensaje(func):
    #Decorador que señala inicio y fin de una funcion, generalmente, los decoradores son utilizados para mantener y/o controlar flujos de funcionamiento
    #para facilitar el proceso de deteccion y correcion de errores
    def wrapper():
        print("Inicio de la función.")
        func()
        print("Fin de la función.")
    return wrapper

@decorador_mensaje
def funcion_principal():
    #Función principal que imprime un mensaje en pantalla.
    print("Esta es la función principal.")

# Prueba de la función decorada
funcion_principal()
