peso = float(input("¿Cuál es tu peso? (kg): ")) #Obtiene el peso en kilogramos
altura = float(input("¿Cuál es tu altura? (m): ")) #Obtiene la altura en metros
imc = peso / (altura ** 2) #Calcula el imc
print("Tu IMC es de:", imc) #Imprime el resultado