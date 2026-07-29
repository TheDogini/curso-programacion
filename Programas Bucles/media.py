#Imprime las instrucciones
print("Ingresa números positivos para obtener su media, ingresa un número negativo para salir")
#Inicializa las variables
suma = 0
conteo = 0
while True: #Cicla indeterminadamente
    numero = int(input("Tu número: ")) #Pregunta por un número
    if numero < 0: #Si el número es negativo, termina el ciclo
        break
    else: #Si no...
        suma += numero #Añade el número a la suma
        conteo += 1 #Añade 1 al conteo e números
#Calcula el promedio (media)
media = suma / conteo
#Imprime el resultado
print("La media de los números ingresados es de:", media)
print("Programa finalizado")