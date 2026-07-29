#Pregunta el número a evaluar
numero = int(input("¿De cuál número deseas obtener su factorial?: "))

#Inicializa la variable del resultado
resultado = 1

#Cicla del 1 en adelante hasta llegar al número obtenido
for i in range(1, numero + 1):
    resultado *= i #Multiplica el resultado por el índice

#Imprime el resultado
print("El factorial de", numero, "es:", resultado)