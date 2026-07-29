#Imprime las instrucciones
print("Ingresa una letra, y el programa te dirá si es vocal o consonante (ingresa ' ' para terminar)")
while True:
    #Pregunta al usuario por su letra
    letra = input("Tu letra: ").lower()
    if letra == " ": #Si es un espacio, termina el ciclo
        print("Programa terminado")
        break
    elif letra in ("aeiou"): #Busca si la letra está en alguna de las vocales
        print("Es vocal") #Imprime el diagnóstico
    else: #Si no es una vocal, debe ser consonante
        print("Es consonante") #Imprime el resultados