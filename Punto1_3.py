def encontrar_maximo(numeros):
    #Retorna el número mas alto encontrado en una lista de números. Al igual que "sum", "max" utiliza elementos de tipo iterable, y analia sus valores, determinando el valor
    #mas alto dentro del mismo. Segun la documentacion, en el caso que se encuentren 2 maximo (Consideremos 2 numeros de mismo valor (10, 2, 4, 10)) solo se devolvera la primera
    #ocurrencia
    return max(numeros)

# Casos de prueba
print("Valor maximo encontrado dentro de la lista 1: ", encontrar_maximo([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Salida: 9
print("Valor maximo encontrado dentro de la lista 2: ", encontrar_maximo([2, 6, 5]))                    # Salida: 6
