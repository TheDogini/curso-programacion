#Imprime las instrucciones
print("Ingresa números, y el programa contará cuántos de ellos son impares (0 para salir)")
#Inicializa la variable
impares = 0
while True: #Inicia un ciclo indefinido
    numero = int(input("Número: ")) #Pregunta por un número
    if numero == 0: #Si el número es 0, termina el ciclo
        break
    elif numero % 2 == 1: #Evalúa si es impar, y si lo es, añade uno a la variable
        impares +=1
#Imprime el resultado
print("Cantidad de números impares ingresados:", impares)
print("Programa finalizado")