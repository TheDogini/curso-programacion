def maximo_manual(lista):
    """Función para encontrar el valor máximo"""
    if len(lista) == 0:
        return None
    maximo = lista[0]
    for num in lista[1:]:
        if num > maximo:
            maximo = num
    return maximo

def minimo_manual(lista):
    """Función para encontrar el valor mínimo"""
    if len(lista) == 0:
        return None
    minimo = lista[0]
    for num in lista:
        if num < minimo:
            minimo = num
    return minimo
#Inicializar la lista
numeros = []
for i in range(8):
    #Pedir los números al usuario
    valor = int(input(f"Número {i+1}: "))
    #Añadir los números a la lista
    numeros.append(valor)
#Llamar a las funciones
mayor_manual = maximo_manual(numeros)
menor_manual = minimo_manual(numeros)
#Imprimir los resultados
print("Mayor (manual):", mayor_manual)
print("Menor (manual):", menor_manual)