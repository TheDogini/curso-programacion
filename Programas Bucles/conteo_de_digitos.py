#Pide al usuario el número a evaluar
numero = int(input("Ingresa un número para contar sus dígitos: "))
#Inicializa la variable
digitos = 0
#Inicia un ciclo
for i in range(0, numero):
    if numero == 0: #Si el número llega a 0, el ciclo acaba
        break
    else: #Si no...
        digitos += 1 #Se agrega 1 a la variable del resultado
        #Se realiza una división entera entre 10 para "recorrer el punto" del número
        numero = numero // 10 
#Se imprime le resultado
print("El número tiene", digitos, "dígitos")