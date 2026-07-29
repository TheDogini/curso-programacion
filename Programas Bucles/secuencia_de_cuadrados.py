#Imprime las instrucciones
print("Ingresa números y el programa te dará el cuadrado de ellos (0 para salir)")
while True: #Inicializa el ciclo indefinido
    numero = int(input("Número: ")) #Pide el número al usuario
    if numero == 0: #Si el número es 0, finaliza el ciclo
        print("Programa finalizado")
        break
    else:
        resultado = numero ** 2 #Si no, calcula el cuadrado y lo imprime
        print("El cuadrado de", numero, "es:", resultado)