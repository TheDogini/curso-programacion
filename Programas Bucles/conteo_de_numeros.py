#Pregunta al usuario cuántos números va a ingresar
limite = int(input("¿Cuántos núemros deseas contar?: "))
#Inicializa las variables
mayores = 0
menores = 0
iguales = 0
for i in range(0, limite):
    #Pregunta el número a evaluar
    numero = int(input("Número: "))
    #Evalúa el núemro ingresado
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1
#Imprime los resultados
print("Proceso terminado")
print("Números mayores a 0:", mayores)
print("Números menores a 0:", menores)
print("Números iguales a 0:", iguales)