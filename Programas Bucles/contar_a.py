#Pregunta al usuario la palabra a evaluar
palabra = input("Ingresa una palabra: ").lower()
#Inicializa la variable del resultado en 0
resultado = 0
#Cicla letra por letra en la palabra
for letra in palabra:
    if letra == 'a': #Si encuentra la letra 'a', suma 1 al resultado
        resultado += 1
#Imprime el resultado
print("La palabra contiene la letra 'a'", resultado, "veces")