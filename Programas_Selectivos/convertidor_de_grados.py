#Se obtiene la temperatura a evaluar
temperatura_C = float(input("¿Cuál es tu temperatura? (C): "))

#Se pregunta a qué se debe convertir
conversion = input("¿A qué los deseas convertir? ('F' o 'K'): ").upper()

#Se selecciona la temperatura correspondiente
match conversion:
    case "F":
        #Se calcula la temperatura final
        temperatura_final = (temperatura_C * 1.8) + 32
        #se imprime el resultado
        print("La temperatura es de: ", temperatura_final, "°F", sep="")
    case "K":
        #Se calcula la temperatura final
        temperatura_final = temperatura_C + 273.15
        #se imprime el resultado
        print("La temperatura es de: ", temperatura_final, "°K", sep="")
    case _:
        #Mensaje de error si hay un error en la selección de operación
        print("Error, conversión inválida")