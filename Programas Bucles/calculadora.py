#Título del programa
print("CALCULADORA BÁSICA")
while True:
    #Pide al usuario el primero número
    numero_1 = int(input("Ingresa el primer número: "))
    #Menú de operaciones
    print("Selecciona el número de tu operación")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    operacion = int(input("Tu opción: "))
    #Verifica el número de operación y actúa acorde a él
    match operacion:
        case 1:
            numero_2 = int(input("Ingresa el segundo número: "))
            print(numero_1, "+", numero_2)
            resultado = numero_1 + numero_2
            print("El resultado de tu suma es:", resultado)
        case 2:
            numero_2 = int(input("Ingresa el segundo número: "))
            print(numero_1, "-", numero_2)
            resultado = numero_1 - numero_2
            print("El resultado de tu resta es:", resultado)
        case 3:
            numero_2 = int(input("Ingresa el segundo número: "))
            print(numero_1, "*", numero_2)
            resultado = numero_1 * numero_2
            print("El resultado de tu multiplicación es:", resultado)
        case 4:
            numero_2 = int(input("Ingresa el segundo número: "))
            print(numero_1, "/", numero_2)
            resultado = numero_1 / numero_2
            print("El resultado de tu división es:", resultado)
        case _:
            print("Error, elige un número de operación válido")
    #Pregunta al usuario si desea hacer otra operación
    opcion = input("¿Desea continuar? (s/n): ")
    if opcion == "n": #Si no es así, termina el ciclo
        break