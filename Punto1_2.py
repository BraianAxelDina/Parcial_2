def sumar_lista(numeros):
    #Retorna la sumatoria de todos los números en una lista. Se utiliza la funcion interna "sum" de python que puede ser utilizada en cualquier objeto
    #de tipo iterable, esto funciona de igual forma que un loop de tipo num = num + iterVal
    return sum(numeros)

# Casos de prueba
print("El resultado de la suma de todos los valores de la lista 1 es: ", sumar_lista([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Salida: 36
print("El resultado de la suma de todos los valores de la lista 2 es: ", sumar_lista([5, 9]))                       # Salida: 14
