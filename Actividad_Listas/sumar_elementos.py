def sumar_lista(lista):
    """Función que suma todos los
    elementos de una lista"""
    suma = 0
    for num in lista:
        suma += num
    return suma
#Inicializa la lista
numeros = []
for i in range (5):
    #Pregunta con un valor
    valor = int(input(f"Ingrese valor {i+1}: "))
    #Añade el valor a una lista
    numeros.append(valor)
#Manda a llamar la función
total = sumar_lista(numeros)
total_sum = sum(numeros) #usando función built-in
#Imprime lso resultados
print("Suma con bucle:", total)
print("Suma con sum():", total_sum)