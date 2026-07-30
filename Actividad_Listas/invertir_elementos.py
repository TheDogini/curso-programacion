def ineverir_manual(lista):
    """Función para invertir una lista"""
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    return invertida
#Inicializar la lista
numeros = []
for i in range(6):
    #Pedir los valores a evaluar
    valor = int(input(f"Número {i+1}: "))
    #Añadir los valores a la lista
    numeros.append(valor)
#Imprime la lista original de elementos
print("Original:", numeros)
#Manda a llamar la función
invertida = ineverir_manual(numeros)
#Imprime la lista invertida
print("Invertida:", invertida)