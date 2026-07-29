#Se pregunta el límite de números al usuario
limite = int(input("¿Hasta qué número deseas que se ejecute la secuencia de cuadrados?: "))
#Se inicialiaza la variable
indice = 1
while True:
    #Se calcula el resultado del cuadrado
    resultado = indice ** 2
    #Se imprime el resultado
    print(resultado)
    #Se añade 1 a la variable del índice
    indice += 1
    #Si el índice ha alcanzado el límite, se termina el ciclo
    if indice == limite + 1:
        print("Programa finalizado")
        break