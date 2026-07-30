def contar_pares_impares(numeros):
    """Función para contar números,
    separados en pares e impares"""
    pares = 0
    impares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares
#Inicializa la lista de números
numeros = []
for i in range(10):
    #Pregunta por 10 números
    num = int(input("Número {}: ". format(i+1)))
    #Los añade a la lista
    numeros.append(num)
#Manda a llamar la lista para asignar valores a pares e impares
p, i = contar_pares_impares(numeros)
#Imprime los resultados
print("Pares:", p)
print("Impares:", i)