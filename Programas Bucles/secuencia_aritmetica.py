#Se pregunta por el primer número de la sucesión
numero = int(input("¿En qué número debería iniciar la secuencia?: "))
#Se pregunta por la diferencia de valores en la secuencia
diferencia = int(input("¿De cuánto es la diferencia?: "))
#Se pregunta hasta qué posición se debe llegar
posicion = int(input("¿Hastá qué posición se debe llegar?: "))
#Se inicializa un índice
indice = 0
#Se inicia un bucle while
while True:
    print(numero) #Se imprime el número
    numero += diferencia #Se suma el número con la diferencia para el siguiente ciclo
    indice += 1 #Se actualiza el índice
    if indice == posicion: #Si el índice ha llegado a la posición...
        print("Programa finalizado") #Se termina el bucle
        break